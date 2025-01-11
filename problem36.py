"""Problem Statement
Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list and the order should be same as in the input list. If there are no duplicate values, it should return an empty list.

Sample Input                                    Expected Output

[12,54,68,759,24,15,12,68,987,758,25,69]            [12, 68]

"""
#lex_auth_01269443477535129681

def find_duplicates(list_of_numbers):
    #start writing your code here
    seen=set()
    temp=set()
    for i in list_of_numbers:
        if i in seen:
            if i not in temp:
                temp.add(i)
               
        else:
            seen.add(i)
    return list(temp)
list_of_numbers=[1,2,2,5,6,5,5,8,1]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)