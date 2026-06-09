from langgraph.graph import StateGraph

from graph.state import CortexState
from graph.nodes import (
    supervisor_agent,
    email_agent,
    task_agent,
    priority_agent,
    briefing_agent
)

workflow = StateGraph(CortexState)


def route_email(state):

    return state["route"]


# Nodes
workflow.add_node(
    "supervisor_agent",
    supervisor_agent
)

workflow.add_node(
    "email_agent",
    email_agent
)

workflow.add_node(
    "task_agent",
    task_agent
)

workflow.add_node(
    "priority_agent",
    priority_agent
)

workflow.add_node(
    "briefing_agent",
    briefing_agent
)


# Entry Point
workflow.set_entry_point(
    "supervisor_agent"
)


# Conditional Routing
workflow.add_conditional_edges(
    "supervisor_agent",
    route_email,
    {
        "task": "email_agent",
        "priority": "priority_agent",
        "ignore": "__end__"
    }
)


# Linear Flow
workflow.add_edge(
    "email_agent",
    "task_agent"
)

workflow.add_edge(
    "task_agent",
    "priority_agent"
)

workflow.add_edge(
    "priority_agent",
    "briefing_agent"
)


# Compile Graph
app = workflow.compile()