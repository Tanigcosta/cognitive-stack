from typing import Dict, List

from .types import Cluster, Policy, PromptSpec


class ClusterRegistry:
    def __init__(self) -> None:
        self._clusters: Dict[str, Cluster] = {}

    def register(self, cluster: Cluster) -> None:
        self._clusters[cluster.name] = cluster

    def get(self, name: str) -> Cluster:
        return self._clusters[name]

    def list_by_tag(self, tag: str) -> List[Cluster]:
        return [cluster for cluster in self._clusters.values() if tag in cluster.tags]


class PolicyRegistry:
    def __init__(self) -> None:
        self._policies: Dict[str, Policy] = {}

    def register(self, policy: Policy) -> None:
        self._policies[policy.name] = policy

    def get(self, name: str) -> Policy:
        return self._policies[name]


class StackRegistry:
    def __init__(self) -> None:
        self._stacks: Dict[str, PromptSpec] = {}

    def register(self, spec: PromptSpec) -> None:
        self._stacks[spec.name] = spec

    def get(self, name: str) -> PromptSpec:
        return self._stacks[name]
