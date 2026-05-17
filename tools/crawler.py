from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

from tools.geo_aeo_analyzer import analyze_geo_aeo
from tools.strategist_engine import generate_strategic_insights
from tools.serp_analyzer import analyze_serp


def crawl_website(url):

    with sync_playwright() as p:

        # ====================================
        # LAUNCH BROWSER
        # ====================================

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-http2",
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox"
            ]
        )

        # ====================================
        # CREATE PAGE
        # ====================================

        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )

        try:

            # ====================================
            # LOAD WEBSITE
            # ====================================

            page.goto(
                url,
                timeout=30000,
                wait_until="commit"
            )

            # Wait for partial JS rendering
            page.wait_for_timeout(5000)

            # Get HTML
            html = page.content()

        except Exception as e:

            print(f"\nERROR LOADING WEBSITE:\n{e}")

            browser.close()

            return {
                "title": "Error",
                "description": "Could not load website",
                "h1_tags": [],
                "total_links": 0,
                "total_images": 0,
                "missing_alt_count": 0,
                "word_count": 0,
                "seo_score": 0,
                "issues": ["Website could not be crawled"],

                "geo_score": 0,
                "geo_issues": ["No GEO analysis available"],
                "answer_blocks": 0,
                "tables_found": 0,
                "schema_found": 0,

                "executive_summary": "Website could not be analyzed.",

                "strategic_insights": [],

                "priority_actions": [],

                "serp_keyword": "",
                "serp_results": [],
                "serp_insights": []
            }

        # ====================================
        # PARSE HTML
        # ====================================

        soup = BeautifulSoup(html, "html.parser")

        # ====================================
        # TITLE
        # ====================================

        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "No Title"
        )

        # ====================================
        # META DESCRIPTION
        # ====================================

        meta_desc = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        description = (
            meta_desc.get("content").strip()
            if meta_desc and meta_desc.get("content")
            else ""
        )

        # ====================================
        # H1 TAGS
        # ====================================

        h1_tags = [
            h1.get_text(strip=True)
            for h1 in soup.find_all("h1")
        ]

        # ====================================
        # LINKS
        # ====================================

        links = [
            a.get("href")
            for a in soup.find_all("a", href=True)
        ]

        # ====================================
        # IMAGES
        # ====================================

        images = soup.find_all("img")

        missing_alt = []

        for img in images:

            if not img.get("alt"):

                missing_alt.append(img.get("src"))

        # ====================================
        # WORD COUNT
        # ====================================

        text = soup.get_text(separator=" ")

        words = text.split()

        word_count = len(words)

        # ====================================
        # SEO SCORING
        # ====================================

        score = 100

        issues = []

        # Title check
        if len(title) < 30:

            score -= 10

            issues.append("Title too short")

        # Meta description check
        if len(description) < 50:

            score -= 10

            issues.append(
                "Meta description missing or too short"
            )

        # H1 checks
        if len(h1_tags) == 0:

            score -= 15

            issues.append("Missing H1 tag")

        if len(h1_tags) > 1:

            score -= 10

            issues.append("Multiple H1 tags found")

        # ALT text checks
        if len(missing_alt) > 0:

            score -= 10

            issues.append(
                f"{len(missing_alt)} images missing ALT text"
            )

        # Thin content checks
        if word_count < 300:

            score -= 10

            issues.append("Thin content detected")

        # Prevent negative score
        if score < 0:

            score = 0

        # ====================================
        # GEO / AEO ANALYSIS
        # ====================================

        geo_result = analyze_geo_aeo(html)

        # ====================================
        # SERP ANALYSIS
        # ====================================

        search_keyword = title

        serp_result = analyze_serp(search_keyword)

        # ====================================
        # STRATEGIST ENGINE
        # ====================================

        strategy_result = generate_strategic_insights({

            "seo_score": score,

            "h1_tags": h1_tags,

            "word_count": word_count,

            "missing_alt_count": len(missing_alt),

            "geo_score": geo_result["geo_score"],

            "answer_blocks": geo_result["answer_blocks"],

            "schema_found": geo_result["schema_found"],

            "tables_found": geo_result["tables_found"],

            "serp_insights": serp_result["insights"]
        })

        # ====================================
        # CLOSE BROWSER
        # ====================================

        browser.close()

        # ====================================
        # RETURN RESULTS
        # ====================================

        return {

            # SEO
            "title": title,
            "description": description,
            "h1_tags": h1_tags,
            "total_links": len(links),
            "total_images": len(images),
            "missing_alt_count": len(missing_alt),
            "word_count": word_count,
            "seo_score": score,
            "issues": issues,

            # GEO / AEO
            "geo_score": geo_result["geo_score"],
            "geo_issues": geo_result["issues"],
            "answer_blocks": geo_result["answer_blocks"],
            "tables_found": geo_result["tables_found"],
            "schema_found": geo_result["schema_found"],

            # STRATEGIST
            "executive_summary": strategy_result["executive_summary"],
            "strategic_insights": strategy_result["strategic_insights"],
            "priority_actions": strategy_result["priority_actions"],

            # SERP
            "serp_keyword": serp_result["keyword"],
            "serp_results": serp_result["results"],
            "serp_insights": serp_result["insights"]
        }