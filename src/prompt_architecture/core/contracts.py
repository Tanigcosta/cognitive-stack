import json

from .types import OutputContract


def non_empty(output: str) -> bool:
    return bool(output and output.strip())


def valid_json(output: str) -> bool:
    try:
        json.loads(output)
        return True
    except (TypeError, json.JSONDecodeError):
        return False


MARKDOWN_BRIEF = OutputContract(
    format_name="markdown_brief",
    instruction="Return markdown with sections: Summary, Key Points, Recommendation.",
    validator=non_empty,
)

JSON_DECISION = OutputContract(
    format_name="json_decision",
    instruction='Return valid JSON with keys: "summary", "options", "risks", "recommendation".',
    validator=valid_json,
)

ACTION_LIST = OutputContract(
    format_name="action_list",
    instruction="Return a concise action list with clear next steps.",
    validator=non_empty,
)
