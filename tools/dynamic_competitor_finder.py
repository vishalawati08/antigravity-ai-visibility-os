import requests

from bs4 import BeautifulSoup

from urllib.parse import urlparse


# =========================================
# DOMAIN CLEANER
# =========================================

def clean_domain(url):

    parsed = urlparse(url)

    domain = parsed.netloc.replace(
        "www.",
        ""
    )

    return domain


# =========================================
# GOOGLE SEARCH
# =========================================

def search_google(query):

    headers = {

        "User-Agent":
            (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120 Safari/537.36"
            )
    }

    url = (
        f"https://www.google.com/search?q={query}"
    )

    response = requests.get(

        url,

        headers=headers,

        timeout=15
    )

    soup = BeautifulSoup(

        response.text,

        "html.parser"
    )

    results = []

    for link in soup.select("a"):

        href = link.get("href")

        if href and "/url?q=" in href:

            try:

                real_url = (
                    href.split("/url?q=")[1]
                    .split("&")[0]
                )

                if real_url.startswith("http"):

                    results.append(real_url)

            except:

                pass

    return results


# =========================================
# DYNAMIC COMPETITOR FINDER
# =========================================

def discover_competitors(url):

    domain = clean_domain(url)

    query = domain.replace(".com", "")

    search_results = search_google(query)

    competitors = []

    for result in search_results:

        clean = clean_domain(result)

        # Ignore self
        if domain in clean:

            continue

        # Ignore major platforms
        if any(x in clean for x in [

            "google",

            "youtube",

            "linkedin",

            "facebook",

            "instagram",

            "twitter",

            "wikipedia"
        ]):

            continue

        competitor_url = (
            f"https://{clean}"
        )

        if competitor_url not in competitors:

            competitors.append(
                competitor_url
            )

        if len(competitors) >= 5:

            break

    return competitors