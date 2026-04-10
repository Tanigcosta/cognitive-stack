from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class Cluster:
    name: str
    instruction: str
    purpose: str = ""
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Policy:
    name: str
    instruction: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OutputContract:
    format_name: str
    instruction: str
    validator: Optional[Callable[[str], bool]] = None


@dataclass
class PromptContext:
    task: str
    inputs: Dict[str, Any] = field(default_factory=dict)
    background: Optional[str] = None
    audience: Optional[str] = None


@dataclass
class PromptSpec:
    name: str
    intent: str
    clusters: List[Cluster]
    policies: List[Policy]
    output_contract: OutputContract
    context: PromptContext
    version: str = "1.0.0"
    tags: List[str] = field(default_factory=list)


@dataclass
class PipelineStep:
    name: str
    spec: PromptSpec
    output_key: str


@dataclass
class Pipeline:
    name: str
    steps: List[PipelineStep]


@dataclass
class RuntimeResult:
    prompt: str
    output: str
    valid: bool
    repaired: bool = False
