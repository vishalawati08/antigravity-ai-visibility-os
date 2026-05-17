# =========================================
# TASK PLANNING ENGINE
# =========================================

class TaskPlanningEngine:

    def generate_tasks(

        self,

        reflections,

        shared_memory
    ):

        tasks = []

        # =================================
        # REFLECTION-BASED TASKS
        # =================================

        for item in reflections:

            issue = item["issue"]

            if issue == "Limited execution depth":

                tasks.append({

                    "task":
                        (
                            "Expand strategic "
                            "research coverage"
                        ),

                    "priority":
                        "High"
                })

            elif issue == "Low agent collaboration":

                tasks.append({

                    "task":
                        (
                            "Increase inter-agent "
                            "coordination"
                        ),

                    "priority":
                        "Medium"
                })

        # =================================
        # MEMORY-BASED TASKS
        # =================================

        for memory in shared_memory:

            finding = memory["finding"]

            if "crawlability" in finding:

                tasks.append({

                    "task":
                        (
                            "Perform advanced "
                            "technical SEO audit"
                        ),

                    "priority":
                        "High"
                })

            if "AI discoverability" in finding:

                tasks.append({

                    "task":
                        (
                            "Expand GEO/AEO "
                            "optimization analysis"
                        ),

                    "priority":
                        "Critical"
                })

        return tasks