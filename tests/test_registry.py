from prompt_architecture.core.clusters import EXTRACT
from prompt_architecture.core.policies import NO_HALLUCINATION
from prompt_architecture.core.registry import ClusterRegistry, PolicyRegistry, StackRegistry
from prompt_architecture.stacks.enterprise import USECASE_ASSESSMENT_STACK


def test_cluster_registry_register_and_get() -> None:
    registry = ClusterRegistry()
    registry.register(EXTRACT)
    assert registry.get("extract").name == "extract"


def test_policy_registry_register_and_get() -> None:
    registry = PolicyRegistry()
    registry.register(NO_HALLUCINATION)
    assert registry.get("no_hallucination").name == "no_hallucination"


def test_stack_registry_register_and_get() -> None:
    registry = StackRegistry()
    registry.register(USECASE_ASSESSMENT_STACK)
    assert registry.get(USECASE_ASSESSMENT_STACK.name).name == USECASE_ASSESSMENT_STACK.name
