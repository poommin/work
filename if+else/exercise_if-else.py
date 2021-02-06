score = int(input("Enter your score: "))


if score >= 80 and score < 101:
    print("grade:  A")
elif score >= 75 and score < 80:
    print("grade:  B+")
elif score >= 70 and score <= 74:
    print("grade:  B")
elif score >= 65 and score <= 69:
    print("grade:  C+")
elif score >= 60 and score <= 74:
    print("grade:  C")
elif score >= 55 and score <= 59:
    print("grade:  D+")
elif score >= 50 and score <= 54:
    print("grade:  D")
else:
    print("grade:  F")