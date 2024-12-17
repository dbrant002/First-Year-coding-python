#Name: Dennis Brantley
#Date: 11/24/24
#Class: CIT-115-D01
#Email: dlbrantley@student.stcc.edu


#Used a function to ask for the 4 inputs required rather than make 4 seperate blocks of code

def datavalidate(numx):
    fOriginalamt =-1
    while fOriginalamt < 0:
        try:
            fOriginalamt = float(input(numx))
            if fOriginalamt < 0:
                print("Must enter a numeric value!")

        except ValueError:
            print("Must enter a numeric value!")
    return fOriginalamt

#Called the function that was created above to ask for these inputs
fOgdeposit = datavalidate("What is the original deposit? ")
fIntrate = (datavalidate("What is the interest rate? ") / 100) /12
iMonths= int(datavalidate("What is the number of months? "))
fgoalamt = datavalidate("What is your goal amount? ")


#Setting up the loop for number of months input above. Since we dont know what the iMonths going to be we use +1 because
#we want to include the iMonths given. For loops are exclusive of the stop number.
for iMonths in range(1, iMonths + 1):
    fAcctbalance = fOgdeposit* fIntrate
    fOgdeposit += fAcctbalance
    print (f"Month: {iMonths:<2} acount balance is ${fOgdeposit:,.2f}")

if fgoalamt == 0:
    iMonths == 0

#Loop to calculate the number of months to reach your goal amout of money.
while fOgdeposit< fgoalamt:
    fInterestamt = fOgdeposit* fIntrate
    fOgdeposit += fInterestamt
    iMonths += 1
    if fOgdeposit> fgoalamt:
        print (f"It will take {iMonths:<2} months to reach your goal of ${fgoalamt:,.2f}")























