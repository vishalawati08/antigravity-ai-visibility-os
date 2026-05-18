# =========================================
# RESEARCH CONTEXT BUILDER
# =========================================

def build_research_context(

    site_data,

    competitor_data
):

    # =====================================
    # COMPETITOR AVERAGE
    # =====================================

    competitor_average = 0

    if competitor_data:

        competitor_average = (

            sum(

                competitor.get(
                    "seo_score",
                    0
                )

                for competitor in competitor_data

                if isinstance(
                    competitor,
                    dict
                )

            )

            / len(competitor_data)
        )

    # =====================================
    # TITLE
    # =====================================

    title_present = bool(

        site_data.get(
            "title"
        )
    )

    # =====================================
    # META DESCRIPTION
    # =====================================

    meta_description_present = bool(

        site_data.get(
            "meta_description"
        )
    )

    # =====================================
    # H1 COUNT
    # =====================================

    h1_count = len(

        site_data.get(
            "h1_tags",
            []
        )
    )

    # =====================================
    # H2 COUNT
    # =====================================

    h2_count = len(

        site_data.get(
            "h2_tags",
            []
        )
    )

    # =====================================
    # INTERNAL LINKS
    # =====================================

    internal_link_count = len(

        site_data.get(
            "internal_links",
            []
        )
    )

    # =====================================
    # FINAL CONTEXT
    # =====================================

    return {

        # BASIC

        "url":
            site_data.get(
                "url",
                ""
            ),

        "title":
            site_data.get(
                "title",
                ""
            ),

        "meta_description":
            site_data.get(
                "meta_description",
                ""
            ),

        # PRESENCE FLAGS

        "title_present":
            title_present,

        "meta_description_present":
            meta_description_present,

        # CONTENT

        "word_count":
            site_data.get(
                "word_count",
                0
            ),

        "content_depth":
            site_data.get(
                "content_depth",
                "Low"
            ),

        # STRUCTURE

        "h1_count":
            h1_count,

        "h2_count":
            h2_count,

        "schema_found":
            site_data.get(
                "schema_found",
                False
            ),

        "faq_detected":
            site_data.get(
                "faq_detected",
                False
            ),

        # LINKS

        "internal_link_count":
            internal_link_count,

        # IMAGES

        "images_missing_alt":
            site_data.get(
                "images_missing_alt",
                0
            ),

        # AI READINESS

        "ai_readiness":
            site_data.get(
                "ai_readiness",
                "Low"
            ),

        # COMPETITION

        "competitor_average":
            competitor_average,

        "competitor_count":
            len(competitor_data),

        # TECHNICAL

        "canonical":
            site_data.get(
                "canonical",
                ""
            ),

        "robots_meta":
            site_data.get(
                "robots_meta",
                ""
            ),

        # RAW FINDINGS

        "technical_findings":
            site_data.get(
                "technical_findings",
                []
            )
    }