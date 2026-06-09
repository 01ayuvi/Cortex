from typing import TypedDict


class CortexState(TypedDict):

    email_text: str

    summary: str

    task_data: dict

    priority: str

    route: str