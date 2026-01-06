def normalize_company_name(company_name):
    
    if company_name is None:
        return None
    company_name = str(company_name).strip()
    if company_name == "":
        return None
    name_lower = company_name.lower()
    if "caf" in name_lower:
        return "CAF SoftSol India Pvt Ltd."
    return company_name