from pydantic import BaseModel, Field
from typing import Literal


class ClaimAssessment(BaseModel):
    """Structured output for a preliminary insurance claim assessment."""

    claim_id: str = Field(
        description="Unique identifier of the insurance claim."
    )

    claim_type: Literal["Auto", "Home"] = Field(
        description="Type of insurance claim."
    )

    claim_amount: float = Field(
        gt=0,
        description="Claimed monetary amount, which must be positive."
    )

    status: str = Field(
        description="Current status of the claim in the source data."
    )

    key_facts: list[str] = Field(
        description="Important facts retrieved from the claim record."
    )

    missing_information: list[str] = Field(
        description="Information that is missing or needs verification."
    )

    preliminary_assessment: str = Field(
        description="Evidence-based preliminary assessment of the claim."
    )

    requires_human_review: bool = Field(
        description="Whether the claim needs further review by a human."
    )

    final_decision: Literal["Not made"] = Field(
        description="Must remain Not made; the AI must not make a final coverage or payment decision."
    )
