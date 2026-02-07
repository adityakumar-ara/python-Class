# def sum(a,b):
#     return  a+b

# print(sum(2,3))

# def sub(a,b):
#     return a-b
# print("subtraction is :",sub(3,2))
# print("subtraction is :",sub(8,10))


# a= int (input("enter first number:"))
# b = int (input("Enter second number:"))
# def sub(a,b):
#     return a-b
# print("subtraction is :",sub(a,b))

print("<<<--welcome to calculator-->>>")
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication (a,b):
    return a*b
def Divison(a,b):
    return a,b
def Reminder(a,b):
    return a % b
a = int (input("Enter your first number:"))
b = int (input("Enter your second number:"))
c = input("please enter (+,-,*,/,%):")
if (c == '+'):
    print("addititon",addition(a,b)) 
elif (c == '-'):
    print("subtraction",subtraction(a,b)) 
elif (c == '*'):
    print("Multiplication",multiplication(a,b))  
elif(c == '/'):
    print("Divison",Divison(a,b))  
elif (c == '%'):
    print("Reminder",Reminder(a,b))           
else:
    print("inviled your choise")    