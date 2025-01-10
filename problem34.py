"""Problem Statement
Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
Handle the possible errors in the code written inside the function.

Sample Input            Expected Output

16                          120
"""
#lex_auth_01269442760027340879

def find_smallest_number(num):
    #start writing your code here'
    def divisors(n):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        return count
    number=0
    while divisors(number) != num:
        number+=1    
    return number

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)