from tools.crawler import crawl_website

from tools.priority_action_engine import (
    build_priority_actions
)

from tools.action_matrix_builder import (
    build_action_matrix
)

from tools.research_context_builder import (
    build_research_context
)

from tools.scoring_engine import (
    calculate_scores
)

from tools.ai_overview_simulator import (
    simulate_ai_overview
)

from tools.structured_section_generator import (
    executive_summary,
    generate_ai_visibility_section,
    generate_competitor_section,
    generate_serp_section,
    generate_recommendations_section
)

from tools.reflection_engine import (
    generate_reflections
)

from tools.recursive_refinement_engine import (
    recursive_refinement
)

from tools.autonomous_expansion_engine import (
    autonomous_expansion
)

from tools.orchestration_runtime import (
    execute_orchestration
)

from tools.technical_audit_engine import (
    generate_technical_audit
)

from tools.competitor_discovery import (
    discover_competitors
)

from tools.geo_aeo_engine import (
    generate_geo_aeo_analysis
)

from tools.competitor_crawler import (
    crawl_competitors
)

from tools.competitor_scoring import (
    score_competitors
)


# =========================================
# MAIN AI STRATEGY ORCHESTRATOR
# =========================================

def run_ai_strategy(

    url,

    objective
):

    # =====================================
    # ORCHESTRATION EXECUTION
    # =====================================

    orchestration_results = execute_orchestration(

        url,

        objective
    )

    # =====================================
    # WEBSITE CRAWL
    # =====================================

    site_data = crawl_website(url)

    # =====================================
    # TECHNICAL AUDIT
    # =====================================

    technical_audit = generate_technical_audit(

        site_data
    )

    # =====================================
    # GEO / AEO ANALYSIS
    # =====================================

    geo_aeo_analysis = generate_geo_aeo_analysis(

        site_data
    )

    # =====================================
    # COMPETITOR DISCOVERY
    # =====================================

    competitors = discover_competitors(

        url,

        site_data
    )

    # =====================================
    # COMPETITOR CRAWLING
    # =====================================

    crawled_competitors = crawl_competitors(

        competitors
    )

    # =====================================
    # COMPETITOR SCORING
    # =====================================

    competitor_data = score_competitors(

        crawled_competitors
    )

    # =====================================
    # PRIORITY ACTIONS
    # =====================================

    priority_actions = build_priority_actions(

        site_data
    )

    # =====================================
    # ACTION MATRIX
    # =====================================

    action_matrix = build_action_matrix(

        priority_actions
    )

    # =====================================
    # RESEARCH CONTEXT
    # =====================================

    research_context = build_research_context(

        site_data,

        competitor_data
    )

    # =====================================
    # SCORES
    # =====================================

    scores = calculate_scores(

        research_context
    )

    # =====================================
    # AI OVERVIEW
    # =====================================

    ai_overview = simulate_ai_overview(

        site_data
    )

    # =====================================
    # REFLECTIONS
    # =====================================

    reflections = generate_reflections(

        orchestration_results
    )

    # =====================================
    # RECURSIVE REFINEMENT
    # =====================================

    recursive_results = recursive_refinement(

        orchestration_results
    )

    # =====================================
    # AUTONOMOUS TASKS
    # =====================================

    autonomous_tasks = autonomous_expansion(

        orchestration_results
    )

    # =====================================
    # EXECUTIVE SUMMARY
    # =====================================

    executive = executive_summary(

        research_context
    )

    # =====================================
    # AI VISIBILITY SECTION
    # =====================================

    ai_visibility = generate_ai_visibility_section(

        site_data,

        scores
    )

    # =====================================
    # COMPETITOR SECTION
    # =====================================

    competitor_section = generate_competitor_section(

        {
            "competitors": competitor_data
        },

        scores
    )

    # =====================================
    # SERP SECTION
    # =====================================

    serp_section = generate_serp_section(

        site_data,

        scores
    )

    # =====================================
    # RECOMMENDATIONS
    # =====================================

    recommendations = generate_recommendations_section(

        priority_actions
    )

    # =====================================
    # FINAL OUTPUT
    # =====================================

    return {

        "site_data": site_data,

        "technical_audit": technical_audit,

        "geo_aeo_analysis": geo_aeo_analysis,

        "scores": scores,

        "research_context": research_context,

        "priority_actions": priority_actions,

        "action_matrix": action_matrix,

        "ai_overview": ai_overview,

        "executive_summary": executive,

        "ai_visibility": ai_visibility,

        "competitor_analysis": competitor_section,

        "competitor_data": competitor_data,

        "serp_analysis": serp_section,

        "recommendations": recommendations,

        "reflections": reflections,

        "recursive_refinement": recursive_results,

        "autonomous_tasks": autonomous_tasks,

        "orchestration_results": orchestration_results,

        "orchestration_history":
            orchestration_results.get(
                "execution_log",
                []
            ),

        "orchestration_metrics":
            orchestration_results.get(
                "orchestration_metrics",
                {}
            )
    }