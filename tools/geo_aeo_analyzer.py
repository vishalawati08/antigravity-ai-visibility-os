from bs4 import BeautifulSoup
import re


def analyze_geo_aeo(html):

    soup = BeautifulSoup(html, "html.parser")

    score = 100

    issues = []

    # =========================
    # FAQ DETECTION
    # =========================
    faq_found = False

    faq_keywords = [
        "faq",
        "frequently asked questions"
    ]

    page_text = soup.get_text().lower()

    for keyword in faq_keywords:

        if keyword in page_text:
            faq_found = True
            break

    if not faq_found:
        score -= 15
        issues.append("No FAQ section found")

    # =========================
    # TABLE DETECTION
    # =========================
    tables = soup.find_all("table")

    if len(tables) == 0:
        score -= 10
        issues.append("No structured tables found")

    # =========================
    # NUMBERED LIST DETECTION
    # =========================
    ordered_lists = soup.find_all("ol")

    if len(ordered_lists) == 0:
        score -= 10
        issues.append("No numbered lists found")

    # =========================
    # ANSWER BLOCK DETECTION
    # =========================
    paragraphs = soup.find_all("p")

    answer_blocks = 0

    for p in paragraphs:

        text = p.get_text(strip=True)

        words = text.split()

        if 40 <= len(words) <= 80:
            answer_blocks += 1

    if answer_blocks == 0:
        score -= 20
        issues.append("No AI-friendly answer blocks detected")

    # =========================
    # SCHEMA DETECTION
    # =========================
    schema = soup.find_all(
        "script",
        attrs={"type": "application/ld+json"}
    )

    if len(schema) == 0:
        score -= 20
        issues.append("No schema markup detected")

    # =========================
    # FRESHNESS SIGNALS
    # =========================
    years = re.findall(r"202[4-9]", page_text)

    if len(years) == 0:
        score -= 10
        issues.append("No freshness signals detected")

    # Prevent negative score
    if score < 0:
        score = 0

    return {
        "geo_score": score,
        "answer_blocks": answer_blocks,
        "tables_found": len(tables),
        "numbered_lists": len(ordered_lists),
        "schema_found": len(schema),
        "issues": issues,
    }