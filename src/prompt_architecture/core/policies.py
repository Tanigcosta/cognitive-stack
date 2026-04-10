from .types import Policy


NO_HALLUCINATION = Policy(
    name="no_hallucination",
    instruction="Do not invent facts, references, or missing inputs. State uncertainty explicitly.",
)

BUSINESS_TONE = Policy(
    name="business_tone",
    instruction="Use a professional, direct, and credible tone.",
)

ACTIONABLE = Policy(
    name="actionable",
    instruction="Prefer concrete recommendations, decisions, and next actions.",
)

NO_FLUFF = Policy(
    name="no_fluff",
    instruction="Avoid filler, generic language, and repetition.",
)
