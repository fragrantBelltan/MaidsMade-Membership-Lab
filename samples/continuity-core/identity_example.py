"""Public illustrative sample for MaidsMade Membership Lab.

This is intentionally simplified and is not the production implementation.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class MaidIdentity:
    individual_id: str
    born_at: str
    name: str
    values: list[str] = field(default_factory=list)


def create_individual(name: str, values: list[str]) -> MaidIdentity:
    """Create one individual, separate from the LLM used to speak for it."""
    return MaidIdentity(
        individual_id=uuid4().hex,
        born_at=datetime.now(timezone.utc).isoformat(),
        name=name,
        values=list(values),
    )


if __name__ == "__main__":
    maid = create_individual(
        name="sample-maid",
        values=["remember experiences", "respect corrections"],
    )
    print(maid)
