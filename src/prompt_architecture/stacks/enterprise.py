from ..core.clusters import COMPRESS, CRITIQUE, EXTRACT, SYNTHESIZE
from ..core.contracts import JSON_DECISION, MARKDOWN_BRIEF
from ..core.policies import ACTIONABLE, BUSINESS_TONE, NO_FLUFF, NO_HALLUCINATION
from ..core.types import PromptContext, PromptSpec


USECASE_INTAKE_STACK = PromptSpec(
    name="stack.enterprise.usecase_intake.v1",
    version="1.0.0",
    intent="Normalize an enterprise AI request into a clear problem framing.",
    clusters=[EXTRACT, COMPRESS],
    policies=[NO_HALLUCINATION, BUSINESS_TONE, NO_FLUFF],
    output_contract=MARKDOWN_BRIEF,
    context=PromptContext(
        task="Extract the business problem, target users, process touched, expected value, assumptions, and unknowns.",
        audience="AI intake team",
    ),
    tags=["enterprise", "intake"],
)

USECASE_ASSESSMENT_STACK = PromptSpec(
    name="stack.enterprise.usecase_assessment.v1",
    version="1.0.0",
    intent="Assess whether an enterprise AI use case should move to pilot.",
    clusters=[EXTRACT, CRITIQUE, SYNTHESIZE, COMPRESS],
    policies=[NO_HALLUCINATION, BUSINESS_TONE, ACTIONABLE, NO_FLUFF],
    output_contract=JSON_DECISION,
    context=PromptContext(
        task="Evaluate the AI use case for business value, feasibility, data readiness, risk, and implementation priority.",
        audience="AI steering committee",
    ),
    tags=["enterprise", "assessment", "decision"],
)

REQUIREMENTS_EXTRACTION_STACK = PromptSpec(
    name="stack.enterprise.requirements_extraction.v1",
    version="1.0.0",
    intent="Extract business and technical requirements from messy stakeholder input.",
    clusters=[EXTRACT, SYNTHESIZE, COMPRESS],
    policies=[NO_HALLUCINATION, BUSINESS_TONE, NO_FLUFF],
    output_contract=MARKDOWN_BRIEF,
    context=PromptContext(
        task="Read stakeholder notes and extract requirements, assumptions, dependencies, and open questions.",
        audience="product and delivery teams",
    ),
    tags=["enterprise", "requirements"],
)
