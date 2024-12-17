#Dennis Brantley
#Temp Converter
#dlbrantley@student.stcc.edu
#10/26/24



#Ask myself what am I looking for?
#No constants but the variables are set to what the answers to the questions are.
#They are variables because everyones answer will be different depending where they are.

fTemp= float(input("Enter a temperature "))
sDegreetype= input("Is the temp F for fahrenheit or C for Celsius? ").upper()

#My constant is set here.

SERROR_MESSAGE= "Please enter either F or C"

#My first condition is set. Only having 2 outcomes.
if sDegreetype != "C" and sDegreetype != "F":

    print(SERROR_MESSAGE)
    raise SystemExit

#Second condition is set here also only having 2 outcomes
#Calculation for meeting second condition
if sDegreetype== "C":
        if fTemp> 100:
                print("Temp cannot be greater than 100.")
        else:
                fFinaltemp= (9.0/ 5.0) * fTemp+32
                print(f"Wow that's amazing, {fTemp: .1f} degrees celsius is {fFinaltemp:.1f} degrees fahrenheit.")

#originally had a 3rd condtion set here and it worked, but I was helped in understanding a better way
#a more efficient way. Also got me to think a bit more. I left the condition commented out to reference.

#if strDegreetype== "F":
#Second calculation for second possible outcome.
else:
        if fTemp> 212:
         print("Temp cannot be greater than 212.")
        elif fTemp <=212:
                fFinaltemp= (5.0 / 9) * (fTemp -32)
                print(f"Wow that's amazing, {fTemp: .1f} degrees fahrenheit is {fFinaltemp:.1f} degrees celsius.")


