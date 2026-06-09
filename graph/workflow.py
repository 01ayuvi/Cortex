from langgraph.graph import StateGraph

from graph.state import CortexState
from graph.nodes import (
    email_agent,
    task_agent
)

from graph.nodes import (
    email_agent,
    task_agent,
    priority_agent
)
workflow = StateGraph(
    CortexState
)

workflow.add_node(
    "email_agent",
    email_agent
)

workflow.add_node(
    "task_agent",
    task_agent
)

workflow.set_entry_point(
    "email_agent"
)

workflow.add_edge(
    "email_agent",
    "task_agent"
)

workflow.add_node(
    "priority_agent",
    priority_agent
)
workflow.add_edge(
    "task_agent",
    "priority_agent"
)
app = workflow.compile()