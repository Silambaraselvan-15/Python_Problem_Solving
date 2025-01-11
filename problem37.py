"""Problem Statement
Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. Otherwise returns False.

The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position. The length of the strings should be the same.

Note: Perform case insensitive comparison wherever applicable.

Sample Input                                                        Expected Output

eat, tea                                                                True

backward,drawback                                                       False 
(Reason: character 'a' repeats at position 6, not an anagram)

Reductions,discounter                                                   True

About, table                                                            False

 """

#lex_auth_0127382206342184961397

def check_anagram(data1, data2):
    data1 = data1.lower()
    data2 = data2.lower()
    
    if len(data1) != len(data2):
        return False
    elif sorted(data1) == sorted(data2):
        for i in data1:
            for j in data2:
                if i == j and data1.index(i) == data2.index(j):
                    return False
        return True
    else:
        return False    
    

print(check_anagram("listen", "silent")) 
print(check_anagram("mango", "apple")) 