# Function to add Two Numbers
def add(x, y):
    """Returns the sum of x and y."""
    return x + y
# Function to subtract Two Numbers
def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y
# Function to add Multiply Numbers
def multiply(x, y):
    """Returns the product of x and y."""
    return x * y
# Function to add Divide Numbers
def Divide(x, y):
    if y == 0:
        return "Error! Divivsion by zero not allowed"
    else:
        return x/ y
    
def Calculator():
        print("Select Operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

while True:
      # Take input from the user
      Choice = input("Enter choices (1/2/3/4)")
      # Check the input is one of the four options
      if Choice in ['1','2','3','4']:
           num1= float(input("Enter first number"))
           num2 = float(input("Enter second number"))
      if Choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
      if Choice == '2':
           print(f"{num1} - {num2} = {subtract(num1, num2)}")   
      if Choice == '3':                  
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
      if Choice == '4':
              print(f"{num1} / {num2} = {Divide(num1, num2)}")         
       # Option to exit the loop
      next_calculation = input("Do you want to perform another calculation? (yes/no): ")
      if next_calculation.lower() != 'yes':
        break       
      print("Thank you for using the calculator!")
      # End of the Calculator Function
      Calculator()  # Call the Calculator function to start the program