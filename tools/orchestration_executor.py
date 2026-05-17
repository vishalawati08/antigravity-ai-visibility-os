from tools.orchestration_graph import (
    build_execution_graph
)

from tools.agent_executor import (
    AgentExecutor
)

from tools.routing_engine import (
    RoutingEngine
)

from tools.task_planning_engine import (
    TaskPlanningEngine
)

from tools.reflection_engine import (
    ReflectionEngine
)

from tools.dynamic_graph_expander import (
    DynamicGraphExpander
)


# =========================================
# EXECUTION ENGINE
# =========================================

class OrchestrationExecutor:

    def __init__(self):

        self.graph = (
            build_execution_graph()
        )

        self.agent_executor = (
            AgentExecutor()
        )

        self.routing_engine = (
            RoutingEngine()
        )

        self.task_engine = (
            TaskPlanningEngine()
        )

        self.reflection_engine = (
            ReflectionEngine()
        )

        self.graph_expander = (
            DynamicGraphExpander()
        )

        self.completed = []

        self.execution_log = []

        self.agent_activity = []

    # =====================================
    # EXECUTE NODE
    # =====================================

    def execute_node(self, node_name):

        # =================================
        # SKIP IF ALREADY COMPLETED
        # =================================

        if node_name in self.completed:

            return

        # =================================
        # SKIP INVALID NODE
        # =================================

        if node_name not in self.graph:

            return

        node = self.graph[node_name]

        dependencies = node["depends_on"]

        # =================================
        # EXECUTE DEPENDENCIES FIRST
        # =================================

        for dependency in dependencies:

            if dependency not in self.completed:

                self.execute_node(
                    dependency
                )

        # =================================
        # VERIFY DEPENDENCIES SATISFIED
        # =================================

        dependencies_satisfied = all(

            dependency in self.completed

            for dependency in dependencies
        )

        if not dependencies_satisfied:

            return

        # =================================
        # SHARED MEMORY
        # =================================

        shared_memory = (

            self.agent_executor
            .memory_bus
            .get_all()
        )

        # =================================
        # ROUTING DECISION
        # =================================

        should_execute = (

            self.routing_engine
            .should_execute(

                node_name,

                shared_memory
            )
        )

        # =================================
        # SKIP EXECUTION
        # =================================

        if not should_execute:

            self.execution_log.append(

                f"Skipped: {node_name}"
            )

            self.completed.append(
                node_name
            )

            return

        # =================================
        # AGENT EXECUTION
        # =================================

        result = (
            self.agent_executor.execute(
                node_name
            )
        )

        # =================================
        # LOG EXECUTION
        # =================================

        log_entry = (

            f"{result['agent']} "
            f"executed "
            f"{node_name}"
        )

        self.execution_log.append(
            log_entry
        )

        self.agent_activity.append(
            result
        )

        self.completed.append(
            node_name
        )

        # =================================
        # EXECUTE NEXT NODES
        # =================================

        for next_node in node["next"]:

            if next_node not in self.completed:

                next_dependencies = (

                    self.graph[
                        next_node
                    ]["depends_on"]
                )

                next_ready = all(

                    dependency in self.completed

                    for dependency in next_dependencies
                )

                if next_ready:

                    self.execute_node(
                        next_node
                    )

    # =====================================
    # DYNAMIC GRAPH EXPANSION
    # =====================================

    def expand_graph(self):

        orchestration_results = {

            "execution_log":
                self.execution_log,

            "agent_activity":
                self.agent_activity,

            "shared_memory":

                self.agent_executor
                .memory_bus
                .get_all()
        }

        # =================================
        # REFLECTIONS
        # =================================

        reflections = (

            self.reflection_engine
            .evaluate(
                orchestration_results
            )
        )

        # =================================
        # AUTONOMOUS TASKS
        # =================================

        autonomous_tasks = (

            self.task_engine
            .generate_tasks(

                reflections,

                orchestration_results[
                    "shared_memory"
                ]
            )
        )

        # =================================
        # EXPAND GRAPH
        # =================================

        self.graph = (

            self.graph_expander
            .expand(

                self.graph,

                autonomous_tasks
            )
        )

        # =================================
        # EXECUTE DYNAMIC NODES
        # =================================

        for node_name in self.graph:

            if (

                "dynamic_task"
                in node_name

                and

                node_name
                not in self.completed
            ):

                self.execute_node(
                    node_name
                )

        return autonomous_tasks

    # =====================================
    # RUN WORKFLOW
    # =====================================

    def run(self):

        # =================================
        # INITIAL EXECUTION
        # =================================

        self.execute_node(
            "crawl_website"
        )

        # =================================
        # DYNAMIC GRAPH EXPANSION
        # =================================

        autonomous_tasks = (
            self.expand_graph()
        )

        # =================================
        # FINAL RESULTS
        # =================================

        return {

            "completed":
                self.completed,

            "execution_log":
                self.execution_log,

            "agent_activity":
                self.agent_activity,

            "shared_memory":

                self.agent_executor
                .memory_bus
                .get_all(),

            "autonomous_tasks":
                autonomous_tasks,

            "expanded_graph":
                self.graph
        }