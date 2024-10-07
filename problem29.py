"""Problem Statement
The road transport corporation (RTC) of a city wants to know whether a particular bus-route is running on profit or loss.

Assume that the following information are given:
Price per litre of fuel = 70
Mileage of the bus in km/litre of fuel = 10
Price(Rs) per ticket = 80

The bus runs on multiple routes having different distance in kms and number of passengers.
Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss."""


#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    fuel_cost = 70
    milage=10
    ticket_cost=80
    collection=no_of_passengers*ticket_cost
    print(collection)
    fuel_usage_cost=(fuel_cost*distance)//milage
    print(fuel_usage_cost)
    if collection>fuel_usage_cost:
        return collection-fuel_usage_cost
    else:
        return -1

    
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=100
no_of_passengers=10
print(calculate(distance,no_of_passengers))