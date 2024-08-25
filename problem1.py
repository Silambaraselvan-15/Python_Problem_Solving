#lex_auth_012693711503400960120

def find_product(num1,num2,num3):
    product=0
    if (num1!=7 and num2!=7 and num3!=7):
        product=(num1*num2*num3)
    elif num1!=7 and num2==7 and num3!=7:
        product=num3
    elif num1!=7 and num2!=7 and num3==7:
        product = -1
    elif num1==7 and num2!=7 and num3!=7:
        product = num2*num3
    else:
        product=-1



    #write your logic here
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(4,2,3)
print(product)
product=find_product(7,2,3)
print(product)
product=find_product(4,7,3)
print(product)
product=find_product(4,2,7)
print(product)