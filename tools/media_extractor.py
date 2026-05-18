# =========================================
# MEDIA EXTRACTION
# =========================================

def extract_media(soup):

    images = soup.find_all("img")

    image_count = len(images)

    missing_alt = 0

    alt_coverage = 0

    for image in images:

        alt = image.get("alt")

        if not alt:

            missing_alt += 1

    if image_count > 0:

        alt_coverage = round(

            (
                (
                    image_count -
                    missing_alt
                )

                / image_count
            ) * 100,

            2
        )

    return {

        "image_count":
            image_count,

        "missing_alt":
            missing_alt,

        "alt_coverage":
            alt_coverage
    }