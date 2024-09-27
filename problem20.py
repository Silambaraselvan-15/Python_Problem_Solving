"""Problem Statement
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

1.Assume that the sentence would begin with a word and there will be only a single space between the words.

2.Perform case sensitive string operations wherever necessary.

Sample Input                            Expected Output

the sun rises in the east             eht snu sesir ni eht stea"""


#lex_auth_01269444195664691284
import random
def encrypt_sentence(sentence):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    words = sentence.split()  
    encrypted_words = []  
    for i in range(len(words)):
        word = words[i]
        
        if (i+1) % 2 != 0:
            encrypted_words.append(word[::-1])
        else:
            consonants = []
            vowels_in_word = []
            for char in word:
                if char in vowels:
                    vowels_in_word.append(char)
                else:
                    consonants.append(char)
            
            rearranged_word = ''.join(consonants) + ''.join(vowels_in_word)
            encrypted_words.append(rearranged_word)

    encrypted_sentence = ' '.join(encrypted_words)
    
    return encrypted_sentence

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
