#lex_auth_012693782475948032141
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if (distance_in_kms<=3) and (distance_in_kms>0):
        delivery_charge=0
        
    elif distance_in_kms>=4 and distance_in_kms<=6:
        delivery_charge=3*(distance_in_kms-3)
        
    elif distance_in_kms>6:
        delivery_charge=9+6*(distance_in_kms-6)
    else:
        delivery_charge=-1
     #write your logic here
    if food_type=="N" and quantity_ordered>=1 and delivery_charge>=0:
        bill_amount=(150*quantity_ordered)+delivery_charge
        return bill_amount
    elif food_type=="V" and quantity_ordered>=1 and delivery_charge>=0:
        bill_amount=(120*quantity_ordered)+delivery_charge
        return bill_amount
    else:
        bill_amount= -1
        return bill_amount
#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",1,7)
print(bill_amount)
bill_amount=calculate_bill_amount("V",1,7)
print(bill_amount)
bill_amount=calculate_bill_amount("N",2,8)
print(bill_amount)