"""A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp, 
the teacher rewards them with chocolates.

Write a Python function to

1. Find the total number of chocolates received by all the children put together.
Assume that each child is identified by an id and it is stored in a tuple and the number of chocolates given to each child is stored in a list.

2. The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.

If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", should be displayed.

If the given child Id is invalid, an error message "Child id is invalid" should be displayed.
Otherwise, the extra chocolates provided for the child must be added to his/her existing number of chocolates and
display the list containing the total number of chocolates received by each child."""


#lex_auth_01269442027919769669

#Global variables
    
child_id=(11, 12, 13, 14, 15)
chocolates_received=[33, 12, 0, 0, 2]
result=dict(zip(child_id,chocolates_received))

def calculate_total_chocolates():
    return sum(chocolates_received)
def reward_child(child_id_rewarded,extra_chocolates):
    if child_id_rewarded not in child_id: 
        print("Child id is invalid")
    elif extra_chocolates < 1:
        print("Extra chocolates is less than 1")
    else:
        value=child_id.index(child_id_rewarded)
        chocolates_received[value]+=extra_chocolates
        print(chocolates_received)
reward_child(20,14)
print(calculate_total_chocolates())
