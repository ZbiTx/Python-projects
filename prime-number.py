print("==Prime Number Checker, Finder and List==")

def checker(x):
    if x==0 or x==1:
        return False
    elif x==2:
        return True
    elif x>1:
        for i in range(2,x):
            if x%i==0:
                return False
            elif i>=x-1:
                return True
            else:
                continue
    else:
        print("Invalid Input, please try again")

def finder(x):
    primes = []
    if x<0:
        print("Negative value error. ")
    else:
        for i in range(1,10000):
            if checker(i):
                primes.append(i)
        print("nth prime =",primes[x-1])

def list(x):
    primes = []
    if x<=0:
        print("Zero Primes Found.")
    else:
        for i in range(1,10000):
            if checker(i):
                primes.append(i)
        print(primes[:x])

user_input = int(input("1 Prime Number Checker | 2 Prime Number Finder | 3 Prime Number List\n"))

if user_input==1:
    x = int(input("Enter an integer: "))
    if checker(x)==True:
        print(x,"is prime")
    elif checker(x)==False:
        print(x,"is not prime")
    else:
        checker(x) 
elif user_input==2:
    finder(int(input("Enter nth prime number: ")))
elif user_input==3:
    list(int(input("Enter amount of primes: ")))
else:
    print("Invalid input, please try again.")