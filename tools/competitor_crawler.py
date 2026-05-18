from tools.crawler import crawl_website


# =========================================
# COMPETITOR CRAWLER
# =========================================

def crawl_competitors(

    competitors
):

    crawled_competitors = []

    for competitor in competitors:

        try:

            domain = competitor.get(
                "domain",
                ""
            )

            if not domain.startswith("http"):

                url = f"https://{domain}"

            else:

                url = domain

            site_data = crawl_website(
                url
            )

            crawled_competitors.append({

                "name":
                    competitor.get(
                        "name",
                        "Unknown"
                    ),

                "domain":
                    domain,

                "site_data":
                    site_data
            })

        except Exception as error:

            crawled_competitors.append({

                "name":
                    competitor.get(
                        "name",
                        "Unknown"
                    ),

                "domain":
                    competitor.get(
                        "domain",
                        ""
                    ),

                "crawl_error":
                    str(error)
            })

    return crawled_competitors