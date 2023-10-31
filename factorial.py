import math

def factorial(number):
    if type(number) is not int:
        return None
    if number==0:
        return 1;
    elif number>0:
        return number*factorial(number-1);
    
x=factorial(5)
print(x)
x=factorial(6)
print(x)
x=factorial(0)
print(x)
x=factorial(-2)
print(x)
x=factorial(1.2)
print(x)
x=factorial("no output for Strings ")
print(x)



    