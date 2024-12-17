#CONSTANTS

#Set constants instead of variables because these values will not change
#If they were values that were going to change they would be set as variables instead

FMARS = 0.38
FMERCURY = 0.38
FVENUS = 0.91
FMOON = 0.165
FJUPITER = 2.34
FSATURN = 0.93
FURANUS = 0.92
FNEPTUNE = 1.12
FPLUTO = 0.066


#Conversions and variables
#sName and fWeight are both variables as the values given will change from user to user.

sName = input("What is your name: ")





#Converting the string that the user would input to a float so it can be solved.
#Without converting to a float it would be a string and strings cannot be used in a math equation.
fWeight = float(input("What is your Earth weight?: "))





#Output and calculations

#Made all the output "f strings" as a way to format them to be read easier,
#make more sense by adding variables or in this case constants
#and adding 10 spaces being occupied at the end of each string inside the curly braces
#so that the floats right side align
print(f"{sName}", 'Here are your weights on our solar systems planets')

print(f"{"Weight on Mars":25} {fWeight * FMARS:10,.2f}"'lbs')
print(f"{"Weight on Mercury":25} {fWeight * FMERCURY:10,.2f}"'lbs')
print(f"{"Weight on Venus":25} {fWeight * FVENUS:10,.2f}"'lbs')
print(f"{"Weight on Moon":25} {fWeight * FMOON:10,.2f}"'lbs')
print(f"{"Weight on Jupiter":25} {fWeight * FJUPITER:10,.2f}"'lbs')
print(f"{"Weight on Saturn":25} {fWeight * FSATURN:10,.2f}"'lbs')
print(f"{"Weight on Uranus":25} {fWeight * FURANUS:10,.2f}"'lbs')
print(f"{"Weight on Neptune":25} {fWeight * FNEPTUNE:10,.2f}"'lbs')
print(f"{"Weight on Pluto":25} {fWeight * FPLUTO:10,.2f}"'lbs')