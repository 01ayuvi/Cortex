from graph.workflow import app

result = app.invoke(
    {
        "email_text":
        """
        URGENT:
        Submit the performance report
        by Friday.
        """
    }
)

print(result)