#lex_auth_012693788748742656146

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    #Start writing your code here
    if account_number<=1999 and account_number>=1000:
        if loan_type=="Car":
            eligible_loan_amount=500000
            bank_emi_expected=36
            if salary>25000:
                if account_balance>=100000:
                    if loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected :
                        print("Account number:", account_number)
                        print("The customer can avail the amount of Rs.", eligible_loan_amount)
                        print("Eligible EMIs :", bank_emi_expected)
                        print("Requested loan amount:", loan_amount_expected)
                        print("Requested EMI's:",customer_emi_expected)
                    else:
                        print("The customer is not eligible for the loan")
                else:
                    print("Insufficient account balance")
            else:
                print("Invalid loan type or salary")
        elif loan_type=="House":
            eligible_loan_amount=6000000
            bank_emi_expected=60
            if salary>50000:
                if account_balance>=100000:
                    if loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected :
                        print("Account number:", account_number)
                        print("The customer can avail the amount of Rs.", eligible_loan_amount)
                        print("Eligible EMIs :", bank_emi_expected)
                        print("Requested loan amount:", loan_amount_expected)
                        print("Requested EMI's:",customer_emi_expected)
                    else:
                        print("The customer is not eligible for the loan")
                else:
                    print("Insufficient account balance")
            else:
                print("Invalid loan type or salary")
        elif loan_type=="Business":
            eligible_loan_amount=7500000
            bank_emi_expected=84
            if salary>75000:
                if account_balance>=100000:
                    if loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected :
                        print("Account number:", account_number)
                        print("The customer can avail the amount of Rs.", eligible_loan_amount)
                        print("Eligible EMIs :", bank_emi_expected)
                        print("Requested loan amount:", loan_amount_expected)
                        print("Requested EMI's:",customer_emi_expected)
                    else:
                        print("The customer is not eligible for the loan")
                else:
                    print("Insufficient account balance")
            else:
                 print("Invalid loan type or salary") 
        else:
            print("Invalid loan type or salary") 
    else:
        print("Invalid account number")


    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)