# Python Program using function to make a simple calculator
# Python using while loop 
# Python using if, elif, else statement

def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    return(x//y)        # this // operator will give integer numbers not float

# To Evaluate the one1 and two2 in this operation
one1 = eval(input("Enter your first number: "))
two2 = eval(input("Enter your second number: "))

print("==============================================")
print("Select the option ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
print("==============================================")

while(True):
    choice = int(input("Enter the choice from (1/2/3/4/5):-->"))
    if choice in (1,2,3,4,5):
        if choice == 1:
            print("Addition of two numbers",one1, "and",two2,"is:-->",add(one1,two2))
        elif choice == 2:
            print("Subtraction of two numbers",one1, "and",two2,"is:-->",subtract(one1,two2))
        elif choice == 3:
            print("Multiplication of two numbers",one1, "and",two2,"is:-->",multiply(one1,two2))
        elif choice == 4:
            print("Division of two numbers",one1, "and",two2,"is:-->",divide(one1,two2))
        if choice == 5:
            print("Thank you for trying it: ")
            exit()      # to terminate the operation of choice
    else:
        print("Invalid choice you made their Please try again! ")