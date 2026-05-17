import json
import os


# =========================================
# PERSISTENT MEMORY ENGINE
# =========================================

class PersistentMemory:

    def __init__(self):

        self.memory_file = (
            "persistent_memory.json"
        )

        self.memory = (
            self.load_memory()
        )

    # =====================================
    # LOAD MEMORY
    # =====================================

    def load_memory(self):

        if not os.path.exists(
            self.memory_file
        ):

            return []

        try:

            with open(

                self.memory_file,

                "r",

                encoding="utf-8"

            ) as file:

                return json.load(file)

        except Exception:

            return []

    # =====================================
    # SAVE MEMORY
    # =====================================

    def save_memory(self):

        with open(

            self.memory_file,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.memory,

                file,

                indent=4
            )

    # =====================================
    # STORE EXECUTION
    # =====================================

    def store_execution(

        self,

        orchestration_results
    ):

        self.memory.append({

            "execution_log":

                orchestration_results[
                    "execution_log"
                ],

            "shared_memory":

                orchestration_results[
                    "shared_memory"
                ]
        })

        self.save_memory()

    # =====================================
    # GET HISTORY
    # =====================================

    def get_history(self):

        return self.memory