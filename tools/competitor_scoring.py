from tools.research_context_builder import (
    build_research_context
)

from tools.scoring_engine import (
    calculate_scores
)


# =========================================
# COMPETITOR SCORING
# =========================================

def score_competitors(

    site_data,

    geo_analysis,

    competitor_data
):

    # =====================================
    # BUILD RESEARCH CONTEXT
    # =====================================

    research_context = build_research_context(

        site_data,

        geo_analysis,

        competitor_data

    )

    # =====================================
    # CALCULATE SCORES
    # =====================================

    scores = calculate_scores(

        research_context
    )

    # =====================================
    # RETURN SCORES
    # =====================================

    return {

        "seo_score":
            scores.get(
                "seo_score",
                0
            ),

        "ai_visibility_score":
            scores.get(
                "ai_visibility_score",
                0
            ),

        "geo_score":
            scores.get(
                "geo_score",
                0
            ),

        "competitive_readiness":
            scores.get(
                "competitive_readiness",
                0
            )
    }