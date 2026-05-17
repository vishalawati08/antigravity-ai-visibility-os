# =========================================
# AGENT REGISTRY
# =========================================

def get_agent_registry():

    agents = {

        "technical_seo_agent": {

            "role":
                "Technical SEO Specialist",

            "objective":
                (
                    "Analyze crawlability, "
                    "metadata structure, "
                    "technical SEO maturity "
                    "and indexing readiness."
                )
        },

        "geo_intelligence_agent": {

            "role":
                "AI Visibility Strategist",

            "objective":
                (
                    "Analyze GEO readiness, "
                    "AI discoverability, "
                    "semantic search optimization "
                    "and AI-citation potential."
                )
        },

        "competitor_agent": {

            "role":
                "Competitive Intelligence Analyst",

            "objective":
                (
                    "Analyze competitors, "
                    "visibility gaps, "
                    "market positioning "
                    "and comparative weaknesses."
                )
        },

        "recommendation_agent": {

            "role":
                "Strategic Growth Advisor",

            "objective":
                (
                    "Generate prioritized "
                    "business recommendations "
                    "for AI-search growth."
                )
        }
    }

    return agents