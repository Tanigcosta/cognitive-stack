from typing import Callable

from .builder import PromptBuilder
from .types import PromptSpec, RuntimeResult


class PromptRuntime:
    def __init__(self, llm_call: Callable[[str], str]):
        self.llm_call = llm_call
        self.builder = PromptBuilder()

    def run_spec(self, spec: PromptSpec) -> RuntimeResult:
        prompt = self.builder.build(spec)
        output = self.llm_call(prompt)

        validator = spec.output_contract.validator
        valid = validator(output) if validator else True
        repaired = False

        if not valid:
            repaired = True
            repair_prompt = (
                prompt
                + "\n\nThe previous answer did not satisfy the output contract. "
                + "Regenerate it so it strictly matches the output contract."
            )
            output = self.llm_call(repair_prompt)
            valid = validator(output) if validator else True

        return RuntimeResult(
            prompt=prompt,
            output=output,
            valid=valid,
            repaired=repaired,
        )
