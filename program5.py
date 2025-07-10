salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
    loan_amount=int(input("enter loan amount:"))
    if(loan_amount<=50000):
        print("you are eligible for loan")
    else:
        print("maximum loan amount is 50000")
else:
    print("you are not eligible for loan")

    
