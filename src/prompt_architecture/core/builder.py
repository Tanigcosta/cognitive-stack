from .types import PromptSpec


class PromptBuilder:
    def build(self, spec: PromptSpec) -> str:
        parts = []
        parts.append(f"Task intent: {spec.intent}")

        if spec.context.background:
            parts.append("Background:")
            parts.append(spec.context.background)

        if spec.context.audience:
            parts.append(f"Audience: {spec.context.audience}")

        parts.append("Task:")
        parts.append(spec.context.task)

        if spec.context.inputs:
            parts.append("Inputs:")
            for key, value in spec.context.inputs.items():
                parts.append(f"- {key}: {value}")

        if spec.clusters:
            parts.append("Behavior modules:")
            for cluster in spec.clusters:
                parts.append(f"- {cluster.instruction}")

        if spec.policies:
            parts.append("Policies:")
            for policy in spec.policies:
                parts.append(f"- {policy.instruction}")

        parts.append("Output contract:")
        parts.append(spec.output_contract.instruction)

        return "\n".join(parts)
