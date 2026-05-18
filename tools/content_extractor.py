# =========================================
# CONTENT EXTRACTION
# =========================================

def extract_content(soup):

    # TITLE
    title = ""

    if soup.title:

        title = soup.title.text.strip()

    # META DESCRIPTION
    meta_description = ""

    meta = soup.find(

        "meta",

        attrs={
            "name": "description"
        }
    )

    if meta:

        meta_description = meta.get(
            "content",
            ""
        )

    # HEADINGS
    h1_tags = [

        h.get_text(strip=True)

        for h in soup.find_all("h1")
    ]

    h2_tags = [

        h.get_text(strip=True)

        for h in soup.find_all("h2")
    ]

    h3_tags = [

        h.get_text(strip=True)

        for h in soup.find_all("h3")
    ]

    # PARAGRAPHS
    paragraphs = soup.find_all("p")

    paragraph_count = len(
        paragraphs
    )

    # WORD COUNT
    text = soup.get_text(
        separator=" ",
        strip=True
    )

    words = text.split()

    word_count = len(words)

    return {

        "title": title,

        "title_length":
            len(title),

        "meta_description":
            meta_description,

        "meta_description_length":
            len(meta_description),

        "h1_tags":
            h1_tags,

        "h2_tags":
            h2_tags,

        "h3_tags":
            h3_tags,

        "h1_count":
            len(h1_tags),

        "h2_count":
            len(h2_tags),

        "h3_count":
            len(h3_tags),

        "paragraph_count":
            paragraph_count,

        "word_count":
            word_count
    }