# =========================================
# STRATEGIC SIGNAL ENGINE
# =========================================

def generate_strategic_signals(research_context):

    signals = []

    technical = research_context["technical_seo"]

    geo = research_context["geo_aeo_signals"]

    competitors = research_context[
        "competitor_positioning"
    ]

    # =====================================
    # SEO MATURITY
    # =====================================

    if technical["seo_score"] < 70:

        signals.append(
            "Technical SEO maturity remains below "
            "enterprise competitive standards, "
            "limiting long-term organic visibility."
        )

    # =====================================
    # SCHEMA SIGNALS
    # =====================================

    if "No schema markup detected." in geo["weaknesses"]:

        signals.append(
            "Absence of structured schema reduces "
            "eligibility for AI-generated answer "
            "surfaces and semantic interpretation."
        )

    # =====================================
    # CONTENT DEPTH
    # =====================================

    if technical["word_count"] < 1000:

        signals.append(
            "Limited semantic content depth weakens "
            "AI discoverability and topical authority."
        )

    # =====================================
    # H1 STRUCTURE
    # =====================================

    if len(technical["h1_tags"]) > 1:

        signals.append(
            "Fragmented heading hierarchy may reduce "
            "semantic clarity for AI parsers."
        )

    # =====================================
    # IMAGE SEO
    # =====================================

    if technical["missing_alt"] > 0:

        signals.append(
            "Missing ALT attributes reduce multimodal "
            "AI-search visibility potential."
        )

    # =====================================
    # COMPETITOR COMPARISON
    # =====================================

    for competitor in competitors:

        if competitor["geo_score"] > geo["geo_score"]:

            signals.append(
                f"{competitor['url']} demonstrates "
                f"stronger AI-search readiness and "
                f"semantic optimization maturity."
            )

    # =====================================
    # SERP OWNERSHIP
    # =====================================

    serp_insights = research_context[
        "serp_intelligence"
    ]["serp_insights"]

    for insight in serp_insights:

        if "distributor" in insight.lower():

            signals.append(
                "Distributor ecosystems may currently "
                "control valuable commercial search "
                "visibility."
            )

    # =====================================
    # AI SEARCH READINESS
    # =====================================

    if geo["geo_score"] < 60:

        signals.append(
            "The website currently behaves more like "
            "a traditional enterprise website than "
            "an AI-citable knowledge source."
        )

    # =====================================
    # CONTENT ARCHITECTURE
    # =====================================

    if technical["word_count"] < 700:

        signals.append(
            "Shallow content architecture limits "
            "semantic coverage across modern "
            "answer-engine ecosystems."
        )

    return signals