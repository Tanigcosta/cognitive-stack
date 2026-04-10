from prompt_architecture.core.builder import PromptBuilder
from prompt_architecture.stacks.enterprise import USECASE_ASSESSMENT_STACK


def test_builder_generates_expected_sections() -> None:
    prompt = PromptBuilder().build(USECASE_ASSESSMENT_STACK)
    assert "Task intent:" in prompt
    assert "Task:" in prompt
    assert "Behavior modules:" in prompt
    assert "Policies:" in prompt
    assert "Output contract:" in prompt
