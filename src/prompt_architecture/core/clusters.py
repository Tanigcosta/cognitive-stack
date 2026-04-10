from .types import Cluster


EXTRACT = Cluster(
    name="extract",
    instruction="Identify the key entities, variables, constraints, dependencies, and unknowns.",
    purpose="signal extraction",
    tags=["analysis", "requirements"],
)

PLAN = Cluster(
    name="plan",
    instruction="Create a clear plan before attempting the answer.",
    purpose="planning",
    tags=["planning"],
)

CRITIQUE = Cluster(
    name="critique",
    instruction="Critically evaluate assumptions, risks, edge cases, and weaknesses before finalizing.",
    purpose="adversarial review",
    tags=["risk", "review"],
)

SYNTHESIZE = Cluster(
    name="synthesize",
    instruction="Combine the strongest findings into a coherent final answer.",
    purpose="integration",
    tags=["synthesis"],
)

COMPRESS = Cluster(
    name="compress",
    instruction="Use concise wording, high information density, and minimal redundancy.",
    purpose="brevity",
    tags=["brevity"],
)

TEACH = Cluster(
    name="teach",
    instruction="Explain clearly using simple language and layered structure.",
    purpose="pedagogical mode",
    tags=["education", "clarity"],
)

JSON_ONLY = Cluster(
    name="json_only",
    instruction="Return only valid JSON that matches the requested schema.",
    purpose="structured output",
    tags=["format", "json"],
)
