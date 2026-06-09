from agents.task_agent import extract_task


def supervisor_agent(state):

    email = state["email_text"].lower()

    if "security" in email:

        route = "priority"

    elif "newsletter" in email:

        route = "ignore"

    else:

        route = "task"

    return {
        "route": route
    }


def email_agent(state):

    email = state["email_text"]

    return {
        "summary": email[:200]
    }


def task_agent(state):

    email = state["email_text"]

    task_data = extract_task(email)

    return {
        "task_data": task_data
    }


def priority_agent(state):

    email = state["email_text"].lower()

    priority = "LOW"

    urgent_keywords = [
        "urgent",
        "asap",
        "immediately",
        "security",
        "deadline",
        "critical"
    ]

    for keyword in urgent_keywords:

        if keyword in email:

            priority = "HIGH"
            break

    return {
        "priority": priority
    }