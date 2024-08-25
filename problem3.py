#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    value_of_coins=(no_of_five*5) + (no_of_one*1)
    if(rupees_to_make<=(value_of_coins)):

        max_five_coin=(rupees_to_make//5)
        if max_five_coin>no_of_five:
            diff=max_five_coin-no_of_five

            max_five_coin=max_five_coin-diff

        remaining_amount=rupees_to_make-(max_five_coin*5)
        if remaining_amount>no_of_one:
            difference=remaining_amount-no_of_one
            remaining_amount=remaining_amount-difference
        if ((max_five_coin*5)+(remaining_amount))!=rupees_to_make:
            print(-1)
            return 0
        five_needed=max_five_coin
        one_needed=remaining_amount

        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)
    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(105,20,5)
make_amount(110,21,8)
make_amount(93,19,2)
make_amount(125,22,15)
make_amount(16,1,15)