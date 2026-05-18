from tools.research_context_builder import (
    build_research_context
)

from tools.scoring_engine import (
    calculate_scores
)


# =========================================
# COMPETITOR SCORING ENGINE
# =========================================

def score_competitors(

    crawled_competitors
):

    scored = []

    for competitor in crawled_competitors:

        site_data = competitor.get(
            "site_data",
            {}
        )

        if not site_data:

            continue

        research_context = build_research_context(

            site_data,

            []
        )

        scores = calculate_scores(

            research_context
        )

        scored.append({

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

            "content_depth":
                site_data.get(
                    "content_depth",
                    "Low"
                ),

            "word_count":
                site_data.get(
                    "word_count",
                    0
                )
        })

    return scored