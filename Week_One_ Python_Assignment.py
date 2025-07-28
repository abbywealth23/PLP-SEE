# A simple Calculator that ask users for input of two figures and operator.
# ask user to enter a the figures and the operator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = (input("Enter the operator (-, +, x, /): "))

#calculations 
if operator == "+":
        add = num1 + num2   #addition
        print(f"{num1} + {num2} = {add}")
        print("Done!")
elif operator == "-":
        subtract = num1 - num2  #subtraction
        print(f"{num1} - {num2} = {subtract}")
        print("Done")
elif operator == "/":
        if num2 != 0:
                division = num1 / num2  #Division  
                print(f"{num1} / {num2} = {division}")   
                print("Done")
        else:
                print("sorry, you can't divide by 0")
elif operator == "*":
        multiply = num1 * num2  #multiplication
        print(f"{num1} * {num2} = {multiply}")
        print("Done")
else: print("Oops! Wrong Operator")
