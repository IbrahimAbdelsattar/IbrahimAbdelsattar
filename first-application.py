# Simple calculator with loop

def calculator():
    while True:
        print("Hello :)\n")
        print("This is a simple calculator to calculate two numbers\n")
        x = int(input("Please enter the first number\n"))
        y = int(input("Please enter the second number\n"))
        opr = input("""Please choose the operator: "add", "sub", "mult", "div"\n""")
        
        if opr.lower() == "add":
            result = x + y

        elif opr.lower() == "sub":
            result = x - y

        elif opr.lower() == "mult":
            result = x * y

        elif opr.lower() == "div":
            if y == 0:
                result = "Error: Division by zero is not allowed."
            else:
                result = x / y

        else:
            result = "Invalid operator entered."
        
        print(f"Result: {result}")
        
        again = input("Do you want to calculate again? (yes to continue, stop to exit)\n")
        if again.lower() == "stop":
            print("Thank you for using the calculator!")
            break  
        
calculator()
