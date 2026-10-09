from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from datetime import date


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

    def _validate_claim(self, claim: dict, requested_claim_id: str) -> list[str]:
        errors = []

        required_fields = [
            "claim_id",
            "policy_number",
            "claim_type",
            "date_of_loss",
            "claim_amount",
            "status",
            "description",
        ]

        for field in required_fields:
            if field not in claim or claim[field] is None or claim[field] == "":
                errors.append(f"Missing required field: {field}")

        if errors:
            return errors

        if claim["claim_id"] != requested_claim_id:
            errors.append("Claim ID does not match the requested ID.")

        if claim["claim_type"] not in ["Auto", "Home"]:
            errors.append("Invalid claim type.")

        if not isinstance(claim["claim_amount"], (int, float)) or isinstance(claim["claim_amount"], bool) or claim["claim_amount"] <= 0:
            errors.append("Claim amount must be a positive number.")

        try:
            date.fromisoformat(claim["date_of_loss"])
        except (ValueError, TypeError):
            errors.append("Date of loss must be a valid ISO date (YYYY-MM-DD).")

        if not isinstance(claim["policy_number"], str):
            errors.append("Policy number must be a string.")

        if not isinstance(claim["description"], str):
            errors.append("Claim description must be a string.")

        return errors

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

        requested_claim_id = claim_id.strip().upper()
        claim = claims.get(requested_claim_id)

        if not claim:
            return f"No claim was found with claim ID: {requested_claim_id}"

        errors = self._validate_claim(claim, requested_claim_id)

        if errors:
            return "Claim validation failed: " + "; ".join(errors)

        return str(claim)


search_claim = SearchClaimTool()
