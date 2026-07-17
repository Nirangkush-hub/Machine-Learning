#__init__ method can be treated as a constructor which is
#autometically created when an object is created 
#self is used to create an instance of a class(similar to "this" keyword in java)
#try and except is used so that the user while trying to input does nt inputs any other value except for numeric value
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        self.result = a / b
        return self.result

my_calc = Calculator()

try:
    while(True):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("------------------------")
        print("SIMPLE CALCULATOR:")
        print("1.ADDITION.\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT")
        print("------------------------")
        ch=int(input("Enter the operation you want to perform: "))

        if ch==1:
            print("Addition: ",my_calc.add(num1, num2))
        elif ch==2:
            print("Subtraction: ",my_calc.subtract(num1, num2))
        elif ch==3:
            print("Multiplication: ",my_calc.multiply(num1, num2))
        elif ch==4:
            print("Division: ",my_calc.divide(num1, num2))
        elif ch==5:
            break
        else:
            print("Enter a valid choice.")
except ValueError:
    print("Invalid input! Please enter numbers only.")