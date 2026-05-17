# =========================================
# EXECUTIVE SCORING ENGINE
# =========================================

def calculate_scores(research_context):

    # =====================================
    # BASE SCORES
    # =====================================

    seo_score = research_context.get(
        "seo_score",
        50
    )

    geo_score = research_context.get(
        "geo_score",
        50
    )

    word_count = research_context.get(
        "word_count",
        0
    )

    schema_found = research_context.get(
        "schema_found",
        False
    )

    competitor_seo = research_context.get(
        "avg_competitor_seo",
        50
    )

    competitor_geo = research_context.get(
        "avg_competitor_geo",
        50
    )

    # =====================================
    # AI VISIBILITY SCORE
    # =====================================

    ai_visibility_score = geo_score

    if schema_found:

        ai_visibility_score += 5

    if word_count > 1500:

        ai_visibility_score += 5

    ai_visibility_score = min(
        ai_visibility_score,
        100
    )

    # =====================================
    # COMPETITIVE READINESS
    # =====================================

    competitive_readiness = round(

        (
            seo_score
            +
            geo_score
            +
            competitor_seo
            +
            competitor_geo
        ) / 4,

        2
    )

    # =====================================
    # FINAL OUTPUT
    # =====================================

    return {

        "seo_score":
            round(seo_score, 2),

        "ai_visibility_score":
            round(ai_visibility_score, 2),

        "competitive_readiness":
            round(
                competitive_readiness,
                2
            )
    }