# =========================================
# SCORING ENGINE
# =========================================

def calculate_scores(

    research_context
):

    # =====================================
    # BASE SCORES
    # =====================================

    seo_score = 40

    ai_visibility_score = 40

    geo_score = 40

    competitive_readiness = 40

    # =====================================
    # CONTENT DEPTH
    # =====================================

    word_count = research_context.get(
        "word_count",
        0
    )

    if word_count > 2500:

        seo_score += 15

        ai_visibility_score += 15

        geo_score += 10

    elif word_count > 1200:

        seo_score += 10

        ai_visibility_score += 8

        geo_score += 6

    elif word_count > 800:

        seo_score += 5

    # =====================================
    # TITLE TAG
    # =====================================

    if research_context.get("title_present"):

        seo_score += 8

    # =====================================
    # META DESCRIPTION
    # =====================================

    if research_context.get(
        "meta_description_present"
    ):

        seo_score += 5

    # =====================================
    # H1 STRUCTURE
    # =====================================

    h1_count = research_context.get(
        "h1_count",
        0
    )

    if h1_count == 1:

        seo_score += 8

        geo_score += 4

    elif h1_count > 1:

        seo_score -= 4

    # =====================================
    # H2 COVERAGE
    # =====================================

    h2_count = research_context.get(
        "h2_count",
        0
    )

    if h2_count >= 5:

        seo_score += 8

        ai_visibility_score += 10

        geo_score += 10

    elif h2_count >= 2:

        seo_score += 4

    # =====================================
    # SCHEMA
    # =====================================

    if research_context.get(
        "schema_found"
    ):

        seo_score += 10

        ai_visibility_score += 15

        geo_score += 12

    # =====================================
    # FAQ DETECTION
    # =====================================

    if research_context.get(
        "faq_detected"
    ):

        ai_visibility_score += 15

        geo_score += 18

    # =====================================
    # INTERNAL LINKING
    # =====================================

    internal_links = research_context.get(
        "internal_link_count",
        0
    )

    if internal_links >= 15:

        seo_score += 10

    elif internal_links >= 5:

        seo_score += 5

    # =====================================
    # IMAGE ALT COVERAGE
    # =====================================

    missing_alt = research_context.get(
        "images_missing_alt",
        0
    )

    if missing_alt == 0:

        seo_score += 5

    elif missing_alt > 10:

        seo_score -= 5

    # =====================================
    # CONTENT DEPTH SCORE
    # =====================================

    content_depth = research_context.get(
        "content_depth",
        "Low"
    )

    if content_depth == "High":

        ai_visibility_score += 12

        competitive_readiness += 12

    elif content_depth == "Medium":

        ai_visibility_score += 6

        competitive_readiness += 6

    # =====================================
    # AI READINESS
    # =====================================

    ai_readiness = research_context.get(
        "ai_readiness",
        "Low"
    )

    if ai_readiness == "High":

        ai_visibility_score += 20

        geo_score += 15

        competitive_readiness += 15

    elif ai_readiness == "Medium":

        ai_visibility_score += 10

        geo_score += 8

    # =====================================
    # COMPETITOR AVERAGE
    # =====================================

    competitor_average = research_context.get(
        "competitor_average",
        50
    )

    if competitor_average > 70:

        competitive_readiness += 10

    elif competitor_average > 60:

        competitive_readiness += 5

    # =====================================
    # SCORE NORMALIZATION
    # =====================================

    seo_score = min(100, max(0, seo_score))

    ai_visibility_score = min(
        100,
        max(0, ai_visibility_score)
    )

    geo_score = min(
        100,
        max(0, geo_score)
    )

    competitive_readiness = min(
        100,
        max(0, competitive_readiness)
    )

    # =====================================
    # FINAL SCORES
    # =====================================

    return {

        "seo_score":
            seo_score,

        "ai_visibility_score":
            ai_visibility_score,

        "geo_score":
            geo_score,

        "competitive_readiness":
            competitive_readiness
    }