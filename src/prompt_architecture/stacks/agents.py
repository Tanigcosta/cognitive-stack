from ..core.clusters import COMPRESS, CRITIQUE, EXTRACT, PLAN, SYNTHESIZE
from ..core.contracts import JSON_DECISION, MARKDOWN_BRIEF
from ..core.policies import ACTIONABLE, NO_FLUFF, NO_HALLUCINATION
from ..core.types import PromptContext, PromptSpec


TASK_DECOMPOSITION_STACK = PromptSpec(
    name="stack.agents.task_decomposition.v1",
    version="1.0.0",
    intent="Decompose a large task into executable subtasks.",
    clusters=[EXTRACT, PLAN, COMPRESS],
    policies=[NO_HALLUCINATION, ACTIONABLE, NO_FLUFF],
    output_contract=MARKDOWN_BRIEF,
    context=PromptContext(
        task="Break the task into sequenced subtasks, dependencies, blockers, and success criteria.",
        audience="agent planner",
    ),
    tags=["agents", "planning"],
)

TOOL_SELECTION_STACK = PromptSpec(
    name="stack.agents.tool_selection.v1",
    version="1.0.0",
    intent="Choose the most appropriate tool for the current step.",
    clusters=[EXTRACT, CRITIQUE, COMPRESS],
    policies=[NO_HALLUCINATION, ACTIONABLE, NO_FLUFF],
    output_contract=JSON_DECISION,
    context=PromptContext(
        task="Select the best tool, explain why, identify required inputs, and define a fallback path.",
        audience="agent executor",
    ),
    tags=["agents", "tools"],
)

SELF_REVIEW_STACK = PromptSpec(
    name="stack.agents.self_review.v1",
    version="1.0.0",
    intent="Review the agent output before returning it.",
    clusters=[CRITIQUE, SYNTHESIZE, COMPRESS],
    policies=[NO_HALLUCINATION, ACTIONABLE, NO_FLUFF],
    output_contract=MARKDOWN_BRIEF,
    context=PromptContext(
        task="Review the output for errors, missing elements, uncertainty, and readiness to return.",
        audience="agent reviewer",
    ),
    tags=["agents", "review"],
)
