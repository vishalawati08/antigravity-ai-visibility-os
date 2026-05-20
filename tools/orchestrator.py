from tools.crawler import (
    crawl_website
)

from tools.geo_aeo_engine import (
    analyze_geo_aeo
)

from tools.competitor_crawler import (
    crawl_competitors
)

from tools.competitor_scoring import (
    score_competitors
)

from tools.research_context_builder import (
    build_research_context
)

from tools.scoring_engine import (
    calculate_scores
)

from tools.structured_section_generator import (

    generate_executive_summary,

    generate_technical_audit,

    generate_geo_section,

    generate_competitor_section,

    generate_recommendations
)


# =========================================
# MAIN ORCHESTRATOR
# =========================================

def run_ai_strategy(

    url,

    prompt
):

    # =====================================
    # CRAWL WEBSITE
    # =====================================

    site_data = crawl_website(
        url
    )

    # =====================================
    # GEO / AEO ANALYSIS
    # =====================================

    geo_analysis = analyze_geo_aeo(
        site_data
    )

    # =====================================
    # COMPETITOR ANALYSIS
    # =====================================

    competitor_data = crawl_competitors(
        url
    )

    # =====================================
    # BUILD RESEARCH CONTEXT
    # =====================================

    research_context = build_research_context(

        site_data,

        geo_analysis,

        competitor_data

    )

    # =====================================
    # CALCULATE SCORES
    # =====================================

    scores = calculate_scores(
        research_context
    )

    # =====================================
    # COMPETITOR SCORING
    # =====================================

    competitor_scores = score_competitors(

        site_data,

        geo_analysis,

        competitor_data

    )

    # =====================================
    # EXECUTIVE SUMMARY
    # =====================================

    executive_summary = generate_executive_summary(

        research_context,

        scores
    )

    # =====================================
    # TECHNICAL AUDIT
    # =====================================

    technical_audit = generate_technical_audit(

        site_data,

        scores
    )

    # =====================================
    # GEO SECTION
    # =====================================

    geo_section = generate_geo_section(

        geo_analysis,

        scores
    )

    # =====================================
    # COMPETITOR SECTION
    # =====================================

    competitor_section = generate_competitor_section(

        competitor_data,

        competitor_scores
    )

    # =====================================
    # RECOMMENDATIONS
    # =====================================

    recommendations = generate_recommendations(

        research_context,

        scores
    )

    # =====================================
    # FINAL REPORT
    # =====================================

    return {

        "url":
            url,

        "prompt":
            prompt,

        "scores":
            scores,

        "research_context":
            research_context,

        "crawl_data":
            site_data,

        "geo_aeo_analysis":
            geo_analysis,

        "competitor_data":
            competitor_data,

        "executive_summary":
            executive_summary,

        "technical_audit":
            technical_audit,

        "geo_section":
            geo_section,

        "competitor_section":
            competitor_section,

        "recommendations":
            recommendations
    }