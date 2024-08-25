#lex_auth_012693802383794176153

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    failure="Triangle can't be formed"
    success="Triangle can be formed"
    if ( (num1< (num2+num3)) and (num2<(num1+num3)) and (num3<num2+num1)):
        return success 
   
        
    else:
         return failure 
    
       
        
        

    #Write your logic here

    #Use the following messages to return the result wherever necessary

#Provide different values for the variables, num1, num2, num3 and test your program

print(form_triangle(1,4,3))
print(form_triangle(1,7,3))
print(form_triangle(1,2,4))
print(form_triangle(12,7,3))