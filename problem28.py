"""
Problem Statement
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

The number and its double should have exactly the same number of digits.

Both the numbers should have the same digits ,but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order."""


#lex_auth_01269441810970214471

def check_double(number):
    double=number*2
    double_list=list(str(double))
    number_list=list(str(number))
    print(number," == ",double)
    TF_list=[]
      
    for i in double_list:
        if i in number_list:
            TF = True
            TF_list.append(TF)
        else:
            TF = False
            TF_list.append(TF)
    return all(TF_list)

    
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(100))