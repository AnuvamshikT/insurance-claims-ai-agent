import pytest
from pydantic import ValidationError

from tools.claim_assessment import ClaimAssessment


def test_valid_claim_assessment():
    assessment = ClaimAssessment(
        claim_id="CLM-1001",
        claim_type="Auto",
        claim_amount=12500,
        status="Under Review",
        key_facts=["Vehicle collision reported"],
        missing_information=["Coverage details require verification"],
        preliminary_assessment="The claim requires further review.",
        requires_human_review=True,
        final_decision="Not made",
    )

    assert assessment.claim_id == "CLM-1001"
    assert assessment.claim_type == "Auto"
    assert assessment.claim_amount == 12500
    assert assessment.final_decision == "Not made"


def test_invalid_claim_type_is_rejected():
    with pytest.raises(ValidationError):
        ClaimAssessment(
            claim_id="CLM-1001",
            claim_type="Life",
            claim_amount=12500,
            status="Under Review",
            key_facts=[],
            missing_information=[],
            preliminary_assessment="Test assessment",
            requires_human_review=True,
            final_decision="Not made",
        )


def test_final_decision_approval_is_rejected():
    with pytest.raises(ValidationError):
        ClaimAssessment(
            claim_id="CLM-1001",
            claim_type="Auto",
            claim_amount=12500,
            status="Under Review",
            key_facts=[],
            missing_information=[],
            preliminary_assessment="Test assessment",
            requires_human_review=True,
            final_decision="Approved",
        )


def test_non_positive_claim_amount_is_rejected():
    with pytest.raises(ValidationError):
        ClaimAssessment(
            claim_id="CLM-1001",
            claim_type="Auto",
            claim_amount=-100,
            status="Under Review",
            key_facts=[],
            missing_information=[],
            preliminary_assessment="Test assessment",
            requires_human_review=True,
            final_decision="Not made",
        )
