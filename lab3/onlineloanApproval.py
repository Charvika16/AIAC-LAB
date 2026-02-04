def online_loan_approval(income, credit_score, existing_loans):
    if credit_score>=750 and income >=30000:
        return "loan Approaved"
    elif credit_score >=650 and credit_score<=749 and existing_loans==0:
        return "loan Approaved with high intrest "
    elif credit_score <650 and income <30000:
        return "loan rejected"
    else:
        return "loan requires further review"
#example usage
print(online_loan_approval(40000, 780, 1))  
print(online_loan_approval(28000, 640, 2))  
print(online_loan_approval(32000, 700, 0))  
