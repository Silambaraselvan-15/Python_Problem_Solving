"""Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number
where

Consider AI as the value for airline
src and dest should be the first three characters of the source and destination cities.
number should be auto-generated starting from 101
The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, return the list of all generated ticket numbers.

Sample Input                                        Expected Output

airline = AI                                          ['AI:Ban:Lon:106', 'AI:Ban:Lon:107', 'AI:Ban:Lon:108', 'AI:Ban:Lon:109', 'AI:Ban:Lon:110']
source = Bangalore
destination = London
no_of_passengers = 10



airline = BA                                          ['BA:Aus:Fra:101', 'BA:Aus:Fra:102']
source = Australia
destination = France
no_of_passengers = 2


"""
#lex_auth_012693763253788672132

def generate_ticket(airline, source, destination, no_of_passengers):
   
    ticket_number_list = []

    source_abbr = source[:3]
    destination_abbr = destination[:3]

    start_number = 101
    for i in range(no_of_passengers):
        ticket_number = f"{airline}:{source_abbr}:{destination_abbr}:{start_number + i}"
        ticket_number_list.append(ticket_number)

    if no_of_passengers > 5:
        return ticket_number_list[-5:]
    else:
        return ticket_number_list

print(generate_ticket("AI", "Bangalore", "London", 10))

print(generate_ticket("BA", "Australia", "France", 2))
