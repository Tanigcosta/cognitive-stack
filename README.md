# 🧠 Cognitive Stack

> A modular framework for designing and scaling LLM cognitive systems.

---

## Why this exists

Most organisations approach LLMs as a tooling problem.

They experiment with prompts.  
They test use cases.  
They build isolated copilots or automations.

But as soon as they try to scale, the same issues appear:

- inconsistent outputs  
- fragile prompt logic  
- lack of governance  
- no clear way to reuse what works  
- difficulty aligning AI with real business workflows  

The challenge isn’t adoption.

It’s **architecture**.

---

## A different perspective

LLMs are not traditional software components.  
They don’t execute deterministic logic.

They operate by activating learned patterns —  
what we can think of as **latent cognitive behaviours**.

This means:

> You don’t control an LLM.  
> You **shape how it thinks**.

Cognitive Stack is built around that idea.

---

## What this framework does

Cognitive Stack introduces a structured way to design LLM-based systems:

- **Cognitive Clusters**  
  Reusable behaviour modules (e.g. reasoning, critique, extraction, planning)

- **Policies**  
  Guardrails for reliability, tone, and governance

- **Stacks**  
  Composed cognitive patterns aligned to real business tasks

- **Pipelines**  
  Multi-step reasoning flows that mirror how decisions are actually made

This moves LLM usage from isolated prompts to **composable system design**.

---

## From prompting to architecture

Most prompt engineering focuses on:

> “How do I get a better answer?”

Cognitive Stack focuses on:

> “How do I design a reliable cognitive workflow?”

That shift enables:

- predictable behaviour across use cases  
- reusable design patterns  
- clearer separation between logic, constraints, and outputs  
- alignment with enterprise requirements (auditability, control, scalability)

---

## Where this fits in enterprise AI

This framework is designed to sit between:

- **business workflows**  
- **LLM capabilities**  
- **AI platforms (Copilot, APIs, agent frameworks)**  

It provides a missing layer:

> A **design abstraction** for building reliable AI systems.

---

## Example applications

Cognitive Stack is particularly suited for:

- **AI opportunity assessment**  
  Structuring how organisations evaluate and prioritise GenAI use cases  

- **Copilot design**  
  Separating intent detection, context shaping, and response generation  

- **Agent workflows**  
  Designing multi-step, tool-augmented reasoning pipelines  

- **Decision support systems**  
  Making reasoning explicit, auditable, and structured  

---

## Design principles

- **Separate behaviour from constraints**  
- **Compose, don’t monolithically prompt**  
- **Make outputs contract-driven**  
- **Design for variability, not determinism**  
- **Treat reasoning as a system, not a side-effect**

---

## What this repository provides

- A lightweight SDK (Python-first)  
- A reusable library of cognitive clusters and policies  
- Predefined stacks for enterprise use cases  
- Pipeline patterns for multi-step reasoning  
- A foundation for building scalable LLM systems  

---

## Why this matters

As LLM adoption matures, the limiting factor is no longer access to models.

It’s the ability to design systems that are:

- reliable  
- interpretable  
- reusable  
- aligned with business value  

Cognitive Stack is an attempt to formalise that layer.

---

## Author’s perspective

This framework reflects hands-on experience designing enterprise AI solutions at the intersection of:

- data platforms  
- automation  
- and Generative AI systems  

It is intended as both a practical toolkit and a design approach for building **production-grade AI systems**.

---

## Final thought

The shift happening now is subtle but important:

We are moving from  
**using AI tools**  

to  
**designing AI systems**.

Cognitive Stack sits in that transition.

---

## License

This project is licensed under the Apache 2.0.
=======
# Prompt Architecture Starter Kit

A production-style starter kit for treating prompts as reusable **cognitive infrastructure** rather than one-off strings.

This repository gives you:

- reusable **clusters** for behavior activation
- reusable **policies** for stable constraints
- **output contracts** and validators
- **prompt specs** as the main unit of design
- **pipelines** for multi-step reasoning
- **registries** for reuse and versioning
- example enterprise stacks for:
  - opportunity assessment
  - Copilot / assistant design
  - agent workflow design
- tests you can extend in real projects

## Why this exists

Most teams still treat prompt engineering as handcrafted prompt writing.

This starter kit assumes a different operating model:

- **clusters** = reusable behavior modules
- **policies** = reusable guardrails
- **stacks** = reusable prompt compositions
- **pipelines** = reusable cognitive flows

That shift makes prompting more testable, maintainable, and team-friendly.

## Repository structure

```text
prompt-architecture-starter/
  pyproject.toml
  README.md
  src/
    prompt_architecture/
      __init__.py
      core/
        __init__.py
        types.py
        clusters.py
        policies.py
        contracts.py
        builder.py
        registry.py
        runtime.py
        pipeline.py
        evaluator.py
      stacks/
        __init__.py
        enterprise.py
        copilot.py
        agents.py
      routers/
        __init__.py
        task_router.py
  tests/
    test_builder.py
    test_registry.py
    test_runtime.py
    test_pipeline.py
    test_stacks.py
```

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install in editable mode

```bash
pip install -e .
```

### 3. Run tests

```bash
pip install pytest
pytest
```

## Core concepts

### Cluster
A reusable behavior trigger.

Examples:
- extract requirements
- critique assumptions
- synthesize findings
- compress output
- force JSON-only output

### Policy
A stable constraint that should remain true regardless of task.

Examples:
- do not hallucinate
- use business tone
- avoid fluff
- be actionable

### Output contract
A target output shape and optional validator.

Examples:
- markdown summary with fixed headings
- JSON decision schema
- action list only

### Prompt spec
The main design unit.

A `PromptSpec` combines:
- intent
- clusters
- policies
- output contract
- task context

### Pipeline
A sequence of prompt specs used as separate reasoning stages.

Examples:
- discover -> critique -> decide
- classify intent -> shape context -> answer
- decompose task -> select tool -> self-review

## Example: build a prompt from a stack

```python
from prompt_architecture.core.builder import PromptBuilder
from prompt_architecture.stacks.enterprise import USECASE_ASSESSMENT_STACK

prompt = PromptBuilder().build(USECASE_ASSESSMENT_STACK)
print(prompt)
```

## Example: run a stack with a mock LLM

```python
from prompt_architecture.core.runtime import PromptRuntime
from prompt_architecture.stacks.enterprise import USECASE_ASSESSMENT_STACK


def mock_llm(prompt: str) -> str:
    return '{"summary": "feasible", "options": ["pilot"], "risks": ["quality drift"], "recommendation": "Proceed with a human-in-the-loop pilot."}'

runtime = PromptRuntime(llm_call=mock_llm)
result = runtime.run_spec(USECASE_ASSESSMENT_STACK)

print(result.valid)
print(result.output)
```

## Example stacks included

### Enterprise
- `stack.enterprise.usecase_intake.v1`
- `stack.enterprise.usecase_assessment.v1`
- `stack.enterprise.requirements_extraction.v1`

### Copilot
- `stack.copilot.intent_classification.v1`
- `stack.copilot.context_shaping.v1`
- `stack.copilot.answer_generation.v1`

### Agents
- `stack.agents.task_decomposition.v1`
- `stack.agents.tool_selection.v1`
- `stack.agents.self_review.v1`

## Suggested next extensions

- add Pydantic validators for structured outputs
- add telemetry for stack version, latency, repairs, and user feedback
- add model-specific routing by task type
- add evaluation harnesses for variance and quality scoring
- add retrieval-aware context shaping for RAG systems
- add policy packs for governance-sensitive enterprise use cases

## Design rules

1. Keep clusters small and single-purpose.
2. Separate behavior from policy.
3. Treat output as a contract.
4. Prefer pipelines over giant prompts.
5. Version stacks and route by task type.
6. Test for stability, not just elegance.

## License

Add your preferred license before publishing.
>>>>>>> 9d3a9e6 (Initial commit)
