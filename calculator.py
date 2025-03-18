import math

print("Pythonic Scientific Calculator (PSC)\n")

def const(value):
    match value:
        case 2.71:
            return math.e
        case 3.14:
            return math.pi
        case 6.28:
            return math.tau
        case _:
            return value

user_input = int(input("1 Addition| 2 Subtraction | 3 Multiplication | 4 Division | 5 Logarithm | 6 Square Root | 7 Exponents| 8 Sine | 9 Cosine | 0 Tangent\n"))

x = float(input("x: "))
x = const(x)
y = float(input("y: "))
y = const(y)

if user_input == 1:
    print(x,"+",y,"=",x+y)
elif user_input == 2:
    print(x,"-",y,"=",x-y)
elif user_input == 3:
    print(x,"*",y,"=",x*y)
elif user_input == 4:
    try:
        print(x,"/",y,"=",x/y)
    except:
        print(x,"/",y,"= undefined")
elif user_input == 5:
    print("log_",y,"(",x,")"," = ", math.log(x,y), sep="")
elif user_input == 6: 
    print("Sqrt of",x,"=",math.sqrt(x),
          "Sqrt of",y,"=",math.sqrt(y))
elif user_input == 7:
    print(x,"^",y," = ",pow(x,y),sep="")
elif user_input == 8:
    print("Sinx =", math.sin(math.radians(x)),
          "Siny =", math.sin(math.radians(y)))
elif user_input == 9:
    print("Cosy =", math.cos(math.radians(x)),
          "Cosy =", math.cos(math.radians(y)))
elif user_input == 0:
    print("Tanx =", math.tan(math.radians(x)),
          "Tany =", math.tan(math.radians(y)))
else:
    print("Option not found, please try again.")