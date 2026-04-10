from prompt_architecture.core.runtime import PromptRuntime
from prompt_architecture.stacks.enterprise import USECASE_ASSESSMENT_STACK


VALID_JSON = '{"summary": "high value", "options": ["pilot"], "risks": ["quality drift"], "recommendation": "Proceed with a human-in-the-loop pilot."}'


def test_runtime_returns_valid_result() -> None:
    runtime = PromptRuntime(llm_call=lambda _prompt: VALID_JSON)
    result = runtime.run_spec(USECASE_ASSESSMENT_STACK)
    assert result.valid is True
    assert result.repaired is False


def test_runtime_repairs_invalid_result() -> None:
    calls = iter(["not json", VALID_JSON])
    runtime = PromptRuntime(llm_call=lambda _prompt: next(calls))
    result = runtime.run_spec(USECASE_ASSESSMENT_STACK)
    assert result.repaired is True
    assert result.valid is True
