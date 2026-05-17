# =========================================
# SHARED MEMORY BUS
# =========================================

class SharedMemoryBus:

    def __init__(self):

        self.memory = []

    # =====================================
    # PUBLISH MEMORY
    # =====================================

    def publish(

        self,

        agent,

        finding
    ):

        self.memory.append({

            "agent":
                agent,

            "finding":
                finding
        })

    # =====================================
    # READ MEMORY
    # =====================================

    def get_all(self):

        return self.memory

    # =====================================
    # FILTER BY AGENT
    # =====================================

    def get_agent_memory(

        self,

        agent_name
    ):

        return [

            item

            for item in self.memory

            if item["agent"] == agent_name
        ]