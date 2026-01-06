def test_normalize_company_name():
    from company_name_cleaner import normalize_company_name

    assert normalize_company_name("CAF softsol") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("CAF solution") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("CAF softSolution India Pvt Limited") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("") is None
    assert normalize_company_name(None) is None
    assert normalize_company_name("Other Company") == "Other Company"

    print("All test cases passed!")