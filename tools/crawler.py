import requests

import cloudscraper

from bs4 import BeautifulSoup

from urllib.parse import urljoin

import random

import time


# =========================================
# SELENIUM
# =========================================

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


# =========================================
# USER AGENTS
# =========================================

USER_AGENTS = [

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0 Safari/537.36",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
]


# =========================================
# RANDOM HEADERS
# =========================================

def get_headers():

    return {

        "User-Agent":
            random.choice(
                USER_AGENTS
            ),

        "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",

        "Accept-Language":
            "en-US,en;q=0.5"
    }


# =========================================
# EXTRACTION
# =========================================

def extract_page_data(

    html,

    url
):

    soup = BeautifulSoup(
        html,
        "lxml"
    )

    h1_tags = [

        h.get_text(strip=True)

        for h in soup.find_all("h1")
    ]

    h2_tags = [

        h.get_text(strip=True)

        for h in soup.find_all("h2")
    ]

    paragraphs = [

        p.get_text(strip=True)

        for p in soup.find_all("p")
    ]

    internal_links = []

    for link in soup.find_all(

        "a",

        href=True
    ):

        href = link["href"]

        if href.startswith("/"):

            internal_links.append(

                urljoin(
                    url,
                    href
                )
            )

    full_text = " ".join(
        paragraphs
    )

    word_count = len(
        full_text.split()
    )

    schema_found = (

        "application/ld+json"

        in html
    )

    faq_detected = (

        "faq"

        in html.lower()
    )

    ai_readiness = "Low"

    if word_count > 4000 and len(h2_tags) >= 5:

        ai_readiness = "High"

    elif word_count > 1500:

        ai_readiness = "Medium"

    return {

        "url":
            url,

        "h1_tags":
            h1_tags,

        "h2_tags":
            h2_tags,

        "paragraphs":
            paragraphs,

        "internal_links":
            internal_links,

        "word_count":
            word_count,

        "schema_found":
            schema_found,

        "faq_detected":
            faq_detected,

        "ai_readiness":
            ai_readiness
    }


# =========================================
# VALIDATION
# =========================================

def is_valid_extraction(

    page_data
):

    if not isinstance(
        page_data,
        dict
    ):

        return False

    if page_data.get(
        "word_count",
        0
    ) < 300:

        return False

    return True


# =========================================
# REQUESTS
# =========================================

def fetch_requests(

    url
):

    response = requests.get(

        url,

        headers=get_headers(),

        timeout=30
    )

    return response.text


# =========================================
# CLOUDSCRAPER
# =========================================

def fetch_cloudscraper(

    url
):

    scraper = cloudscraper.create_scraper()

    response = scraper.get(

        url,

        headers=get_headers(),

        timeout=40
    )

    return response.text


# =========================================
# SELENIUM
# =========================================

def fetch_selenium(

    url
):

    options = Options()

    options.add_argument(
        "--headless"
    )

    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    options.add_argument(
        "--no-sandbox"
    )

    options.add_argument(
        "--disable-dev-shm-usage"
    )

    options.add_argument(

        f"user-agent={random.choice(USER_AGENTS)}"
    )

    driver = webdriver.Chrome(

        service=Service(

            ChromeDriverManager().install()
        ),

        options=options
    )

    driver.get(url)

    # =====================================
    # HYDRATION WAIT
    # =====================================

    time.sleep(6)

    html = driver.page_source

    driver.quit()

    return html


# =========================================
# MAIN CRAWLER
# =========================================

def crawl_website(

    url
):

    strategies = [

        ("requests", fetch_requests),

        ("cloudscraper", fetch_cloudscraper),

        ("selenium", fetch_selenium)
    ]

    all_pages = []

    successful_strategy = None

    for strategy_name, strategy in strategies:

        try:

            print(
                f"Trying {strategy_name}"
            )

            html = strategy(
                url
            )

            page_data = extract_page_data(

                html,

                url
            )

            if is_valid_extraction(
                page_data
            ):

                successful_strategy = strategy_name

                all_pages.append(
                    page_data
                )

                print(
                    f"{strategy_name} success"
                )

                break

            else:

                print(
                    f"{strategy_name} extraction invalid"
                )

        except Exception as error:

            print(
                f"{strategy_name} failed: {error}"
            )

            continue

    # =====================================
    # FAILURE
    # =====================================

    if len(all_pages) == 0:

        return {

            "url":
                url,

            "word_count":
                0,

            "schema_found":
                False,

            "faq_detected":
                False,

            "ai_readiness":
                "Low",

            "crawl_confidence":
                "Low",

            "pages_crawled":
                0,

            "h2_tags":
                [],

            "internal_links":
                [],

            "all_pages":
                []
        }

    # =====================================
    # AGGREGATION
    # =====================================

    total_words = sum(

        page.get(
            "word_count",
            0
        )

        for page in all_pages
    )

    schema_found = any(

        page.get(
            "schema_found",
            False
        )

        for page in all_pages
    )

    faq_detected = any(

        page.get(
            "faq_detected",
            False
        )

        for page in all_pages
    )

    h2_tags = []

    internal_links = []

    for page in all_pages:

        h2_tags.extend(

            page.get(
                "h2_tags",
                []
            )
        )

        internal_links.extend(

            page.get(
                "internal_links",
                []
            )
        )

    # =====================================
    # CONFIDENCE
    # =====================================

    if successful_strategy == "selenium":

        crawl_confidence = "High"

    elif successful_strategy == "cloudscraper":

        crawl_confidence = "Medium"

    else:

        crawl_confidence = "Medium"

    return {

        "url":
            url,

        "word_count":
            total_words,

        "schema_found":
            schema_found,

        "faq_detected":
            faq_detected,

        "ai_readiness":

            all_pages[0].get(
                "ai_readiness",
                "Low"
            ),

        "crawl_confidence":
            crawl_confidence,

        "pages_crawled":
            len(all_pages),

        "h2_tags":
            h2_tags,

        "internal_links":
            internal_links,

        "all_pages":
            all_pages
    }