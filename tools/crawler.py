from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


# =========================================
# PAGE ANALYZER
# =========================================

def analyze_page(

    html,

    url
):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    data = {

        "url": url,

        "title": "",

        "meta_description": "",

        "h1_tags": [],

        "h2_tags": [],

        "paragraphs": [],

        "internal_links": [],

        "word_count": 0,

        "schema_found": False,

        "faq_detected": False
    }

    # =====================================
    # TITLE
    # =====================================

    if soup.title:

        data["title"] = soup.title.text.strip()

    # =====================================
    # META DESCRIPTION
    # =====================================

    meta = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    if meta:

        data["meta_description"] = meta.get(
            "content",
            ""
        )

    # =====================================
    # H1 TAGS
    # =====================================

    data["h1_tags"] = [

        h.get_text(strip=True)

        for h in soup.find_all("h1")
    ]

    # =====================================
    # H2 TAGS
    # =====================================

    data["h2_tags"] = [

        h.get_text(strip=True)

        for h in soup.find_all("h2")
    ]

    # =====================================
    # PARAGRAPHS
    # =====================================

    paragraphs = [

        p.get_text(" ", strip=True)

        for p in soup.find_all("p")
    ]

    data["paragraphs"] = paragraphs

    full_text = " ".join(paragraphs)

    data["word_count"] = len(
        full_text.split()
    )

    # =====================================
    # SCHEMA DETECTION
    # =====================================

    schema_tags = soup.find_all(

        "script",

        attrs={
            "type": "application/ld+json"
        }
    )

    if schema_tags:

        data["schema_found"] = True

    # =====================================
    # FAQ DETECTION
    # =====================================

    page_text = soup.get_text(
        " ",
        strip=True
    ).lower()

    faq_keywords = [

        "faq",

        "frequently asked questions"
    ]

    for keyword in faq_keywords:

        if keyword in page_text:

            data["faq_detected"] = True

    # =====================================
    # INTERNAL LINKS
    # =====================================

    parsed_domain = urlparse(url).netloc

    for link in soup.find_all("a"):

        href = link.get("href")

        if not href:

            continue

        absolute_url = urljoin(
            url,
            href
        )

        if parsed_domain in absolute_url:

            data["internal_links"].append(
                absolute_url
            )

    return data


# =========================================
# MAIN WEBSITE CRAWLER
# =========================================

def crawl_website(url):

    visited = set()

    pages_to_visit = [url]

    crawled_pages = []

    max_pages = 5

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            while (

                pages_to_visit

                and

                len(crawled_pages) < max_pages
            ):

                current_url = pages_to_visit.pop(0)

                if current_url in visited:

                    continue

                visited.add(current_url)

                try:

                    page.goto(

                        current_url,

                        timeout=45000,

                        wait_until="domcontentloaded"
                    )

                    html = page.content()

                    page_data = analyze_page(

                        html,

                        current_url
                    )

                    crawled_pages.append(
                        page_data
                    )

                    # =====================
                    # DISCOVER NEW LINKS
                    # =====================

                    for link in page_data[
                        "internal_links"
                    ]:

                        if (

                            link not in visited

                            and

                            link not in pages_to_visit
                        ):

                            pages_to_visit.append(
                                link
                            )

                except Exception:

                    continue

            browser.close()

    except Exception as error:

        return {

            "url": url,

            "title": "",

            "meta_description": "",

            "h1_tags": [],

            "h2_tags": [],

            "paragraphs": [],

            "internal_links": [],

            "word_count": 0,

            "schema_found": False,

            "faq_detected": False,

            "content_depth": "Low",

            "ai_readiness": "Low",

            "technical_findings": [

                f"Crawler failed: {str(error)}"
            ]
        }

    # =====================================
    # SAFETY CHECK
    # =====================================

    if len(crawled_pages) == 0:

        return {

            "url": url,

            "title": "",

            "meta_description": "",

            "h1_tags": [],

            "h2_tags": [],

            "paragraphs": [],

            "internal_links": [],

            "word_count": 0,

            "schema_found": False,

            "faq_detected": False,

            "content_depth": "Low",

            "ai_readiness": "Low",

            "technical_findings": [

                "Crawler could not extract any pages."
            ]
        }

    # =====================================
    # AGGREGATE DATA
    # =====================================

    total_word_count = sum(

        page.get(
            "word_count",
            0
        )

        for page in crawled_pages
    )

    total_h1 = sum(

        len(
            page.get(
                "h1_tags",
                []
            )
        )

        for page in crawled_pages
    )

    total_h2 = sum(

        len(
            page.get(
                "h2_tags",
                []
            )
        )

        for page in crawled_pages
    )

    schema_found = any(

        page.get(
            "schema_found",
            False
        )

        for page in crawled_pages
    )

    faq_detected = any(

        page.get(
            "faq_detected",
            False
        )

        for page in crawled_pages
    )

    all_internal_links = []

    for page in crawled_pages:

        all_internal_links.extend(

            page.get(
                "internal_links",
                []
            )
        )

    # =====================================
    # CONTENT DEPTH
    # =====================================

    content_depth = "Low"

    if total_word_count > 8000:

        content_depth = "High"

    elif total_word_count > 3000:

        content_depth = "Medium"

    # =====================================
    # AI READINESS
    # =====================================

    ai_score = 0

    if schema_found:

        ai_score += 1

    if faq_detected:

        ai_score += 1

    if total_h2 >= 10:

        ai_score += 1

    if total_word_count >= 3000:

        ai_score += 1

    ai_readiness = "Low"

    if ai_score >= 3:

        ai_readiness = "High"

    elif ai_score == 2:

        ai_readiness = "Medium"

    # =====================================
    # PRIMARY PAGE
    # =====================================

    primary_page = crawled_pages[0]

    # =====================================
    # FINAL SITE DATA
    # =====================================

    return {

        "url": url,

        "pages_crawled":
            len(crawled_pages),

        "all_pages":
            crawled_pages,

        "title":
            primary_page.get(
                "title",
                ""
            ),

        "meta_description":
            primary_page.get(
                "meta_description",
                ""
            ),

        "h1_tags":
            primary_page.get(
                "h1_tags",
                []
            ),

        "h2_tags":
            primary_page.get(
                "h2_tags",
                []
            ),

        "paragraphs":
            primary_page.get(
                "paragraphs",
                []
            ),

        "internal_links":
            list(
                set(all_internal_links)
            ),

        "word_count":
            total_word_count,

        "schema_found":
            schema_found,

        "faq_detected":
            faq_detected,

        "content_depth":
            content_depth,

        "ai_readiness":
            ai_readiness,

        "technical_findings": [

            f"{len(crawled_pages)} pages crawled",

            f"{total_word_count} total words analyzed",

            f"{len(all_internal_links)} internal links discovered"
        ]
    }