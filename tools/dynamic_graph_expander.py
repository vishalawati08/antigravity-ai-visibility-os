# =========================================
# DYNAMIC GRAPH EXPANDER
# =========================================

class DynamicGraphExpander:

    def expand(

        self,

        graph,

        autonomous_tasks
    ):

        expanded_graph = graph.copy()

        # =================================
        # CREATE DYNAMIC TASK NODES
        # =================================

        for index, task in enumerate(

            autonomous_tasks
        ):

            node_name = (
                f"dynamic_task_{index}"
            )

            expanded_graph[node_name] = {

                "depends_on": [

                    "recommendation_engine"
                ],

                "next": [],

                "task":
                    task["task"],

                "priority":
                    task["priority"]
            }

            # =============================
            # CONNECT INTO GRAPH
            # =============================

            if (
                "recommendation_engine"
                in expanded_graph
            ):

                expanded_graph[
                    "recommendation_engine"
                ]["next"].append(
                    node_name
                )

        return expanded_graph