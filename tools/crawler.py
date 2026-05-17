import requests

from bs4 import BeautifulSoup


# =========================================
# SIMPLE WEBSITE CRAWLER
# =========================================

def crawl_website(url):

    try:

        headers = {

            "User-Agent": (

                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64)"
            )
        }

        response = requests.get(

            url,

            headers=headers,

            timeout=20
        )

        html = response.text

        soup = BeautifulSoup(

            html,

            "html.parser"
        )

        # =====================================
        # TITLE
        # =====================================

        title = "No title found"

        if soup.title:

            title = soup.title.text.strip()

        # =====================================
        # META DESCRIPTION
        # =====================================

        meta_description = ""

        meta_tag = soup.find(

            "meta",

            attrs={
                "name": "description"
            }
        )

        if meta_tag:

            meta_description = (
                meta_tag.get("content", "")
            )

        # =====================================
        # HEADINGS
        # =====================================

        h1_tags = soup.find_all("h1")

        h2_tags = soup.find_all("h2")

        # =====================================
        # IMAGES
        # =====================================

        images = soup.find_all("img")

        missing_alt = 0

        for image in images:

            if not image.get("alt"):

                missing_alt += 1

        # =====================================
        # CONTENT
        # =====================================

        text_content = soup.get_text()

        word_count = len(

            text_content.split()
        )

        # =====================================
        # SCHEMA
        # =====================================

        schema_found = bool(

            soup.find_all(

                "script",

                attrs={
                    "type":
                    "application/ld+json"
                }
            )
        )

        # =====================================
        # BASIC SCORES
        # =====================================

        seo_score = 80

        geo_score = 45

        if schema_found:

            geo_score += 10

        if word_count > 1500:

            seo_score += 5

        # =====================================
        # OUTPUT
        # =====================================

        return {

            "url": url,

            "title": title,

            "meta_description":
                meta_description,

            "h1_count":
                len(h1_tags),

            "h2_count":
                len(h2_tags),

            "word_count":
                word_count,

            "missing_alt":
                missing_alt,

            "schema_found":
                schema_found,

            "seo_score":
                seo_score,

            "geo_score":
                geo_score,

            "serp_insights": [],

            "technical_seo": {

                "title_present":
                    bool(title),

                "meta_description_present":
                    bool(meta_description),

                "schema_found":
                    schema_found,

                "missing_alt":
                    missing_alt
            }
        }

    except Exception as error:

        print(

            f"CRAWLER ERROR: {error}"
        )

        return {

            "url": url,

            "title":
                "Unknown Website",

            "meta_description":
                "Unable to extract metadata.",

            "h1_count": 0,

            "h2_count": 0,

            "word_count": 0,

            "missing_alt": 0,

            "schema_found": False,

            "seo_score": 50,

            "geo_score": 40,

            "serp_insights": [],

            "technical_seo": {

                "title_present": False,

                "meta_description_present": False,

                "schema_found": False,

                "missing_alt": 0
            }
        }