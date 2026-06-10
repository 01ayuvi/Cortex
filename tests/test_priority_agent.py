from graph.nodes import priority_agent


def test_high_priority():
    result = priority_agent(
        {
            "email_text": "URGENT security issue"
        }
    )

    assert result["priority"] == "HIGH"


def test_low_priority():
    result = priority_agent(
        {
            "email_text": "Weekly team update"
        }
    )

    assert result["priority"] == "LOW"