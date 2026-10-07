def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def divi(x,y):
    return x/y

def calculator():
    print("Select ooperation:") 
    print("1.Add")
    print("2.Subtraction") 
    print("3.Multiply")
    print("4.Divide") 

    choice=input("Enter choice(1/2/3/4):")

    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))

    if choice == '1':
        print(f"The result is:{add(num1,num2)}")
    elif choice == '2':
        print(f"The result is:{sub(num1,num2)}")
    elif choice == '3':
        print(f"The result is:{mul(num1,num2)}")
    elif choice == '4':
        print(f"The result is:{divi(num1,num2)}")  
    else:
        print("Invalid Input")

if __name__ =="__main__":
    calculator()