"""
Given a number n, write a program to find the sum of the largest prime factors of each of 
nine consecutive numbers starting from n.
g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8)
where, g(n) is the sum and f(n) is the largest prime factor of n

For example,

g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18) 
        =5 + 11 + 3 + 13 + 7 + 5 + 2 + 17 + 3 
        =66 """

#lex_auth_01269442963365068878

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        
        if(num%i==0):
            factors.append(i)
    
    #print("factors are " ,factors)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    for i in range(len(list_of_factors)-1,-1,-1):
        if(is_prime(list_of_factors[i],list_of_factors[i]//2)):
            return list_of_factors[i]
    return 1
    #Accepts the list of factors and returns the largest prime factor

def find_f(num):
    factors=find_largest_prime_factor(find_factors(num))
    
    return factors
    #Accepts the number and returns the largest prime factor of the number
    

def find_g(num):
    sum=0
    for i in range(num,num+9):
        sum=sum+find_f(i)
    print("sum is ",sum)
        
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    return sum

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))
print(find_g(78))