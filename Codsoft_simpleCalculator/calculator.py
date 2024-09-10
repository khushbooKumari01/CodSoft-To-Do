print("**************************************************")
print("*                   CALCULATOR                   *")
print("**************************************************")

#code for addition
def add(x,y):
    return x+y
#code for subtraction
def sub(x,y):
    return x-y
#code for multiplication
def mul(x,y):
    return x*y
#code for division
def div(x,y):
    if y==0:
        return "Divide by Zero ! Error"
    else:
        return x/y
#operation for calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter Your Operation ")

    if choice in ['1', '2', '3', '4']:
        input1 = float(input("Enter first number: "))
        input2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{input1} + {input2} = {add(input1, input2)}")
        elif choice == '2':
            print(f"{input1} - {input2} = {sub(input1, input2)}")
        elif choice == '3':
            print(f"{input1} * {input2} = {mul(input1, input2)}")
        elif choice == '4':
            print(f"{input1} / {input2} = {div(input1, input2)}")
        else:
            print("Invalid input")


# Run the calculator
calculator()
