validScore = False
while validScore == False:
    validScore = True
    test1 = int(input("Enter Test 1 score: "))
    if test1 < 1 or test1 > 10:
        print("Invalid Input")
        validScore = False
validScore = False
while validScore == False:
    validScore = True
    test2 = int(input("Enter Test 2 score: "))
    if test2 < 1 or test2 > 10:
        print("Invalid Input")
        validScore = False  

if test1 > 6 and test2 > 6:
    print("Promoted")
elif test1 > 3 and test2 > 3:
    print("Go to final")
else:
    print("Recuperatory")

