# =========================================
# RESEARCH PLANNER ENGINE
# =========================================

def build_research_plan(

    site_data,

    competitors
):

    plan = []

    # =====================================
    # TECHNICAL SEO
    # =====================================

    if site_data["seo_score"] < 80:

        plan.append({

            "stage":
                "Technical SEO Analysis",

            "priority":
                "High",

            "reason":
                (
                    "Technical SEO maturity "
                    "appears below competitive "
                    "enterprise standards."
                )
        })

    # =====================================
    # AI VISIBILITY
    # =====================================

    if site_data["geo_score"] < 70:

        plan.append({

            "stage":
                "AI Visibility Assessment",

            "priority":
                "Critical",

            "reason":
                (
                    "AI-search readiness appears "
                    "weak for modern answer engines."
                )
        })

    # =====================================
    # CONTENT DEPTH
    # =====================================

    if site_data["word_count"] < 1000:

        plan.append({

            "stage":
                "Semantic Content Analysis",

            "priority":
                "High",

            "reason":
                (
                    "Limited semantic depth may "
                    "reduce topical authority."
                )
        })

    # =====================================
    # SCHEMA ANALYSIS
    # =====================================

    if not site_data["schema_found"]:

        plan.append({

            "stage":
                "Structured Data Audit",

            "priority":
                "Critical",

            "reason":
                (
                    "Missing schema limits "
                    "AI-citation readiness."
                )
        })

    # =====================================
    # COMPETITOR ANALYSIS
    # =====================================

    if len(competitors) > 0:

        plan.append({

            "stage":
                "Competitive Visibility Analysis",

            "priority":
                "High",

            "reason":
                (
                    "Competitive benchmarking "
                    "required for market positioning."
                )
        })

    # =====================================
    # SERP ANALYSIS
    # =====================================

    if site_data["serp_insights"]:

        plan.append({

            "stage":
                "SERP Ownership Analysis",

            "priority":
                "Medium",

            "reason":
                (
                    "Search ownership risks "
                    "detected within ranking ecosystem."
                )
        })

    return plan