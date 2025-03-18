import math

equation = []
user_input= input("Enter your equation (e.g. 2+2): ")

def addToEquation(input,operation):
        equation.append(float(input[0]))
        equation.append(operation)
        equation.append(float(input[1]))

def splice(input):
    if "+" in input:
        input = input.split("+")
        addToEquation(input,"+")
    elif "-" in input:
        input = input.split("-")
        addToEquation(input,"-")
    elif "*" in input:
        input = input.split("*")
        addToEquation(input,"*")
    elif "/" in input:
        input = input.split("/")
        addToEquation(input,"/")
    else:
        print("Invalid Operator Error.")
    return equation

equation = splice(user_input)

try: 
    if "+" in equation:
        print(equation[0],"+",equation[0],"=",equation[0]+equation[2])
    elif "-" in equation:
        print(equation[0],"-",equation[2],"=",equation[0]-equation[2])
    elif "*" in equation:
        print(equation[0],"*",equation[2],"=",equation[0]*equation[2])
    elif "/" in equation:
        print(equation[0],"/",equation[2],"=",equation[0]/equation[2])
    else:
        print("Undetermined User Input.")
except:
    print("Invalid Operator Error.")
