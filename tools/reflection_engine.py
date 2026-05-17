# =========================================
# REFLECTION ENGINE
# =========================================

class ReflectionEngine:

    def evaluate(

        self,

        orchestration_results
    ):

        reflections = []

        execution_log = (
            orchestration_results[
                "execution_log"
            ]
        )

        # =================================
        # CHECK EXECUTION DEPTH
        # =================================

        if len(execution_log) < 5:

            reflections.append({

                "issue":
                    "Limited execution depth",

                "recommendation":
                    (
                        "Expand orchestration "
                        "coverage for broader "
                        "strategic reasoning."
                    )
            })

        # =================================
        # CHECK AGENT PARTICIPATION
        # =================================

        agents = [

            activity["agent"]

            for activity in orchestration_results[
                "agent_activity"
            ]
        ]

        unique_agents = set(agents)

        if len(unique_agents) < 3:

            reflections.append({

                "issue":
                    "Low agent collaboration",

                "recommendation":
                    (
                        "Increase multi-agent "
                        "coordination across "
                        "research workflows."
                    )
            })

        # =================================
        # CHECK MEMORY DEPTH
        # =================================

        shared_memory = (
            orchestration_results[
                "shared_memory"
            ]
        )

        if len(shared_memory) < 3:

            reflections.append({

                "issue":
                    "Weak shared intelligence",

                "recommendation":
                    (
                        "Encourage stronger "
                        "cross-agent reasoning "
                        "and collaborative analysis."
                    )
            })

        # =================================
        # SUCCESS CASE
        # =================================

        if not reflections:

            reflections.append({

                "issue":
                    "Execution quality strong",

                "recommendation":
                    (
                        "Autonomous orchestration "
                        "demonstrated effective "
                        "multi-agent coordination."
                    )
            })

        return reflections