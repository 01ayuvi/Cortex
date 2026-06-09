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