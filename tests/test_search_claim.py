from tools.search_claim import search_claim


def test_retrieve_existing_auto_claim():
    result = search_claim.run(claim_id="CLM-1001")

    assert "CLM-1001" in result
    assert "POL-AUTO-5001" in result
    assert "12500" in result
    assert "Under Review" in result


def test_retrieve_existing_home_claim():
    result = search_claim.run(claim_id="CLM-1002")

    assert "CLM-1002" in result
    assert "POL-HOME-7002" in result
    assert "8750" in result
    assert "Submitted" in result


def test_nonexistent_claim_returns_not_found_message():
    result = search_claim.run(claim_id="CLM-9999")

    assert "No claim was found" in result
    assert "CLM-9999" in result
