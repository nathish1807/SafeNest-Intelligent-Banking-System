from agents.fraud_agent import detect_fraud
from agents.loan_agent import check_loan_eligibility


def process_transaction(amount):
    fraud_result = detect_fraud(amount)
    return fraud_result


def process_loan(income, credit_score):
    loan_result = check_loan_eligibility(income, credit_score)
    return loan_result