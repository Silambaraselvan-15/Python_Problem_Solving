"""Problem Statement
A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

Handle the possible errors in the code written inside the function.

Sample Input                        Expected Output

'3523014'                   ['5230', '23014', '523', '352']

"""

#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    
    val=0
    output=[]
    n=len(num_str)
    for i in range(n):
        val=0
        for j in range(i,n):
            val += int(num_str[j])
           
            if val==10:
                output.append(num_str[i:j+1])
                
            elif val > 10:
                break
    return output

    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)