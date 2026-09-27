"""Generic public example for an identity/continuity architecture.

This sample is intentionally simplified and contains no production identity,
character name, user data, or internal implementation detail.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class AgentIdentity:
    individual_id: str
    created_at: str
    display_name: str
    values: list[str] = field(default_factory=list)


def create_individual(display_name: str, values: list[str]) -> AgentIdentity:
    """Create one continuing individual independently from any specific LLM."""
    return AgentIdentity(
        individual_id=uuid4().hex,
        created_at=datetime.now(timezone.utc).isoformat(),
        display_name=display_name,
        values=list(values),
    )


if __name__ == "__main__":
    agent = create_individual(
        display_name="sample-agent",
        values=["preserve experience", "respect corrections"],
    )
    print(agent)
