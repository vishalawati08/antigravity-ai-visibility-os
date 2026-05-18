# =========================================
# LINK EXTRACTION
# =========================================

def extract_links(

    soup,

    base_url
):

    links = soup.find_all(
        "a",
        href=True
    )

    internal_links = 0

    external_links = 0

    for link in links:

        href = link["href"]

        if base_url in href:

            internal_links += 1

        elif href.startswith("http"):

            external_links += 1

    return {

        "internal_links":
            internal_links,

        "external_links":
            external_links
    }