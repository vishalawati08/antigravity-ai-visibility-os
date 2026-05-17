from tools.agent_registry import (
    get_agent_registry
)

from tools.shared_memory_bus import (
    SharedMemoryBus
)


# =========================================
# AGENT EXECUTION ENGINE
# =========================================

class AgentExecutor:

    def __init__(self):

        self.agents = (
            get_agent_registry()
        )

        self.memory_bus = (
            SharedMemoryBus()
        )

    # =====================================
    # ASSIGN AGENT
    # =====================================

    def assign_agent(self, node_name):

        mapping = {

            "technical_analysis":
                "technical_seo_agent",

            "geo_analysis":
                "geo_intelligence_agent",

            "competitor_analysis":
                "competitor_agent",

            "recommendation_engine":
                "recommendation_agent"
        }

        return mapping.get(node_name)

    # =====================================
    # GENERATE FINDING
    # =====================================

    def generate_finding(

        self,

        node_name,

        role
    ):

        findings = {

            "technical_analysis":

                (
                    "Technical SEO weaknesses "
                    "may reduce search crawlability."
                ),

            "geo_analysis":

                (
                    "AI discoverability signals "
                    "indicate weak answer-engine readiness."
                ),

            "competitor_analysis":

                (
                    "Competitors demonstrate "
                    "stronger semantic positioning."
                ),

            "recommendation_engine":

                (
                    "Strategic visibility improvements "
                    "should prioritize GEO optimization."
                )
        }

        return findings.get(

            node_name,

            "Workflow execution completed."
        )

    # =====================================
    # EXECUTE AGENT TASK
    # =====================================

    def execute(self, node_name):

        agent_id = self.assign_agent(
            node_name
        )

        # =================================
        # SYSTEM EXECUTION
        # =================================

        if not agent_id:

            return {

                "node":
                    node_name,

                "agent":
                    "system",

                "status":
                    "completed"
            }

        # =================================
        # AGENT LOOKUP
        # =================================

        agent = self.agents[agent_id]

        # =================================
        # READ SHARED MEMORY
        # =================================

        shared_memory = (
            self.memory_bus.get_all()
        )

        # =================================
        # GENERATE FINDING
        # =================================

        finding = self.generate_finding(

            node_name,

            agent["role"]
        )

        # =================================
        # PUBLISH FINDING
        # =================================

        self.memory_bus.publish(

            agent["role"],

            finding
        )

        # =================================
        # RETURN EXECUTION RESULT
        # =================================

        return {

            "node":
                node_name,

            "agent":
                agent["role"],

            "objective":
                agent["objective"],

            "shared_memory":
                shared_memory,

            "finding":
                finding,

            "status":
                "completed"
        }