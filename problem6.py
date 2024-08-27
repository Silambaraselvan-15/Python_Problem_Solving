#lex_auth_012693810762121216155

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if heads>0 and legs>0 and heads<legs and (legs%2==0):
        count=legs//2
        if count>=heads:
            if count>0:
                count1=count-heads
                chicken_count=heads-count1
                rabbit_count=count1
                print(chicken_count,rabbit_count)
            else:
                print(count)
                print("error")
        elif count<heads:
            count=legs//4
            if count>heads:
                if count>0:
                    count1=count-heads
                    chicken_count=heads-count1
                    rabbit_count=count1
                    print(chicken_count,rabbit_count)
                else:
                    print(count)
                    print("error")
    else:
        print(error_msg)

       
    
solve(35,94)
solve(400,1020)
solve(20,10)
solve(10,20)
solve(23,67)