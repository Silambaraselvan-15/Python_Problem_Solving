"""Problem Statement
Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions 
and returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.
 

Sample Input                                Expected Output

[1, 2, 7, 4, 5, 6, 0, 3], 6                       3

[3, 4, 1, 8, 5, 9, 0, 6], 9                       4
"""

#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
    val=[]
    for i in num_list:
        for j in num_list:
            if i+j==n:
                val.append((i,j))
    
    
    return len(val)//2
    #Remove pass and write your logic here

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))