#Name: Dennis Brantley
#Date: 12/07/24
#Class: CIT-115-D01
#Email: dlbrantley@student.stcc.edu

#imported math module
import math




#Function created for data validation. Used to prompt for input.
def getFloatInput(sPrompt):
     while True:
         try:
            fRandomvari = float(input(sPrompt))
            if fRandomvari > 0:
                break
            else:
                print("Please provide a positive number.")
         except ValueError:
                print("please provide a positive number.")
     return fRandomvari












#Function created to gallon the total gallons of paint. Used the imported math module to round iTotalgallons to next whole number
def getGallonsOfPaint(iSqftofwall, feetpergallonpfpaint):
    iTotalgallons = math.ceil(iSqftofwall / feetpergallonpfpaint)
    return iTotalgallons

#Function used to gather the total numbers of labor hours
def getLaborHours(fHoursPer1Galin, iTotalgallonsin):
    fTotalLaborHours = (fHoursPer1Galin * iTotalgallonsin)
    return fTotalLaborHours

#Function used to gather the total labor cost
def getLaborCost(laborhourspergallon, fPaintinglaborchargeperhour):
      fTotalLaborCost= laborhourspergallon * fPaintinglaborchargeperhour
      return fTotalLaborCost

#Function used to get the total cost of the paint
def getPaintCost(iTotalgallons, fPaintprice):
      fTotalPaintCost =iTotalgallons * fPaintprice
      return fTotalPaintCost

#Function used to apply the correct amount of sales tax for the state the job is in.
def getSalesTax(sState):
             sState= input(sState).upper()
             if sState == ("MA"):
                 fState = .0625

             elif sState == ("CT") or sState == ("VT"):
                 fState =.06

             elif sState == ("ME"):
                 fState = .085

             elif sState == ("RI"):
                 fState = .07

             else:
                fState = 0

             return fState
#Function used to take the above correct sales tax and multiply that by the sum of the finallabor cost and final paint cost
def getTotalTax(fState, fFinalLaborcost, fFinalPaintCost):
    return (fFinalLaborcost+ fFinalPaintCost)* fState

#Function used to apply that tax from the above function
def getGrandTotal(fFinalTax, fFinalPaintCost, fFinalLaborcost ):
    return (fFinalTax + fFinalPaintCost + fFinalLaborcost )

#Function takes all this data, creates and writes it to a file
def writeNameToFile(sLastName, sResults):
    print(sResults)
    with open(f"{sLastName}_PaintJobOutput.txt", "w") as file:
        file.write(sResults)



#Function calls all functions and runs the program
def main():
    fSquarefootage = getFloatInput("What is the sqaure footage? ")
    fPriceOfPaintGal= getFloatInput("What is the cost of paint per gallon? ")
    fFeetPer1Gal =  getFloatInput("How many feet per gallon of paint? ")
    fHoursPer1Gal = getFloatInput("How many hours of labor per gallon of paint? ")
    fLaborChargePerHours = getFloatInput("How much is the labor charge per hour? ")

    sLastname= input("What is the customers last name? ")
    fState= getSalesTax("What state is the job in? Use Abbreviation.  ")



    iTotalgallons = (getGallonsOfPaint(fSquarefootage, fFeetPer1Gal))
    fTotalLaborHours = (getLaborHours(fHoursPer1Gal, iTotalgallons))
    fFinalLaborcost = (getLaborCost(fTotalLaborHours, fLaborChargePerHours))
    fFinalPaintCost = (getPaintCost(iTotalgallons, fPriceOfPaintGal))
    fFinalTax=  getTotalTax(fState, fFinalLaborcost, fFinalPaintCost)
    fGrandTotal= getGrandTotal(fFinalTax, fFinalLaborcost, fFinalPaintCost)
    sResults= f"""Gallons of paint: {iTotalgallons}
hours of labor: {fTotalLaborHours:,.1f}
paint charges: ${fFinalPaintCost:,.2f}
labor charges: ${fFinalLaborcost:,.2f}
tax: ${fFinalTax:,.2f}
total cost: ${fGrandTotal:,.2f}
file: {sLastname}_PaintJobOutput.txt was created"""
    writeNameToFile(sLastname, sResults)


#Called the main function to run the program
main()






















