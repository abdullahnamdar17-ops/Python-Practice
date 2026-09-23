score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 or score < 89:
    print("Your grade is B")
else:
    print("Your grade is C")