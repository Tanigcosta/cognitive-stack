from prompt_architecture.stacks.agents import SELF_REVIEW_STACK, TASK_DECOMPOSITION_STACK, TOOL_SELECTION_STACK
from prompt_architecture.stacks.copilot import ANSWER_GENERATION_STACK, CONTEXT_SHAPING_STACK, INTENT_CLASSIFICATION_STACK
from prompt_architecture.stacks.enterprise import REQUIREMENTS_EXTRACTION_STACK, USECASE_ASSESSMENT_STACK, USECASE_INTAKE_STACK


ALL_STACKS = [
    USECASE_INTAKE_STACK,
    USECASE_ASSESSMENT_STACK,
    REQUIREMENTS_EXTRACTION_STACK,
    INTENT_CLASSIFICATION_STACK,
    CONTEXT_SHAPING_STACK,
    ANSWER_GENERATION_STACK,
    TASK_DECOMPOSITION_STACK,
    TOOL_SELECTION_STACK,
    SELF_REVIEW_STACK,
]


def test_stack_names_are_unique() -> None:
    names = [stack.name for stack in ALL_STACKS]
    assert len(names) == len(set(names))


def test_all_stacks_have_intent_and_contract() -> None:
    for stack in ALL_STACKS:
        assert stack.intent
        assert stack.output_contract.format_name
        assert stack.context.task
