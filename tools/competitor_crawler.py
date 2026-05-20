from tools.crawler import (
    crawl_website
)

from tools.research_context_builder import (
    build_research_context
)

from tools.scoring_engine import (
    calculate_scores
)

from tools.geo_aeo_engine import (
    analyze_geo_aeo
)


# =========================================
# DEFAULT INDUSTRY COMPETITORS
# =========================================

DEFAULT_COMPETITORS = [

    {
        "name":
            "Samtec",

        "url":
            "https://www.samtec.com"
    },

    {
        "name":
            "TE Connectivity",

        "url":
            "https://www.te.com"
    },

    {
        "name":
            "Amphenol",

        "url":
            "https://www.amphenol.com"
    }
]


# =========================================
# COMPETITOR CRAWLER
# =========================================

def crawl_competitors(

    target_url
):

    competitor_results = []

    # =====================================
    # LOOP COMPETITORS
    # =====================================

    for competitor in DEFAULT_COMPETITORS:

        try:

            competitor_name = competitor.get(
                "name",
                "Unknown"
            )

            competitor_url = competitor.get(
                "url",
                ""
            )

            # ==============================
            # CRAWL
            # ==============================

            crawl_data = crawl_website(
                competitor_url
            )

            # ==============================
            # GEO ANALYSIS
            # ==============================

            geo_analysis = analyze_geo_aeo(
                crawl_data
            )

            # ==============================
            # RESEARCH CONTEXT
            # ==============================

            research_context = build_research_context(

                crawl_data,

                geo_analysis,

                []
            )

            # ==============================
            # SCORES
            # ==============================

            scores = calculate_scores(
                research_context
            )

            # ==============================
            # FINAL RESULT
            # ==============================

            competitor_results.append({

                "name":
                    competitor_name,

                "url":
                    competitor_url,

                "seo_score":
                    scores.get(
                        "seo_score",
                        0
                    ),

                "ai_visibility":
                    scores.get(
                        "ai_visibility_score",
                        0
                    ),

                "geo_score":
                    scores.get(
                        "geo_score",
                        0
                    ),

                "crawl_confidence":
                    crawl_data.get(
                        "crawl_confidence",
                        "Low"
                    ),

                "semantic_maturity":
                    research_context.get(
                        "semantic_maturity",
                        "Low"
                    ),

                "content_depth":
                    research_context.get(
                        "content_depth",
                        "Low"
                    ),

                "word_count":
                    research_context.get(
                        "word_count",
                        0
                    ),

                "pages_crawled":
                    research_context.get(
                        "pages_crawled",
                        0
                    )
            })

        except Exception as error:

            competitor_results.append({

                "name":
                    competitor.get(
                        "name",
                        "Unknown"
                    ),

                "url":
                    competitor.get(
                        "url",
                        ""
                    ),

                "seo_score":
                    50,

                "ai_visibility":
                    50,

                "geo_score":
                    50,

                "crawl_confidence":
                    "Low",

                "semantic_maturity":
                    "Low",

                "content_depth":
                    "Low",

                "word_count":
                    0,

                "pages_crawled":
                    0,

                "error":
                    str(error)
            })

    return competitor_results