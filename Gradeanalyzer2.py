#Dennis Brantley
#Grade analyzer
#dlbrantley@student.stcc.edu


sName = input("What is your name? ")

iScore1 = int(input("What is test score 1? "))
iScore2 = int(input("What is test score 2? "))
iScore3 = int(input("What is test score 3? "))
iScore4 = int(input("What is test score 4? "))

sGrade_drop = input("Would you like to drop the lowest grade? Y or N? ").upper()

# Validate scores
if iScore1 < 0 or iScore2 < 0 or iScore3 < 0 or iScore4 < 0:
    raise SystemExit("Test scores must be greater than or equal to 0")

if sGrade_drop != "Y" and sGrade_drop != "N":
    raise SystemExit("Enter Y or N to drop the lowest grade.")

# Determine the lowest score if dropping is selected
numberoftest = 4
if sGrade_drop == "Y":
    if iScore1 < iScore2 and iScore1 < iScore3 and iScore1 < iScore4:
        iLowest = iScore1
    elif iScore2 < iScore3 and iScore2 < iScore4:
        iLowest = iScore2
    elif iScore3 < iScore4:
        iLowest = iScore3
    else:
        iLowest = iScore4
    numberoftest -= 1
else:
    iLowest = 0

# Calculate the average
fGradeaverage = (iScore1 + iScore2 + iScore3 + iScore4 - iLowest) / numberoftest

# Determine letter grade
if fGradeaverage >= 97.0:
    sLetter = "A+"
elif fGradeaverage >= 94.0:
    sLetter = "A"
elif fGradeaverage >= 90.0:
    sLetter = "A-"
elif fGradeaverage >= 87.0:
    sLetter = "B+"
elif fGradeaverage >= 84.0:
    sLetter = "B"
elif fGradeaverage >= 80.0:
    sLetter = "B-"
elif fGradeaverage >= 77.0:
    sLetter = "C+"
elif fGradeaverage >= 74.0:
    sLetter = "C"
elif fGradeaverage >= 70.0:
    sLetter = "C-"
elif fGradeaverage >= 67.0:
    sLetter = "D+"
elif fGradeaverage >= 63.0:
    sLetter = "D"
elif fGradeaverage >= 60.0:
    sLetter = "D-"
else:
    sLetter = "F"

# Print results
print(f"Well {sName}, your grade average is {fGradeaverage:.1f}.")
print(sLetter)