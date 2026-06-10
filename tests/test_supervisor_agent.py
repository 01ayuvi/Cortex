from graph.nodes import supervisor_agent


def test_security_route():

    result = supervisor_agent(
        {
            "email_text":
            "Security alert detected"
        }
    )

    assert result["route"] == "priority"


def test_newsletter_route():

    result = supervisor_agent(
        {
            "email_text":
            "Monthly newsletter"
        }
    )

    assert result["route"] == "ignore"


def test_task_route():

    result = supervisor_agent(
        {
            "email_text":
            "Submit report by Friday"
        }
    )

    assert result["route"] == "task"