# =========================================
# RESEARCH CONTEXT BUILDER
# =========================================

def build_research_context(

    site_data,

    competitor_data
):

    # =====================================
    # SAFE SITE DATA
    # =====================================

    title = site_data.get(
        "title",
        "Unknown Website"
    )

    meta_description = site_data.get(
        "meta_description",
        "No meta description available."
    )

    seo_score = site_data.get(
        "seo_score",
        50
    )

    geo_score = site_data.get(
        "geo_score",
        50
    )

    word_count = site_data.get(
        "word_count",
        0
    )

    schema_found = site_data.get(
        "schema_found",
        False
    )

    issues = site_data.get(
        "issues",
        []
    )

    # =====================================
    # COMPETITOR AVERAGES
    # =====================================

    if competitor_data:

        avg_competitor_seo = round(

            sum(

                competitor.get(
                    "seo_score",
                    50
                )

                for competitor in competitor_data

            ) / len(competitor_data),

            2
        )

        avg_competitor_geo = round(

            sum(

                competitor.get(
                    "geo_score",
                    50
                )

                for competitor in competitor_data

            ) / len(competitor_data),

            2
        )

    else:

        avg_competitor_seo = 50

        avg_competitor_geo = 50

    # =====================================
    # BUILD CONTEXT
    # =====================================

    context = {

        "website_title":
            title,

        "meta_description":
            meta_description,

        "seo_score":
            seo_score,

        "geo_score":
            geo_score,

        "word_count":
            word_count,

        "schema_found":
            schema_found,

        "issues":
            issues,

        "competitor_count":
            len(competitor_data),

        "avg_competitor_seo":
            avg_competitor_seo,

        "avg_competitor_geo":
            avg_competitor_geo
    }

    return context