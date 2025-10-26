#problem
#Grade system: A(>=90), B(>=80), C(>=70), D(>=60), F


#solution
score = float(input("Enter your grade: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade= "D"
else:
    grade = "F"
print(f'Youre grade is {grade}') 