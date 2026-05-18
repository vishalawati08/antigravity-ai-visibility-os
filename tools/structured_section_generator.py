# =========================================
# EXECUTIVE SUMMARY
# =========================================

def executive_summary(

    research_context
):

    word_count = research_context.get(
        "word_count",
        0
    )

    ai_readiness = research_context.get(
        "ai_readiness",
        "Low"
    )

    competitor_average = research_context.get(
        "competitor_average",
        0
    )

    summary = """

    The analysis indicates that the website
    demonstrates evolving search visibility
    maturity with opportunities to improve
    semantic discoverability, AI-answer
    readiness and competitive positioning.

    """

    # =====================================
    # CONTENT DEPTH
    # =====================================

    if word_count > 4000:

        summary += """

        Strong content depth and semantic
        breadth contribute positively to
        topical authority and AI discoverability.

        """

    elif word_count < 1500:

        summary += """

        Limited semantic depth may reduce
        topical authority and weaken broader
        search discoverability.

        """

    # =====================================
    # AI READINESS
    # =====================================

    if ai_readiness == "High":

        summary += """

        AI-answer readiness appears strong,
        supported by semantic structure,
        machine-readable content and
        conversational discoverability signals.

        """

    elif ai_readiness == "Low":

        summary += """

        AI-answer readiness remains limited,
        particularly across structured
        conversational optimization signals.

        """

    # =====================================
    # COMPETITOR POSITION
    # =====================================

    if competitor_average > 75:

        summary += """

        Competitive benchmarking indicates
        that industry competitors demonstrate
        relatively mature semantic and AI
        visibility strategies.

        """

    elif competitor_average > 60:

        summary += """

        Competitive analysis suggests
        moderate industry maturity with
        opportunities for strategic
        differentiation.

        """

    summary += """

    Strategic improvements across
    semantic architecture, structured
    content and AI-answer optimization
    may significantly improve both
    organic search visibility and
    AI-generated discoverability.

    """

    return summary


# =========================================
# AI VISIBILITY SECTION
# =========================================

def generate_ai_visibility_section(

    site_data,

    scores
):

    ai_score = scores.get(
        "ai_visibility_score",
        0
    )

    geo_score = scores.get(
        "geo_score",
        0
    )

    section = f"""

    AI Visibility Intelligence

    AI Visibility Score:
    {ai_score}/100

    GEO / AEO Score:
    {geo_score}/100

    """

    # =====================================
    # SCORE INTERPRETATION
    # =====================================

    if ai_score >= 80:

        section += """

        The website demonstrates strong
        AI-search readiness with relatively
        mature semantic architecture and
        answer-focused discoverability.

        """

    elif ai_score >= 60:

        section += """

        AI visibility maturity appears
        moderate with opportunities to
        strengthen conversational
        optimization and semantic clarity.

        """

    else:

        section += """

        AI discoverability maturity appears
        limited and may reduce inclusion
        within AI-generated search responses.

        """

    # =====================================
    # FAQ
    # =====================================

    if site_data.get("faq_detected"):

        section += """

        FAQ-focused semantic structures
        contribute positively toward
        conversational answer extraction.

        """

    else:

        section += """

        FAQ-oriented semantic structures
        were not strongly detected and
        remain a strategic opportunity area.

        """

    # =====================================
    # SCHEMA
    # =====================================

    if site_data.get("schema_found"):

        section += """

        Structured schema implementation
        improves machine-readable context
        and entity interpretation.

        """

    else:

        section += """

        Missing schema implementation may
        reduce structured discoverability
        across AI systems and search engines.

        """

    return section


# =========================================
# COMPETITOR SECTION
# =========================================

def generate_competitor_section(

    competitor_data,

    scores
):

    competitors = competitor_data.get(
        "competitors",
        []
    )

    section = """

    Competitive Benchmarking Analysis

    The platform identified multiple
    industry-relevant competitors with
    measurable differences across
    semantic maturity, AI visibility
    and content authority.

    """

    if not competitors:

        section += """

        No competitor intelligence
        could be generated.

        """

        return section

    # =====================================
    # BENCHMARK TABLE
    # =====================================

    section += """

    Benchmark Comparison

    """

    for competitor in competitors:

        section += f"""

        ------------------------------------------------

        Competitor:
        {competitor.get('name', 'Unknown')}

        SEO Score:
        {competitor.get('seo_score', 0)}/100

        AI Visibility:
        {competitor.get('ai_visibility', 0)}/100

        GEO / AEO:
        {competitor.get('geo_score', 0)}/100

        Content Depth:
        {competitor.get('content_depth', 'Low')}

        Total Content:
        {competitor.get('word_count', 0)} words

        """

    # =====================================
    # STRATEGIC GAP ANALYSIS
    # =====================================

    section += """

    Strategic Gap Analysis

    Competitive benchmarking indicates
    that differentiation opportunities
    primarily exist across:

    - semantic content architecture
    - answer-focused optimization
    - AI discoverability maturity
    - structured schema implementation
    - topical authority expansion
    - conversational search readiness
    - semantic hierarchy refinement

    """

    # =====================================
    # POSITIONING
    # =====================================

    own_score = scores.get(
        "seo_score",
        0
    )

    top_competitor = max(

        competitors,

        key=lambda x:
            x.get("seo_score", 0)
    )

    competitor_score = top_competitor.get(
        "seo_score",
        0
    )

    if own_score >= competitor_score:

        section += """

        The website demonstrates competitive
        leadership across several core
        visibility dimensions.

        """

    else:

        section += f"""

        The strongest competitor currently
        demonstrates higher estimated SEO
        maturity ({competitor_score}/100),
        indicating opportunities for further
        strategic optimization.

        """

    return section


# =========================================
# SERP SECTION
# =========================================

def generate_serp_section(

    site_data,

    scores
):

    seo_score = scores.get(
        "seo_score",
        0
    )

    word_count = site_data.get(
        "word_count",
        0
    )

    section = f"""

    SERP Visibility Intelligence

    Estimated SEO Maturity:
    {seo_score}/100

    """

    # =====================================
    # SCORE ANALYSIS
    # =====================================

    if seo_score >= 80:

        section += """

        The website demonstrates strong
        technical and semantic SEO maturity
        supporting broader search visibility.

        """

    elif seo_score >= 60:

        section += """

        Moderate SEO maturity detected with
        opportunities to improve semantic
        structure and discoverability.

        """

    else:

        section += """

        SEO maturity appears relatively
        limited compared to broader
        competitive benchmarks.

        """

    # =====================================
    # CONTENT ANALYSIS
    # =====================================

    section += f"""

    Approximate semantic content analyzed:
    {word_count} words

    """

    if word_count > 4000:

        section += """

        Strong semantic depth supports
        topical authority expansion and
        broader keyword discoverability.

        """

    else:

        section += """

        Additional semantic expansion may
        improve topical breadth and ranking
        opportunities.

        """

    # =====================================
    # STRATEGIC AREAS
    # =====================================

    section += """

    Additional optimization opportunities
    include:

    - semantic topic clustering
    - internal linking refinement
    - structured metadata optimization
    - AI-answer discoverability
    - content hierarchy enhancement
    - semantic authority expansion

    """

    return section


# =========================================
# RECOMMENDATIONS SECTION
# =========================================

def generate_recommendations_section(

    priority_actions
):

    section = """

    Strategic Recommendations

    The following initiatives are
    recommended to improve both
    traditional SEO performance and
    AI-generated visibility.

    """

    if not priority_actions:

        section += """

        No major strategic recommendations
        were generated during the analysis.

        """

        return section

    # =====================================
    # PRIORITY ACTIONS
    # =====================================

    for action in priority_actions:

        if isinstance(action, str):

            section += f"""

            ------------------------------------------------

            Recommendation:
            {action}

            Estimated Priority:
            Medium

            """

        elif isinstance(action, dict):

            section += f"""

            ------------------------------------------------

            Recommendation:
            {action.get('action', '')}

            Priority Level:
            {action.get('priority', 'Medium')}

            """

    # =====================================
    # STRATEGIC INITIATIVES
    # =====================================

    section += """

    Recommended long-term strategic
    focus areas include:

    - AI-answer optimization
    - conversational discoverability
    - semantic content scaling
    - structured entity implementation
    - semantic hierarchy refinement
    - topical authority expansion
    - internal linking architecture
    - AI-search readiness enhancement

    """

    return section