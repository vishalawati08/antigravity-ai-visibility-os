# =========================================
# EXECUTIVE SUMMARY
# =========================================

def generate_executive_summary(

    research_context,

    scores
):

    seo_score = scores.get(
        "seo_score",
        0
    )

    ai_score = scores.get(
        "ai_visibility_score",
        0
    )

    geo_score = scores.get(
        "geo_score",
        0
    )

    crawl_confidence = research_context.get(
        "crawl_confidence",
        "Low"
    )

    semantic_maturity = research_context.get(
        "semantic_maturity",
        "Low"
    )

    schema_found = research_context.get(
        "schema_found",
        False
    )

    faq_detected = research_context.get(
        "faq_detected",
        False
    )

    pages_crawled = research_context.get(
        "pages_crawled",
        0
    )

    # =====================================
    # SEO SUMMARY
    # =====================================

    if seo_score >= 85:

        seo_summary = (
            "The website demonstrates strong organic search maturity "
            "with well-developed semantic architecture and content breadth."
        )

    elif seo_score >= 70:

        seo_summary = (
            "The website demonstrates above-average search visibility maturity "
            "with opportunities for deeper semantic optimization and entity enrichment."
        )

    elif seo_score >= 55:

        seo_summary = (
            "The website demonstrates moderate search maturity "
            "with opportunities to strengthen semantic discoverability."
        )

    else:

        seo_summary = (
            "The website demonstrates limited search maturity "
            "with significant opportunities for structural SEO improvement."
        )

    # =====================================
    # AI SUMMARY
    # =====================================

    if ai_score >= 85:

        ai_summary = (
            "AI visibility readiness appears strong, supported by "
            "machine-readable semantic structures and conversational discoverability signals."
        )

    elif ai_score >= 70:

        ai_summary = (
            "AI visibility maturity appears promising with opportunities "
            "for improved conversational-answer optimization."
        )

    else:

        ai_summary = (
            "AI discoverability maturity currently appears limited "
            "due to insufficient semantic-answer optimization."
        )

    # =====================================
    # GEO SUMMARY
    # =====================================

    if geo_score >= 85:

        geo_summary = (
            "The platform demonstrates strong GEO/AEO readiness "
            "with mature semantic-answer architecture."
        )

    elif geo_score >= 70:

        geo_summary = (
            "The platform demonstrates evolving GEO/AEO maturity "
            "with opportunities for improved answer-engine optimization."
        )

    else:

        geo_summary = (
            "The current content ecosystem demonstrates weak GEO/AEO maturity "
            "with minimal AI-answer optimization signals."
        )

    # =====================================
    # SEMANTIC SUMMARY
    # =====================================

    if semantic_maturity == "High":

        semantic_summary = (
            "Semantic content architecture appears mature with strong topical structuring."
        )

    elif semantic_maturity == "Medium":

        semantic_summary = (
            "Semantic organization appears partially developed with opportunities "
            "for stronger entity relationships and topical clustering."
        )

    else:

        semantic_summary = (
            "Semantic architecture appears fragmented with limited topical organization."
        )

    # =====================================
    # STRUCTURED DATA
    # =====================================

    structured_summary = ""

    if schema_found:

        structured_summary += (
            "Structured schema markup contributes positively to machine readability. "
        )

    else:

        structured_summary += (
            "Structured schema opportunities remain underutilized. "
        )

    if faq_detected:

        structured_summary += (
            "FAQ-oriented answer structures improve conversational discoverability."
        )

    else:

        structured_summary += (
            "Limited FAQ-style answer structuring may reduce AI-answer visibility."
        )

    # =====================================
    # CRAWL CONFIDENCE
    # =====================================

    if crawl_confidence == "High":

        crawl_summary = (
            f"The analysis was conducted across {pages_crawled} successfully crawled pages, "
            "providing strong confidence in extracted intelligence signals."
        )

    elif crawl_confidence == "Medium":

        crawl_summary = (
            f"The analysis was conducted across {pages_crawled} partially crawled pages, "
            "providing moderate confidence in extracted intelligence signals."
        )

    else:

        crawl_summary = (
            "Limited crawl confidence may reduce extraction completeness "
            "for semantic and technical evaluation."
        )

    # =====================================
    # FINAL SUMMARY
    # =====================================

    final_summary = f"""

    {seo_summary}

    SEO maturity is currently estimated at {seo_score}/100,
    while AI visibility and GEO/AEO readiness are estimated
    at {ai_score}/100 and {geo_score}/100 respectively.

    {ai_summary}

    {geo_summary}

    {semantic_summary}

    {structured_summary}

    {crawl_summary}

    Strategic improvements across semantic architecture,
    entity optimization, structured content formatting,
    conversational-answer readiness and AI discoverability
    may significantly improve future search visibility maturity.

    """

    return final_summary


# =========================================
# TECHNICAL AUDIT
# =========================================

def generate_technical_audit(

    site_data,

    scores
):

    findings = []

    word_count = site_data.get(
        "word_count",
        0
    )

    schema_found = site_data.get(
        "schema_found",
        False
    )

    faq_detected = site_data.get(
        "faq_detected",
        False
    )

    internal_links = len(

        site_data.get(
            "internal_links",
            []
        )
    )

    crawl_confidence = site_data.get(
        "crawl_confidence",
        "Low"
    )

    total_h2 = len(

        site_data.get(
            "h2_tags",
            []
        )
    )

    # =====================================
    # CONTENT DEPTH
    # =====================================

    if word_count >= 5000:

        findings.append({

            "issue":
                "Content Depth",

            "status":
                "Strong",

            "details":
                f"{word_count} words analyzed across crawled pages.",

            "recommendation":
                "Continue strengthening semantic topical authority.",

            "priority":
                "Low"
        })

    elif word_count >= 1500:

        findings.append({

            "issue":
                "Content Depth",

            "status":
                "Moderate",

            "details":
                f"{word_count} words analyzed across crawled pages.",

            "recommendation":
                "Expand structured technical and educational content depth.",

            "priority":
                "Medium"
        })

    else:

        findings.append({

            "issue":
                "Limited Content Depth",

            "status":
                "Weak",

            "details":
                f"Only {word_count} words detected across crawled pages.",

            "recommendation":
                "Substantially expand semantic content architecture.",

            "priority":
                "High"
        })

    # =====================================
    # SCHEMA
    # =====================================

    if schema_found:

        findings.append({

            "issue":
                "Structured Data",

            "status":
                "Strong",

            "details":
                "Structured schema markup detected.",

            "recommendation":
                "Expand schema coverage to additional technical content types.",

            "priority":
                "Medium"
        })

    else:

        findings.append({

            "issue":
                "Structured Data Missing",

            "status":
                "Weak",

            "details":
                "No structured schema markup detected.",

            "recommendation":
                "Implement FAQ, Product and Organization schema.",

            "priority":
                "High"
        })

    # =====================================
    # FAQ
    # =====================================

    if faq_detected:

        findings.append({

            "issue":
                "FAQ Optimization",

            "status":
                "Strong",

            "details":
                "Conversational FAQ structures detected.",

            "recommendation":
                "Expand answer-engine optimization coverage.",

            "priority":
                "Medium"
        })

    else:

        findings.append({

            "issue":
                "FAQ Optimization",

            "status":
                "Weak",

            "details":
                "No FAQ-oriented answer structures detected.",

            "recommendation":
                "Implement FAQ and conversational-answer formatting.",

            "priority":
                "High"
        })

    # =====================================
    # INTERNAL LINKING
    # =====================================

    if internal_links >= 400:

        link_status = "Strong"

    elif internal_links >= 100:

        link_status = "Moderate"

    else:

        link_status = "Weak"

    findings.append({

        "issue":
            "Internal Linking",

        "status":
            link_status,

        "details":
            f"{internal_links} internal links detected.",

        "recommendation":
            "Improve semantic internal linking between topical clusters.",

        "priority":
            "Medium"
    })

    # =====================================
    # SEMANTIC STRUCTURE
    # =====================================

    if total_h2 >= 10:

        semantic_status = "Strong"

    elif total_h2 >= 5:

        semantic_status = "Moderate"

    else:

        semantic_status = "Weak"

    findings.append({

        "issue":
            "Semantic Structure",

        "status":
            semantic_status,

        "details":
            f"{total_h2} semantic H2 structures detected.",

        "recommendation":
            "Improve semantic topic hierarchy and structured content organization.",

        "priority":
            "Medium"
    })

    # =====================================
    # CRAWL CONFIDENCE
    # =====================================

    findings.append({

        "issue":
            "Crawl Confidence",

        "status":
            crawl_confidence,

        "details":
            "Crawler extraction confidence based on rendered accessibility and semantic extraction completeness.",

        "recommendation":
            "Improve crawl accessibility and rendered semantic stability.",

        "priority":
            "Low"
    })

    return findings


# =========================================
# GEO SECTION
# =========================================

def generate_geo_section(

    geo_analysis,

    scores
):

    return geo_analysis


# =========================================
# COMPETITOR SECTION
# =========================================

def generate_competitor_section(

    competitor_data,

    competitor_scores
):

    # =====================================
    # SAFE DEFAULTS
    # =====================================

    if not isinstance(
        competitor_data,
        list
    ):

        competitor_data = []

    # =====================================
    # COMPETITOR NARRATIVES
    # =====================================

    narratives = []

    strongest_competitor = None

    strongest_score = 0

    weakest_competitor = None

    weakest_score = 999

    # =====================================
    # ANALYZE COMPETITORS
    # =====================================

    for competitor in competitor_data:

        if not isinstance(
            competitor,
            dict
        ):

            continue

        name = competitor.get(
            "name",
            "Unknown"
        )

        seo_score = competitor.get(
            "seo_score",
            0
        )

        ai_score = competitor.get(
            "ai_visibility",
            0
        )

        geo_score = competitor.get(
            "geo_score",
            0
        )

        semantic_maturity = competitor.get(
            "semantic_maturity",
            "Low"
        )

        crawl_confidence = competitor.get(
            "crawl_confidence",
            "Low"
        )

        average_score = round(

            (
                seo_score
                +
                ai_score
                +
                geo_score
            )

            / 3
        )

        # =================================
        # STRONGEST / WEAKEST
        # =================================

        if average_score > strongest_score:

            strongest_score = average_score

            strongest_competitor = name

        if average_score < weakest_score:

            weakest_score = average_score

            weakest_competitor = name

        # =================================
        # INDIVIDUAL NARRATIVE
        # =================================

        if average_score >= 85:

            narrative = (

                f"{name} demonstrates strong semantic maturity, AI visibility readiness "
                f"and answer-engine optimization across its digital ecosystem."
            )

        elif average_score >= 70:

            narrative = (

                f"{name} demonstrates evolving search visibility maturity with "
                f"moderately developed semantic architecture and AI-answer readiness."
            )

        elif average_score >= 50:

            narrative = (

                f"{name} demonstrates partial semantic maturity with opportunities "
                f"for stronger AI-search optimization and structured discoverability."
            )

        else:

            narrative = (

                f"{name} demonstrates limited semantic maturity and weaker "
                f"AI-search discoverability signals relative to industry leaders."
            )

        # =================================
        # CRAWL CONFIDENCE
        # =================================

        if crawl_confidence == "Low":

            narrative += (
                " Crawl confidence was limited, reducing extraction completeness."
            )

        # =================================
        # SEMANTIC MATURITY
        # =================================

        if semantic_maturity == "High":

            narrative += (
                " Strong semantic structuring contributes positively to topical authority."
            )

        elif semantic_maturity == "Medium":

            narrative += (
                " Semantic organization appears partially developed."
            )

        narratives.append(

            {
                "name": name,
                "narrative": narrative
            }
        )

    # =====================================
    # STRATEGIC BENCHMARK SUMMARY
    # =====================================

    benchmark_summary = ""

    if strongest_competitor:

        benchmark_summary += (

            f"{strongest_competitor} currently demonstrates the strongest overall "
            f"AI visibility and semantic maturity profile among analyzed competitors. "
        )

    if weakest_competitor:

        benchmark_summary += (

            f"{weakest_competitor} demonstrates comparatively weaker semantic "
            f"discoverability and AI-search readiness signals. "
        )

    benchmark_summary += (

        "Competitive differentiation opportunities exist across semantic content depth, "
        "AI-answer optimization, structured data ecosystems and conversational discoverability."
    )

    # =====================================
    # FINAL OUTPUT
    # =====================================

    return {

        "competitors":
            competitor_data,

        "benchmark_scores":
            competitor_scores,

        "narratives":
            narratives,

        "benchmark_summary":
            benchmark_summary
    }


# =========================================
# STRATEGIC RECOMMENDATIONS
# =========================================

def generate_recommendations(

    research_context,

    scores
):

    recommendations = []

    if not isinstance(
        research_context,
        dict
    ):

        research_context = {}

    if not isinstance(
        scores,
        dict
    ):

        scores = {}

    seo_score = scores.get(
        "seo_score",
        0
    )

    ai_score = scores.get(
        "ai_visibility_score",
        0
    )

    geo_score = scores.get(
        "geo_score",
        0
    )

    word_count = research_context.get(
        "word_count",
        0
    )

    total_h2 = research_context.get(
        "total_h2",
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

    crawl_confidence = research_context.get(
        "crawl_confidence",
        "Low"
    )

    semantic_maturity = research_context.get(
        "semantic_maturity",
        "Low"
    )

    geo_maturity = research_context.get(
        "geo_maturity",
        "Low"
    )

    internal_links = research_context.get(
        "internal_links",
        0
    )

    pages_crawled = research_context.get(
        "pages_crawled",
        0
    )

    all_text = str(

        research_context.get(
            "all_text",
            ""
        )
    ).lower()

    connector_keywords = [

        "connector",
        "backplane",
        "signal integrity",
        "high speed",
        "power delivery",
        "edge computing",
        "server",
        "gpu",
        "thermal",
        "data center",
        "pcb",
        "high density",
        "networking",
        "ai infrastructure",
        "rack",
        "hyperscale"
    ]

    detected_connector_industry = any(

        keyword in all_text

        for keyword in connector_keywords
    )

    # =====================================
    # CONTENT DEPTH
    # =====================================

    if word_count < 2500:

        if detected_connector_industry:

            recommendations.append(

                "Expand semantic topic coverage around high-speed connectivity, power delivery architectures, signal integrity optimization and edge-compute deployment scenarios."
            )

        else:

            recommendations.append(

                "Expand long-form semantic content coverage across high-intent topical clusters."
            )

    elif word_count < 5000:

        recommendations.append(

            "Increase topical authority depth through additional structured technical and educational content."
        )

    # =====================================
    # SEMANTIC STRUCTURE
    # =====================================

    if total_h2 < 8:

        recommendations.append(

            "Improve semantic hierarchy using richer H2/H3 topical clustering and structured information architecture."
        )

    # =====================================
    # INTERNAL LINKING
    # =====================================

    if internal_links < 100:

        recommendations.append(

            "Strengthen semantic internal linking between related solution pages, product ecosystems and technical content clusters."
        )

    # =====================================
    # SCHEMA
    # =====================================

    if not schema_found:

        recommendations.append(

            "Implement expanded machine-readable schema coverage including FAQ, Product, Organization and TechnicalArticle schema structures."
        )

    else:

        recommendations.append(

            "Expand structured schema coverage across technical resources, product ecosystems and educational content."
        )

    # =====================================
    # FAQ
    # =====================================

    if not faq_detected:

        if detected_connector_industry:

            recommendations.append(

                "Develop conversational-answer content around connector selection, thermal optimization, high-density deployment and AI infrastructure interoperability."
            )

        else:

            recommendations.append(

                "Expand FAQ-oriented answer structures to improve AI-answer discoverability and conversational search visibility."
            )

    else:

        recommendations.append(

            "Expand conversational-answer coverage across broader technical and deployment-oriented search intents."
        )

    # =====================================
    # AI VISIBILITY
    # =====================================

    if ai_score < 80:

        recommendations.append(

            "Strengthen AI-answer discoverability through semantic enrichment and conversational optimization."
        )

    else:

        recommendations.append(

            "Continue strengthening AI-search discoverability through entity-rich semantic architecture and answer-engine optimization."
        )

    # =====================================
    # GEO
    # =====================================

    if geo_score < 80:

        recommendations.append(

            "Increase answer-engine optimization maturity through structured question-answer content and semantic entity relationships."
        )

    else:

        recommendations.append(

            "Expand semantic-answer ecosystems supporting AI-generated search experiences and conversational retrieval systems."
        )

    # =====================================
    # SEMANTIC MATURITY
    # =====================================

    if semantic_maturity == "Low":

        recommendations.append(

            "Strengthen semantic topic clustering and entity relationships to improve topical authority signals."
        )

    elif semantic_maturity == "Medium":

        recommendations.append(

            "Improve semantic depth through expanded entity relationships and interconnected topical ecosystems."
        )

    # =====================================
    # GEO MATURITY
    # =====================================

    if geo_maturity == "Low":

        recommendations.append(

            "Improve GEO/AEO maturity through enhanced answer structuring and conversational semantic formatting."
        )

    # =====================================
    # CRAWL CONFIDENCE
    # =====================================

    if crawl_confidence == "Low":

        recommendations.append(

            "Improve crawl accessibility, rendered semantic content stability and machine-readable discoverability."
        )

    # =====================================
    # PAGE COVERAGE
    # =====================================

    if pages_crawled <= 1:

        recommendations.append(

            "Expand crawl-accessible semantic content depth across additional technical and solution-oriented landing pages."
        )

    # =====================================
    # ADVANCED INDUSTRY RECOMMENDATIONS
    # =====================================

    if detected_connector_industry:

        recommendations.append(

            "Expand technical semantic coverage around AI server infrastructure, rack-density optimization and high-speed backplane ecosystems."
        )

        recommendations.append(

            "Develop AI-search-optimized educational content supporting edge computing, thermal performance and next-generation connector deployment use cases."
        )

    # =====================================
    # HIGH PERFORMANCE
    # =====================================

    if (

        seo_score >= 85

        and

        ai_score >= 85

        and

        geo_score >= 80
    ):

        recommendations.append(

            "Maintain leadership positioning through continuous semantic expansion and AI-search ecosystem optimization."
        )

    # =====================================
    # REMOVE DUPLICATES
    # =====================================

    recommendations = list(

        dict.fromkeys(
            recommendations
        )
    )

    return recommendations