#Ask a ueer to ipput a ccore
score = int(input("entersstueent score(0 - 100):  "))

if score >= 90:
    grade = 'A'

elif score >= 80:
    grade = 'B'

elif score >= 70:
    grade = 'C'

elif score >= 60:
    grade = 'D'

else: 
    grade = 'F'

#print the result
print(f"The students grade is: {grade}")