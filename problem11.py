"""Write a Python program to generate the next 15 leap years starting from a given year. 
   Populate the leap years into a list and display the list. 

"""
#lex_auth_012693797166096384149

def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years=[]
    for i in range(given_year,given_year+100):
        
        if ((i%4==0) and (i%100!=0)) or (i%400==0):
            list_of_leap_years.append(i)
       
    return list_of_leap_years[:15]

list_of_leap_years=find_leap_years(1000)
print(list_of_leap_years)