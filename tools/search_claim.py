from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class SearchClaimInput(BaseModel):
    claim_id: str = Field(
        ...,
        description="The unique insurance claim ID to search for, such as CLM-1001."
    )


class SearchClaimTool(BaseTool):
    name: str = "search_claim"
    description: str = (
        "Search the mock insurance claims database using a claim ID "
        "and return the claim details."
    )
    args_schema: type[BaseModel] = SearchClaimInput

    def _run(self, claim_id: str) -> str:
        claims = {
            "CLM-1001": {
                "claim_id": "CLM-1001",
                "policy_number": "POL-AUTO-5001",
                "claim_type": "Auto",
                "date_of_loss": "2026-09-15",
                "claim_amount": 12500,
                "status": "Under Review",
                "description": (
                    "The policyholder reported that their vehicle was damaged "
                    "in a collision at an intersection."
                ),
            },
            "CLM-1002": {
                "claim_id": "CLM-1002",
                "policy_number": "POL-HOME-7002",
                "claim_type": "Home",
                "date_of_loss": "2026-09-20",
                "claim_amount": 8750,
                "status": "Submitted",
                "description": (
                    "The policyholder reported water damage inside the home "
                    "following a plumbing incident."
                ),
            },
        }

        claim = claims.get(claim_id.strip().upper())

        if not claim:
            return f"No claim was found with claim ID: {claim_id}"

        return str(claim)


search_claim = SearchClaimTool()
