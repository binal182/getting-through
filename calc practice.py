# creating a simple arithmetic calculator
def calculator():
    print("welcome to the simple arithmetic calculator.")
    print(" the available operations are: +, -, *, /")
    # users provides number and function for the calculation
while True:
    num1= float(input("enter the first number: "))
    operation= input("enter the operations (+, -, *, /): ").strip()
    num2= float(input("enter the second number: "))
    #perform the operations based
    if operation == '+':
        result = num1 + num2
    elif operation =='-':
        result = num1-num2
    elif operation =='*':
        result = num1*num2
    elif operation =='/':
        if num2 !=0:
            result = num1/num2
        else:
            print("ERROR: division by zero is not allowed")
            continue
    else: 
        print("invalid operations!!")
        continue
    #display the result
    print(f"the result of {num1} {operation} {num2} is {result}: ")
    #if user wants another calculation
    another =input("do you want to do another calculations? (yes/no)").strip().lower()
    if another == 'yes':
        continue
    elif another =='no':
        print("thank you for using calculator. goodbye!!")
    break
    # get the calculation function
    calculator()

