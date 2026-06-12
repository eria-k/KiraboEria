score=int(input("Enter your score: "))
if score >=90:
    grade="A"
    message="Excellent"
elif score >=80:
    grade="B"
    message="Good"
elif score >=70:
    grade="C"
    message="Satisfactory"
elif score >=60:
    grade="D"
    message="You need to work harder"
else:
    grade="F"
    message="Failed"
print(f"Your score is {score}, which corresponds to grade {grade}. {message}")