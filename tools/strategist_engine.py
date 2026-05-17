def generate_strategic_insights(data):

    insights = []

    priorities = []

    # =========================
    # EXECUTIVE SEO ANALYSIS
    # =========================

    if data["seo_score"] >= 80:

        insights.append(
            "The website demonstrates strong foundational SEO health with solid metadata, internal linking, and content depth."
        )

    elif data["seo_score"] >= 60:

        insights.append(
            "The website has moderate SEO performance but contains structural weaknesses limiting search visibility."
        )

    else:

        insights.append(
            "The website suffers from significant SEO weaknesses affecting discoverability and ranking potential."
        )

    # =========================
    # H1 STRUCTURE
    # =========================

    if len(data["h1_tags"]) > 1:

        insights.append(
            "Multiple H1 tags dilute topical focus and weaken semantic clarity for search engines."
        )

        priorities.append(
            "Reduce multiple H1 tags to strengthen semantic hierarchy."
        )

    # =========================
    # CONTENT DEPTH
    # =========================

    if data["word_count"] > 1200:

        insights.append(
            "Strong content depth improves topical authority and long-tail keyword coverage."
        )

    elif data["word_count"] < 500:

        insights.append(
            "Thin content reduces topical authority and weakens ranking potential for technical queries."
        )

        priorities.append(
            "Expand content depth using specifications, use cases, FAQs, and supporting semantic content."
        )

    # =========================
    # IMAGE SEO
    # =========================

    if data["missing_alt_count"] > 0:

        insights.append(
            f"{data['missing_alt_count']} images are missing ALT text, reducing accessibility and image-search visibility."
        )

        priorities.append(
            "Add descriptive ALT text across all product and marketing visuals."
        )

    # =========================
    # GEO / AEO ANALYSIS
    # =========================

    if data["geo_score"] < 40:

        insights.append(
            "The website is weakly optimized for AI-driven search environments such as ChatGPT, Gemini, and Perplexity."
        )

        priorities.append(
            "Implement answer blocks, schema markup, and structured AI-readable content."
        )

    elif data["geo_score"] >= 70:

        insights.append(
            "The website demonstrates strong AI-search readiness and AI-citability signals."
        )

    # =========================
    # ANSWER BLOCKS
    # =========================

    if data["answer_blocks"] == 0:

        insights.append(
            "No concise answer blocks were detected, limiting AI citation opportunities."
        )

    else:

        insights.append(
            "Answer-style content improves AI-engine extraction and visibility."
        )

    # =========================
    # SCHEMA ANALYSIS
    # =========================

    if data["schema_found"] == 0:

        insights.append(
            "The absence of structured schema weakens machine-readable understanding and rich-result eligibility."
        )

        priorities.append(
            "Add Product, Organization, FAQ, and Breadcrumb schema markup."
        )

    else:

        insights.append(
            "Structured schema markup improves machine-readable search visibility."
        )

    # =========================
    # TABLE ANALYSIS
    # =========================

    if data["tables_found"] == 0:

        insights.append(
            "No structured specification tables were detected, limiting technical readability and AI extraction."
        )

    else:

        insights.append(
            "Structured specification tables strengthen technical clarity and AI readability."
        )

    # =========================
    # SERP INTELLIGENCE
    # =========================

    serp_insights = data.get("serp_insights", [])

    for serp in serp_insights:

        insights.append(serp)

    if any(
        "distributor" in item.lower()
        for item in serp_insights
    ):

        priorities.append(
            "Improve manufacturer-level search ownership to reduce distributor SERP dominance."
        )

    # =========================
    # EXECUTIVE SUMMARY
    # =========================

    executive_summary = (
        "This audit evaluates the website's SEO foundation, AI-search readiness, "
        "content structure, and strategic search visibility. "
        "While the website demonstrates baseline optimization maturity, improvements "
        "in semantic structure, AI-search formatting, and search ownership strategy "
        "are required to compete effectively in modern AI-driven search ecosystems."
    )

    return {
        "executive_summary": executive_summary,
        "strategic_insights": insights,
        "priority_actions": priorities,
    }