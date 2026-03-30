def check_loan_eligibility(income, credit_score):

    if income > 30000 and credit_score > 650:
        return "Loan Approved"

    elif credit_score < 600:
        return "Loan Rejected"

    else:
        return "Manual Review Required"