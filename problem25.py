"""
Problem Statement
Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
145 is a Strong number as 1! + 4! + 5! = 145. 

Sample Input                                     Expected Output

num_list = [145,375,0,100,2]                        [145, 2]

 

Note: 0!=1b

"""

#lex_auth_01269437118923571233

def factorial(number):
    if number == 0:
        return 1
    elif number==1:
        return 1
    else:
        fact=1
        for i in range(1,number+1):
            fact=fact*i
        return fact


def find_strong_numbers(num_list):
    strong_num_list=[]
    for num in num_list:
        digits=[int(digit) for digit in str(num)]

        sum_of_digits=sum(factorial(digit) for digit in digits)
    
        if sum_of_digits==num:
            strong_num_list.append(sum_of_digits)
        
    return strong_num_list 


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
