TASK_ROUTE_MAP = {
    "usecase_intake": "stack.enterprise.usecase_intake.v1",
    "usecase_assessment": "stack.enterprise.usecase_assessment.v1",
    "requirements_extraction": "stack.enterprise.requirements_extraction.v1",
    "copilot_intent_classification": "stack.copilot.intent_classification.v1",
    "copilot_context_shaping": "stack.copilot.context_shaping.v1",
    "copilot_answer_generation": "stack.copilot.answer_generation.v1",
    "agent_task_decomposition": "stack.agents.task_decomposition.v1",
    "agent_tool_selection": "stack.agents.tool_selection.v1",
    "agent_self_review": "stack.agents.self_review.v1",
}


def route_task(task_type: str) -> str:
    return TASK_ROUTE_MAP[task_type]
