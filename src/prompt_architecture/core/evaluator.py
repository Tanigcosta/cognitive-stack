from dataclasses import dataclass


@dataclass
class EvalResult:
    clarity: int
    structure: int
    faithfulness: int
    usefulness: int
    variance: int
    notes: str = ""
