"""Problem Statement
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Sample Input                            Expected output

"I like Python"
"Java is a very popular language"           lieyon

"""

#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    msg1=msg1.replace(" ","")
    msg2=msg2.replace(" ","")
    msg0=set(msg1) 
    msg4=set(msg2)
    msg=msg0 & msg4
    
    if not msg:
        return -1
        
    else:
    
        answer=[]
        for i in msg1:
            if i in msg and i not in answer:
                answer.append(i)
    return "".join(answer)
    

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)