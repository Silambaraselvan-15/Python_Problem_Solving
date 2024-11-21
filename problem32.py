"""Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. 

The function should return true, if it is a palindrome. Else it should return false. 

Note- Perform case insensitive operations wherever necessary."""



#lex_auth_01269442114344550475

def is_palindrome(word):
    word=word.lower()
    if len(word)==0 or len(word)==1:
        return True
    else:
        if word[0]==word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False

    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("Madam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")