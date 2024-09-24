"""Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding.

 Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program

Sample Input            Expected Output

AAAABBBBCCCCCCCC        4A4B8C
                        
AABCCA                  2A1B2C1A


"""

#lex_auth_012693816331657216161

def encode(message):
    count = 1
    answer = []
    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            answer.append(f"{count}{message[i - 1]}")
            count = 1  
     
    answer.append(f"{count}{message[-1]}")
    
    return "".join(answer)


encoded_message = encode("AABBBBCCCCCCCCABB")
print(encoded_message) 

encoded_message = encode("AAABCCA")
print(encoded_message) 

