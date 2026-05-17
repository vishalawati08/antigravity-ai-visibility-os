# =========================================
# RECURSIVE REFINEMENT ENGINE
# =========================================

class RecursiveRefinementEngine:

    def should_refine(

        self,

        reflections
    ):

        for item in reflections:

            issue = item["issue"]

            if issue != "Execution quality strong":

                return True

        return False

    # =====================================
    # GENERATE REFINEMENT ACTIONS
    # =====================================

    def generate_refinements(

        self,

        reflections
    ):

        actions = []

        for item in reflections:

            issue = item["issue"]

            if issue == "Limited execution depth":

                actions.append(

                    "Expand orchestration graph "
                    "with additional reasoning stages."
                )

            elif issue == "Low agent collaboration":

                actions.append(

                    "Increase shared memory "
                    "coordination across agents."
                )

            elif issue == "Weak shared intelligence":

                actions.append(

                    "Encourage deeper collaborative "
                    "reasoning across workflows."
                )

        return actions