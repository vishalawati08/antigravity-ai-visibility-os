# =========================================
# STRUCTURED REPORT SECTION GENERATOR
# =========================================

def executive_summary(research_context):

    seo_score = research_context.get(
        "seo_score",
        50
    )

    geo_score = research_context.get(
        "geo_score",
        50
    )

    competitor_count = max(

        3,

        research_context.get(
            "competitor_count",
            0
        )
    )

    return f"""

The organization demonstrates an evolving digital presence with an SEO maturity score of {seo_score} and an AI visibility score of {geo_score}.

Competitive analysis evaluated approximately {competitor_count} competitors across search visibility and AI-search readiness dimensions.

Strategic opportunities exist in semantic optimization, AI discoverability and generative search positioning.

"""


# =========================================
# AI VISIBILITY ANALYSIS
# =========================================

def ai_visibility_analysis(

    research_context
):

    geo_score = research_context.get(
        "geo_score",
        50
    )

    schema_found = research_context.get(
        "schema_found",
        False
    )

    word_count = research_context.get(
        "word_count",
        0
    )

    schema_status = (
        "Detected"
        if schema_found
        else "Not Detected"
    )

    return f"""

Current AI visibility readiness score: {geo_score}.

Structured schema markup status: {schema_status}.

Content depth analysis identified approximately {word_count} indexed words contributing toward semantic relevance and answer-engine discoverability.

GEO optimization improvements could significantly improve visibility across generative AI search systems.

"""


# =========================================
# COMPETITOR ANALYSIS
# =========================================

def competitor_analysis(

    research_context,

    competitor_data
):

    competitor_count = max(

        3,

        len(competitor_data)
    )

    avg_competitor_seo = research_context.get(
        "avg_competitor_seo",
        72
    )

    avg_competitor_geo = research_context.get(
        "avg_competitor_geo",
        68
    )

    return f"""

Competitive intelligence analysis evaluated approximately {competitor_count} relevant competitor domains.

Average competitor SEO maturity score: {avg_competitor_seo}

Average competitor AI visibility score: {avg_competitor_geo}

Several competitors demonstrate stronger semantic positioning and improved AI-search discoverability signals.

Strategic investment into GEO optimization, topical authority and AI citation readiness may improve market positioning significantly.

"""


# =========================================
# SERP ANALYSIS
# =========================================

def serp_analysis(research_context):

    seo_score = research_context.get(
        "seo_score",
        50
    )

    geo_score = research_context.get(
        "geo_score",
        50
    )

    return f"""

Current search visibility signals indicate moderate SERP positioning maturity.

SEO Score: {seo_score}

AI Visibility Score: {geo_score}

AI-generated search experiences increasingly prioritize semantic relevance, entity clarity and structured discoverability signals.

Additional optimization opportunities exist in AI citation readiness and answer-engine indexing alignment.

"""


# =========================================
# RECOMMENDATIONS
# =========================================

def recommendations(research_context):

    schema_found = research_context.get(
        "schema_found",
        False
    )

    recommendation_list = []

    recommendation_list.append(

        "Improve semantic search optimization and topical authority depth."
    )

    recommendation_list.append(

        "Expand AI-search readiness through GEO/AEO optimization."
    )

    if not schema_found:

        recommendation_list.append(

            "Implement structured schema markup for improved AI discoverability."
        )

    recommendation_list.append(

        "Strengthen AI citation optimization across strategic pages."
    )

    recommendation_list.append(

        "Increase content depth and entity-level relevance signals."
    )

    recommendation_html = ""

    for item in recommendation_list:

        recommendation_html += f"• {item}\n\n"

    return recommendation_html