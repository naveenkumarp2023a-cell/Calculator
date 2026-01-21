print("Welcome to our Calculator")

print("Features")

def addition(a,b):
    return a+b

def subraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

number1=int(input("Enter number 1: "))
number2=int(input("Enter number 2: "))

while True:
    print("---------A simple calculator---------\n 1. Addition \n 2.Subraction \n 3.Multiplication \n 4.Division \n 5.Exit ")
    option=int(input("Enter options for operation: "))

    if(option==1):
        addition(number1,number2)
        print("Addition of two numbers: ",number1+number2)
    elif(option==2):
        subraction(number1,number2)
        print("Subraction of two numbers: ",number2+number2)
    elif(option==3):
        multiplication(number1,number2)
        print("Multiplication of two numbers: ",number2+number2)
    elif(option==4):
        division(number1,number2)
        print("Division of two numbers: ",number2+number2)
    elif(option==5):
        break

print("Thank you for using  our calculator")