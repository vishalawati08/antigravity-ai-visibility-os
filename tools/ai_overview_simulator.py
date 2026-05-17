# =========================================
# AI OVERVIEW SIMULATOR
# =========================================

def simulate_ai_overview(site_data):

    # =====================================
    # SAFE DATA EXTRACTION
    # =====================================

    title = site_data.get(
        "title",
        "Unknown Website"
    )

    meta_description = site_data.get(
        "meta_description",
        (
            "No meta description available "
            "for AI overview generation."
        )
    )

    seo_score = site_data.get(
        "seo_score",
        50
    )

    geo_score = site_data.get(
        "geo_score",
        50
    )

    schema_found = site_data.get(
        "schema_found",
        False
    )

    word_count = site_data.get(
        "word_count",
        0
    )

    # =====================================
    # AI OVERVIEW RESPONSE
    # =====================================

    ai_overview = f"""

    <div>

    <h3>
    AI Search Overview Simulation
    </h3>

    <p>

    <b>{title}</b> demonstrates an
    evolving digital presence with
    moderate AI-search readiness.

    </p>

    <p>

    The website currently has:

    <ul>

        <li>
        SEO Score: {seo_score}
        </li>

        <li>
        AI Visibility Score: {geo_score}
        </li>

        <li>
        Schema Markup:
        {"Detected" if schema_found else "Not Detected"}
        </li>

        <li>
        Content Depth:
        {word_count} words
        </li>

    </ul>

    </p>

    <p>

    AI systems may summarize the
    organization as follows:

    </p>

    <blockquote>

    {meta_description}

    </blockquote>

    <p>

    Improvements in semantic structure,
    GEO optimization and AI citation
    readiness could significantly
    improve discoverability across
    generative search platforms.

    </p>

    </div>

    """

    return ai_overview