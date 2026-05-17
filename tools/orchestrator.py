from tools.crawler import crawl_website

from tools.dynamic_competitor_finder import (
    discover_competitors
)

from tools.research_planner import (
    build_research_plan
)

from tools.priority_action_engine import (
    build_priority_actions
)

from tools.action_matrix_builder import (
    build_action_matrix
)

from tools.research_context_builder import (
    build_research_context
)

from tools.ai_overview_simulator import (
    simulate_ai_overview
)

from tools.orchestration_executor import (
    OrchestrationExecutor
)

from tools.reflection_engine import (
    ReflectionEngine
)

from tools.recursive_refinement_engine import (
    RecursiveRefinementEngine
)

from tools.task_planning_engine import (
    TaskPlanningEngine
)

from tools.persistent_memory import (
    PersistentMemory
)

from tools.orchestration_scoring_engine import (
    OrchestrationScoringEngine
)

from tools.structured_section_generator import (

    executive_summary,

    ai_visibility_analysis,

    competitor_analysis,

    serp_analysis,

    recommendations
)

from tools.scoring_engine import (
    calculate_scores
)

from tools.competitor_table_builder import (
    build_competitor_table
)


# =========================================
# MAIN AI STRATEGY ORCHESTRATOR
# =========================================

def run_ai_strategy(url, prompt):

    # =====================================
    # ORCHESTRATION EXECUTOR
    # =====================================

    executor = (
        OrchestrationExecutor()
    )

    orchestration_results = (
        executor.run()
    )

    # =====================================
    # PERSISTENT MEMORY
    # =====================================

    persistent_memory = (
        PersistentMemory()
    )

    persistent_memory.store_execution(
        orchestration_results
    )

    orchestration_history = (
        persistent_memory.get_history()
    )

    # =====================================
    # WEBSITE CRAWL
    # =====================================

    site_data = crawl_website(url)

    # =====================================
    # COMPETITOR DISCOVERY
    # =====================================

    competitors = discover_competitors(url)

    competitor_data = []

    for competitor in competitors:

        try:

            data = crawl_website(competitor)

            competitor_data.append({

                "url":
                    competitor,

                "seo_score":
                    data["seo_score"],

                "geo_score":
                    data["geo_score"],

                "word_count":
                    data["word_count"],

                "issues":
                    data["issues"],

                "schema_found":
                    data["schema_found"]
            })

        except Exception:

            pass

    # =====================================
    # RESEARCH PLAN
    # =====================================

    research_plan = build_research_plan(

        site_data,

        competitor_data
    )

    # =====================================
    # ACTIONS
    # =====================================

    priority_actions = (
        build_priority_actions(
            site_data
        )
    )

    action_matrix = (
        build_action_matrix(
            priority_actions
        )
    )

    # =====================================
    # RESEARCH CONTEXT
    # =====================================

    research_context = build_research_context(

        site_data,

        competitor_data
    )

    # =====================================
    # BUSINESS SCORING
    # =====================================

    scores = calculate_scores(
        research_context
    )

    # =====================================
    # COMPETITOR TABLE
    # =====================================

    competitor_table = (
        build_competitor_table(

            site_data,

            competitor_data
        )
    )

    # =====================================
    # AI OVERVIEW
    # =====================================

    ai_overview = simulate_ai_overview(
        site_data
    )

    # =====================================
    # REFLECTION
    # =====================================

    reflection_engine = (
        ReflectionEngine()
    )

    reflections = (
        reflection_engine.evaluate(
            orchestration_results
        )
    )

    # =====================================
    # RECURSIVE REFINEMENT
    # =====================================

    refinement_engine = (
        RecursiveRefinementEngine()
    )

    should_refine = (
        refinement_engine.should_refine(
            reflections
        )
    )

    refinement_actions = (
        refinement_engine.generate_refinements(
            reflections
        )
    )

    # =====================================
    # AUTONOMOUS TASKS
    # =====================================

    task_engine = (
        TaskPlanningEngine()
    )

    autonomous_tasks = (
        task_engine.generate_tasks(

            reflections,

            orchestration_results[
                "shared_memory"
            ]
        )
    )

    # =====================================
    # ORCHESTRATION SCORING
    # =====================================

    orchestration_scoring = (
        OrchestrationScoringEngine()
    )

    orchestration_metrics = (

        orchestration_scoring
        .calculate_score(

            orchestration_results,

            reflections,

            autonomous_tasks
        )
    )

    # =====================================
    # CLEANER
    # =====================================

    def clean_text(text):

        if not isinstance(text, str):

            return text

        return (

            text

            .replace("###", "")

            .replace("**", "")

            .replace("```", "")

            .strip()
        )

    # =====================================
    # REPORT TEXT
    # =====================================

    executive_summary_text = clean_text(

        executive_summary(
            research_context
        )
    )

    ai_visibility_text = clean_text(

        ai_visibility_analysis(
            research_context
        )
    )

    competitor_analysis_text = clean_text(

        competitor_analysis(

            research_context,

            competitor_data
        )
    )

    serp_analysis_text = clean_text(

        serp_analysis(
            research_context
        )
    )

    recommendations_text = clean_text(

        recommendations(
            research_context
        )
    )

    ai_overview_text = clean_text(
        ai_overview
    )

    # =====================================
    # FINAL REPORT
    # =====================================

    report = {

        "orchestration_results":
            orchestration_results,

        "orchestration_history":
            orchestration_history,

        "orchestration_metrics":
            orchestration_metrics,

        "reflections":
            reflections,

        "recursive_refinement": {

            "should_refine":
                should_refine,

            "actions":
                refinement_actions
        },

        "autonomous_tasks":
            autonomous_tasks,

        "scores":
            scores,

        "research_plan":
            research_plan,

        "priority_actions":
            priority_actions,

        "action_matrix":
            action_matrix,

        "ai_overview":
            ai_overview_text,

        "executive_summary":
            executive_summary_text,

        "ai_visibility":
            ai_visibility_text,

        "competitor_analysis":
            competitor_analysis_text,

        "competitor_table":
            competitor_table,

        "serp_analysis":
            serp_analysis_text,

        "recommendations":
            recommendations_text
    }

    return report