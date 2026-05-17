# =========================================
# ORCHESTRATION GRAPH ENGINE
# =========================================

def build_execution_graph():

    graph = {

        "crawl_website": {

            "depends_on": [],

            "next": [

                "discover_competitors",

                "technical_analysis",

                "geo_analysis"
            ]
        },

        "discover_competitors": {

            "depends_on": [

                "crawl_website"
            ],

            "next": [

                "competitor_analysis"
            ]
        },

        "technical_analysis": {

            "depends_on": [

                "crawl_website"
            ],

            "next": [

                "strategic_signal_engine"
            ]
        },

        "geo_analysis": {

            "depends_on": [

                "crawl_website"
            ],

            "next": [

                "ai_citation_analysis",

                "ai_overview_simulation"
            ]
        },

        "competitor_analysis": {

            "depends_on": [

                "discover_competitors"
            ],

            "next": [

                "priority_engine"
            ]
        },

        "strategic_signal_engine": {

            "depends_on": [

                "technical_analysis"
            ],

            "next": [

                "recommendation_engine"
            ]
        },

        "ai_citation_analysis": {

            "depends_on": [

                "geo_analysis"
            ],

            "next": [

                "recommendation_engine"
            ]
        },

        "ai_overview_simulation": {

            "depends_on": [

                "geo_analysis"
            ],

            "next": [

                "recommendation_engine"
            ]
        },

        "priority_engine": {

            "depends_on": [

                "competitor_analysis"
            ],

            "next": [

                "report_generation"
            ]
        },

        "recommendation_engine": {

            "depends_on": [

                "strategic_signal_engine",

                "ai_citation_analysis"
            ],

            "next": [

                "report_generation"
            ]
        },

        "report_generation": {

            "depends_on": [

                "priority_engine",

                "recommendation_engine"
            ],

            "next": []
        }
    }

    return graph