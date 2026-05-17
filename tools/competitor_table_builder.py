# =========================================
# COMPETITOR TABLE BUILDER
# =========================================

def build_competitor_table(

    main_site,

    competitors
):

    rows = []

    # =====================================
    # MAIN SITE
    # =====================================

    rows.append({

        "company":
            "Target Website",

        "seo_score":
            main_site["seo_score"],

        "geo_score":
            main_site["geo_score"],

        "word_count":
            main_site["word_count"],

        "schema":
            "Yes" if main_site[
                "schema_found"
            ] else "No"
    })

    # =====================================
    # COMPETITORS
    # =====================================

    for competitor in competitors:

        rows.append({

            "company":
                competitor["url"],

            "seo_score":
                competitor["seo_score"],

            "geo_score":
                competitor["geo_score"],

            "word_count":
                competitor["word_count"],

            "schema":
                "Yes" if competitor[
                    "schema_found"
                ] else "No"
        })

    # =====================================
    # HTML TABLE
    # =====================================

    html = """

    <table class='comparison-table'>

        <tr>

            <th>Organization</th>

            <th>SEO Score</th>

            <th>AI Visibility</th>

            <th>Content Depth</th>

            <th>Schema</th>

        </tr>

    """

    for row in rows:

        html += f"""

        <tr>

            <td>{row['company']}</td>

            <td>{row['seo_score']}</td>

            <td>{row['geo_score']}</td>

            <td>{row['word_count']}</td>

            <td>{row['schema']}</td>

        </tr>

        """

    html += "</table>"

    return html