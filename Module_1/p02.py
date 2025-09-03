#PROBLEM 2 : Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.

def main():


    try:
        num1 = int(input("Enter First Number: "))
        op = input("Enter Operator (+,-,*,/): ")
        num2 = int(input("Enter Second Number: "))
        if num2 == 0 and op == '/':
            raise ZeroDivisionError
    except (TypeError,ZeroDivisionError):
        print("Something went Wrong!")

    ops = {
        "+": lambda x,z: x+z,
        "-": lambda x,z: x-z,
        "*": lambda x,z: x*z,
        "/": lambda x,z: x/z if z!=0 else "Cannot Devide by 0"
    }

    result = ops.get(op)(num1,num2)

    print("Result:",result)

main()