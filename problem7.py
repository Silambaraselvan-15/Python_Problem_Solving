#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))
    if num1<num2:
        for i in range(num2,num1+1,-1):
            
            if sum_of_digits(i)%3==0 and i%5==0 and i%3==0:
                
                max_num=i
                if max_num>99:
                    max_num=-1
                return max_num
            else:
                max_num=-1    
                
    return max_num
#Provide different values for num1 and num2 and test your program.
max_num=find_max(3,30)
print(max_num)
max_num=find_max(100,500)
print(max_num)