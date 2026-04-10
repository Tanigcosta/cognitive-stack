from prompt_architecture.core.pipeline import PipelineRunner
from prompt_architecture.core.runtime import PromptRuntime
from prompt_architecture.core.types import Pipeline, PipelineStep
from prompt_architecture.stacks.enterprise import REQUIREMENTS_EXTRACTION_STACK, USECASE_ASSESSMENT_STACK


VALID_JSON = '{"summary": "high value", "options": ["pilot"], "risks": ["quality drift"], "recommendation": "Proceed with a human-in-the-loop pilot."}'
VALID_MD = "Summary\n\nKey Points\n\nRecommendation"


def test_pipeline_runner_executes_all_steps() -> None:
    outputs = iter([VALID_MD, VALID_JSON])
    runtime = PromptRuntime(llm_call=lambda _prompt: next(outputs))
    pipeline = Pipeline(
        name="enterprise_decision_flow",
        steps=[
            PipelineStep(name="extract_requirements", spec=REQUIREMENTS_EXTRACTION_STACK, output_key="requirements"),
            PipelineStep(name="assess_usecase", spec=USECASE_ASSESSMENT_STACK, output_key="decision"),
        ],
    )

    results = PipelineRunner(runtime).run(pipeline)
    assert set(results.keys()) == {"requirements", "decision"}
    assert results["requirements"].valid is True
    assert results["decision"].valid is True
