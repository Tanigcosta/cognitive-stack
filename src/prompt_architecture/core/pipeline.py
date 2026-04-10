from typing import Dict

from .runtime import PromptRuntime
from .types import Pipeline, RuntimeResult


class PipelineRunner:
    def __init__(self, runtime: PromptRuntime):
        self.runtime = runtime

    def run(self, pipeline: Pipeline) -> Dict[str, RuntimeResult]:
        results: Dict[str, RuntimeResult] = {}
        for step in pipeline.steps:
            results[step.output_key] = self.runtime.run_spec(step.spec)
        return results
