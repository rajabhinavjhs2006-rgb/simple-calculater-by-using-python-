def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def modulo(a, b):
    """Find remainder"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b

def power(a, b):
    """Calculate power"""
    return a ** b

def calculator():
    """Main calculator function"""
    print("=" * 50)
    print("      ARITHMETIC CALCULATOR")
    print("=" * 50)
    
    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Modulo (%)")
        print("6. Power (**)")
        print("7. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5/6/7): ").strip()
        
        if choice == '7':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                operations = {
                    '1': (add, '+'),
                    '2': (subtract, '-'),
                    '3': (multiply, '*'),
                    '4': (divide, '/'),
                    '5': (modulo, '%'),
                    '6': (power, '**')
                }
                
                operation_func, symbol = operations[choice]
                result = operation_func(num1, num2)
                
                print(f"\n{num1} {symbol} {num2} = {result}")
                
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        else:
            print("Invalid choice! Please select a valid operation (1-7).")

if __name__ == "__main__":
    calculator()