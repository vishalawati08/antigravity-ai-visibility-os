# =========================================
# RESEARCH CONTEXT BUILDER
# =========================================

def build_research_context(

    crawl_data,

    geo_analysis,

    competitor_data
):

    # =====================================
    # SAFE DEFAULTS
    # =====================================

    if not isinstance(
        crawl_data,
        dict
    ):

        crawl_data = {}

    if not isinstance(
        competitor_data,
        list
    ):

        competitor_data = []

    # =====================================
    # BASIC EXTRACTION
    # =====================================

    word_count = crawl_data.get(
        "word_count",
        0
    )

    schema_found = crawl_data.get(
        "schema_found",
        False
    )

    faq_detected = crawl_data.get(
        "faq_detected",
        False
    )

    ai_readiness = crawl_data.get(
        "ai_readiness",
        "Low"
    )

    crawl_confidence = crawl_data.get(
        "crawl_confidence",
        "Low"
    )

    pages_crawled = crawl_data.get(
        "pages_crawled",
        1
    )

    # =====================================
    # PAGE AGGREGATION
    # =====================================

    all_pages = crawl_data.get(
        "all_pages",
        []
    )

    total_h1 = 0

    total_h2 = 0

    total_paragraphs = 0

    total_internal_links = 0

    semantic_richness = 0

    for page in all_pages:

        if not isinstance(
            page,
            dict
        ):

            continue

        h1_tags = page.get(
            "h1_tags",
            []
        )

        h2_tags = page.get(
            "h2_tags",
            []
        )

        paragraphs = page.get(
            "paragraphs",
            []
        )

        internal_links = page.get(
            "internal_links",
            []
        )

        total_h1 += len(
            h1_tags
        )

        total_h2 += len(
            h2_tags
        )

        total_paragraphs += len(
            paragraphs
        )

        total_internal_links += len(
            internal_links
        )

        # =================================
        # SEMANTIC RICHNESS
        # =================================

        page_semantics = (

            len(h2_tags) * 2

            +

            len(paragraphs) * 0.5
        )

        semantic_richness += page_semantics

    # =====================================
    # NORMALIZATION
    # =====================================

    if pages_crawled > 0:

        average_h2 = round(

            total_h2 / pages_crawled
        )

    else:

        average_h2 = total_h2

    # =====================================
    # CONTENT DEPTH
    # =====================================

    content_depth = "Low"

    if word_count > 12000:

        content_depth = "High"

    elif word_count > 5000:

        content_depth = "Medium"

    # =====================================
    # SEMANTIC MATURITY
    # =====================================

    semantic_maturity = "Low"

    if semantic_richness > 120:

        semantic_maturity = "High"

    elif semantic_richness > 50:

        semantic_maturity = "Medium"

    # =====================================
    # GEO MATURITY
    # =====================================

    geo_maturity = "Low"

    if isinstance(
        geo_analysis,
        list
    ):

        geo_positive = 0

        for item in geo_analysis:

            if not isinstance(
                item,
                dict
            ):

                continue

            status = item.get(
                "status",
                ""
            ).lower()

            if status in [

                "good",

                "strong",

                "optimized"
            ]:

                geo_positive += 1

        if geo_positive >= 5:

            geo_maturity = "High"

        elif geo_positive >= 2:

            geo_maturity = "Medium"

    # =====================================
    # COMPETITOR AVERAGE
    # =====================================

    competitor_scores = []

    for competitor in competitor_data:

        if not isinstance(
            competitor,
            dict
        ):

            continue

        competitor_scores.append(

            competitor.get(
                "seo_score",
                60
            )
        )

    if len(competitor_scores) > 0:

        competitor_average = round(

            sum(competitor_scores)

            /

            len(competitor_scores)
        )

    else:

        competitor_average = 60

    # =====================================
    # FINAL CONTEXT
    # =====================================

    return {

        "word_count":
            word_count,

        "schema_found":
            schema_found,

        "faq_detected":
            faq_detected,

        "ai_readiness":
            ai_readiness,

        "crawl_confidence":
            crawl_confidence,

        "pages_crawled":
            pages_crawled,

        "total_h1":
            total_h1,

        "total_h2":
            total_h2,

        "average_h2":
            average_h2,

        "total_paragraphs":
            total_paragraphs,

        "internal_links":
            total_internal_links,

        "semantic_richness":
            semantic_richness,

        "semantic_maturity":
            semantic_maturity,

        "content_depth":
            content_depth,

        "geo_maturity":
            geo_maturity,

        "competitor_average":
            competitor_average
    }