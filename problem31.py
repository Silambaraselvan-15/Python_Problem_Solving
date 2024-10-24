"""
Problem Statement

Consider that the human tower is to be performed on a stage and the stage has a maximum weight limit. 

Write a python program to find the maximum number of people at the base level such that 
the total weight of tower does not exceed the maximum weight limit of the stage. 

Assume that:
1. Each person weighs 50 kg 
2. There will always be odd number of men at the base level of the human tower.

"""

#lex_auth_01269437527007232044

def human_pyramid(no_of_people):
    if no_of_people==1:
        return no_of_people*50
    else:
        return no_of_people*50 + human_pyramid(no_of_people-2) 
        #remove pass and place the recursive code the you had written earlier for this function

def find_maximum_people(max_weight):
    for i in range(1,1000,2):
      if human_pyramid(i)<=max_weight:
          no_of_people=i
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable 
    return no_of_people

#Provide different values for max_weight and test your programc 
max_people=find_maximum_people(1250)
print(max_people)
print(human_pyramid(9))