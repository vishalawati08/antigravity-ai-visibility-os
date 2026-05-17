from googlesearch import search


def analyze_serp(keyword):

    results = []

    try:

        for url in search(
            keyword,
            num_results=10
        ):

            results.append(url)

    except Exception as e:

        return {
            "keyword": keyword,
            "results": [],
            "summary": f"SERP fetch failed: {e}"
        }

    # =========================
    # STRATEGIC ANALYSIS
    # =========================

    distributors = [
        "digikey",
        "mouser",
        "arrow",
        "tti",
        "rs-online",
        "farnell"
    ]

    distributor_count = 0

    competitor_domains = []

    for url in results:

        for distributor in distributors:

            if distributor in url.lower():

                distributor_count += 1

        competitor_domains.append(url)

    # =========================
    # STRATEGIC SUMMARY
    # =========================

    insights = []

    if distributor_count >= 3:

        insights.append(
            "Distributors dominate the SERP, indicating weak manufacturer-level search ownership."
        )

    elif distributor_count > 0:

        insights.append(
            "Distributor presence detected in search rankings."
        )

    else:

        insights.append(
            "SERP currently appears manufacturer-driven with limited distributor dominance."
        )

    return {
        "keyword": keyword,
        "results": results,
        "insights": insights
    }