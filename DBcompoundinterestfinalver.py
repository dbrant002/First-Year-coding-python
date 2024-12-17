#Name: Dennis Brantley
#Date: 10/12/24
#Class: CIT-115-D01
#Email: dlbrantley@student.stcc.edu




#Set my variables and input statements.
#Also the conversion to change the float fRate to a decimal for math.
#Also converting all input strings to floats again for math.

fPvv= float(input("What is the starting prinicipal? "))

fRate = float(input("What is the annual interest rate? ")) /100

fCompond = float(input("How many times per year is the interest compounded? "))

fYears = float(input("How many years will the account earn interest? "))

fMt = fYears * fCompond

#This is where the bulk of the math takes place, which is also set as a variable.

FV = fPvv * (1 + fRate / fCompond)**(fMt)


#Output here making sure to format for 2 decimal places and proper commma placement in the {FV} variable

print(f"At the end of {fYears} years you will have ${FV:,.2f}")