# =========================================
# ADAPTIVE ROUTING ENGINE
# =========================================

class RoutingEngine:

    def should_execute(

        self,

        node_name,

        shared_memory
    ):

        # =================================
        # GEO ANALYSIS ROUTING
        # =================================

        if node_name == "geo_analysis":

            return True

        # =================================
        # AI CITATION ANALYSIS
        # =================================

        if node_name == "ai_citation_analysis":

            geo_findings = [

                item

                for item in shared_memory

                if "AI discoverability"
                in item["finding"]
            ]

            return len(geo_findings) > 0

        # =================================
        # PRIORITY ENGINE
        # =================================

        if node_name == "priority_engine":

            competitor_findings = [

                item

                for item in shared_memory

                if "Competitors"
                in item["finding"]
            ]

            return len(competitor_findings) > 0

        # =================================
        # DEFAULT
        # =================================

        return True