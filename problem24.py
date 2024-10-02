"""Problem Statement
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:

The word should have the largest frequency.

In case multiple words have the same frequency, then choose the word that has the maximum length.

Assumptions:

The text has no special characters other than space.

The text would begin with a word and there will be only a single space between the words.

Perform case insensitive string comparisons wherever necessary.

Sample Input                                                                             Expected Output

"Work like you do not need money love like you have
 never been hurt and dance like no one is watching"                                         like 3

"Courage is not the absence of fear but rather the 
judgement that something else is more important than fear"                                  fear 2

"""

#lex_auth_0127382283825971201450
def max_frequency_word_counter(data):
    data = data.lower()
    words = data.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    max_word = ""
    max_frequency = 0
    for word, frequency in word_count.items():
        if frequency > max_frequency:
            max_frequency = frequency
            max_word = word
        elif frequency == max_frequency:
            if len(word) > len(max_word):
                max_word = word
    print(max_word, max_frequency)


#Provide different values for data and test your program
data="Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)