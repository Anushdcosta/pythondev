exam = 1000
while exam > 100:    
    exam = int(input("Enter your exam scores (0 - 100)? "))

    if exam > 100:
        print("Please enter marks between 0 to 100")
    elif exam > 90 and exam <= 100:
        print("Your Grade is A")
    elif exam > 80 and exam <= 89:
        print("Your Grade is B")
    elif exam > 70 and exam <= 79:
        print("Your Grade is C")
    elif exam > 60 and exam <= 69:
        print("Your Grade is D")
    else:
        print("Your Grade is F")



