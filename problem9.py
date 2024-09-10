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
