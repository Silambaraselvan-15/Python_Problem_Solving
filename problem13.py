"""Write a python function, create_largest_number(),
   which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.

    Note: Assume that all the numbers are two digit numbers.
 

   Sample Input            Expected Output

     23,34,55                   553423
"""
#lex_auth_01269441913243238467

def create_largest_number(number_list):
    pass
    #remove pass and write your logic here
    num1=number_list[0]
    num2=number_list[1]
    num3=number_list[2]
    #first we need to find the biggest value
    if num1 >num2 and num1 >num3:
        num="1 is bigger"
        num_val=num1
    elif num2 > num1 and num2 >num3:
        num="2 is bigger"
        num_val=num2
    else:
        num="3 is bigger"
        num_val=num3
    large_number=num_val
    # now we nee to find the second biggest value , so we can add the third value at last
    if (num_val>num1 and num1>num3) :
        numsec="1 is second and 3 is last"
        large_number=(str(large_number)+str(num1)+str(num3))
    if ( num_val>num1 and num1>num2):
        numsec="1 is second and 2 is last"
        large_number=(str(large_number)+str(num1)+str(num2))


    elif (num_val>num2 and num2>num3):
        numsec="2 is second and 3 is last"
        large_number=(str(large_number)+str(num2)+str(num3))


    elif (num_val>num3 and num3>num2) :
        numsec="3 is second and 2 is last"
        large_number=(str(large_number)+str(num3)+str(num2))
    elif ( num_val>num3 and num3>num1):
        numsec="3 is second ans 1 is last"
        large_number=(str(large_number)+str(num3)+str(num1))
    

    elif ( num_val>num2 and num2>num1):
        numsec="2 is second and 1 is last"
        large_number=(str(large_number)+str(num2)+str(num1 ))


    return int(large_number)


number_list=[10, 20, 32]
largest_number=create_largest_number(number_list)
print(largest_number)

