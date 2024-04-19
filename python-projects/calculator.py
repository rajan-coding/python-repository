
def do_calculate():
    print("Welcome to Python Calculator, this is basic arithmetic calculator, you can exit the calculator by typing q at anytime")
    valid=True
    while True:
        input1=input("Enter the first number :")
        input2=input("Enter the second number :")
        try:
            input1=float(input1)
            input2=float(input2)
            prompt="Select the operation you want to perform, for Addition use +, Subration use - , Multiplication use *, Division / :"
            operation=input(prompt)
            result=0
            if operation == "+":
                result=input1+input2
            elif operation == "-":
                result=input1-input2
            elif operation == "*":
                result=input1*input2
            elif operation == "/":
                result=input1/input2
            else:
                print("Invalid operation selected, please select a valid listed operation")
                valid=False
            if valid:
                print(f"The result is : {result}")
        except Exception as e:
            print(e,",please try again")

do_calculate()