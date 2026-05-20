# =========================================
# CALIBRATED ENTERPRISE SCORING ENGINE
# =========================================

def calculate_scores(

    research_context
):

    # =====================================
    # SAFE DEFAULTS
    # =====================================

    if not isinstance(
        research_context,
        dict
    ):

        research_context = {}

    # =====================================
    # EXTRACTION
    # =====================================

    word_count = research_context.get(
        "word_count",
        0
    )

    schema_found = research_context.get(
        "schema_found",
        False
    )

    faq_detected = research_context.get(
        "faq_detected",
        False
    )

    semantic_richness = research_context.get(
        "semantic_richness",
        0
    )

    total_h2 = research_context.get(
        "total_h2",
        0
    )

    internal_links = research_context.get(
        "internal_links",
        0
    )

    crawl_confidence = research_context.get(
        "crawl_confidence",
        "Low"
    )

    pages_crawled = research_context.get(
        "pages_crawled",
        0
    )

    semantic_maturity = research_context.get(
        "semantic_maturity",
        "Low"
    )

    geo_maturity = research_context.get(
        "geo_maturity",
        "Low"
    )

    competitor_average = research_context.get(
        "competitor_average",
        60
    )

    # =====================================
    # INITIAL SCORES
    # =====================================

    seo_score = 35

    ai_visibility_score = 30

    geo_score = 30

    # =====================================
    # CONTENT DEPTH
    # ENTERPRISE-CALIBRATED
    # =====================================

    if word_count >= 8000:

        seo_score += 22

        ai_visibility_score += 18

    elif word_count >= 3500:

        seo_score += 18

        ai_visibility_score += 15

    elif word_count >= 1500:

        seo_score += 14

        ai_visibility_score += 12

    elif word_count >= 700:

        seo_score += 10

        ai_visibility_score += 8

    # =====================================
    # SEMANTIC STRUCTURE
    # =====================================

    if total_h2 >= 15:

        seo_score += 18

        ai_visibility_score += 15

        geo_score += 15

    elif total_h2 >= 8:

        seo_score += 14

        ai_visibility_score += 12

        geo_score += 12

    elif total_h2 >= 4:

        seo_score += 10

        ai_visibility_score += 8

        geo_score += 8

    # =====================================
    # INTERNAL LINKING
    # =====================================

    if internal_links >= 400:

        seo_score += 10

    elif internal_links >= 100:

        seo_score += 7

    elif internal_links >= 30:

        seo_score += 5

    # =====================================
    # SCHEMA
    # =====================================

    if schema_found:

        seo_score += 8

        ai_visibility_score += 14

        geo_score += 16

    # =====================================
    # FAQ DETECTION
    # =====================================

    if faq_detected:

        ai_visibility_score += 12

        geo_score += 14

    # =====================================
    # SEMANTIC MATURITY
    # =====================================

    if semantic_maturity == "High":

        seo_score += 12

        ai_visibility_score += 10

    elif semantic_maturity == "Medium":

        seo_score += 7

        ai_visibility_score += 6

    # =====================================
    # GEO MATURITY
    # =====================================

    if geo_maturity == "High":

        geo_score += 14

    elif geo_maturity == "Medium":

        geo_score += 8

    # =====================================
    # CRAWL CONFIDENCE
    # CALIBRATED MODERATION
    # =====================================

    if crawl_confidence == "High":

        seo_score += 5

        ai_visibility_score += 5

        geo_score += 5

    elif crawl_confidence == "Medium":

        seo_score += 2

        ai_visibility_score += 2

        geo_score += 2

    else:

        seo_score -= 5

        ai_visibility_score -= 5

        geo_score -= 5

    # =====================================
    # PAGE COVERAGE
    # =====================================

    if pages_crawled >= 5:

        seo_score += 6

        ai_visibility_score += 4

    elif pages_crawled >= 2:

        seo_score += 3

        ai_visibility_score += 2

    # =====================================
    # NORMALIZATION
    # =====================================

    seo_score = max(
        20,
        min(
            round(seo_score),
            95
        )
    )

    ai_visibility_score = max(
        20,
        min(
            round(ai_visibility_score),
            95
        )
    )

    geo_score = max(
        20,
        min(
            round(geo_score),
            95
        )
    )

    # =====================================
    # COMPETITIVE READINESS
    # =====================================

    competitive_readiness = round(

        (

            seo_score

            +

            ai_visibility_score

            +

            geo_score
        )

        / 3
    )

    # =====================================
    # INDUSTRY RELATIVE ADJUSTMENT
    # =====================================

    if competitive_readiness > competitor_average:

        competitive_readiness += 4

    elif competitive_readiness < competitor_average:

        competitive_readiness -= 4

    competitive_readiness = max(

        20,

        min(
            competitive_readiness,
            95
        )
    )

    # =====================================
    # FINAL OUTPUT
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