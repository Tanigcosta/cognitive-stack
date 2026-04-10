from ..core.clusters import COMPRESS, EXTRACT, SYNTHESIZE
from ..core.contracts import ACTION_LIST, MARKDOWN_BRIEF
from ..core.policies import ACTIONABLE, BUSINESS_TONE, NO_FLUFF, NO_HALLUCINATION
from ..core.types import PromptContext, PromptSpec


INTENT_CLASSIFICATION_STACK = PromptSpec(
    name="stack.copilot.intent_classification.v1",
    version="1.0.0",
    intent="Classify what the user is trying to do in a Copilot experience.",
    clusters=[EXTRACT, COMPRESS],
    policies=[NO_HALLUCINATION, NO_FLUFF],
    output_contract=ACTION_LIST,
    context=PromptContext(
        task="Classify whether the user wants to ask, summarize, analyze, draft, extract actions, or trigger a workflow.",
        audience="assistant orchestration layer",
    ),
    tags=["copilot", "classification"],
)

CONTEXT_SHAPING_STACK = PromptSpec(
    name="stack.copilot.context_shaping.v1",
    version="1.0.0",
    intent="Prepare retrieved context for a Copilot answer.",
    clusters=[EXTRACT, COMPRESS],
    policies=[NO_HALLUCINATION, NO_FLUFF],
    output_contract=MARKDOWN_BRIEF,
    context=PromptContext(
        task="Extract the relevant facts, missing facts, contradictions, and confidence level from the provided context.",
        audience="assistant orchestration layer",
    ),
    tags=["copilot", "context"],
)

ANSWER_GENERATION_STACK = PromptSpec(
    name="stack.copilot.answer_generation.v1",
    version="1.0.0",
    intent="Generate a final assistant answer in a business setting.",
    clusters=[SYNTHESIZE, COMPRESS],
    policies=[NO_HALLUCINATION, BUSINESS_TONE, ACTIONABLE, NO_FLUFF],
    output_contract=MARKDOWN_BRIEF,
    context=PromptContext(
        task="Generate a clear final answer based on the shaped context and user request.",
        audience="end user",
    ),
    tags=["copilot", "answer"],
)
