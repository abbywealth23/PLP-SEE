# A simple grading system that ouputs the grades of college students
#Prompt usser to enter a score from 0 - 100

Student_score = float(input("Enter the student's score (0 -100): ")) #this part ask the user a score

#conditions for outputing grade
if Student_score > 75:
    print("You have done well!")
    print("Your grade is 'A'")
elif Student_score > 65:
    print("You did great!")
    print("Your grade is 'B'")
elif Student_score > 55 :
    print("You have tried!")
    print("Your grade is 'C'")
elif Student_score > 40:
     print("You need to put more effort")
     print("Your grade is 'D'")
else:
    print("You have scored low")
    print("You Fail")