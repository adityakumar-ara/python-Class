# print("Hell world")
# #arithmetic opreater
# a=4
# b=8
# print("sum is",a+b )
# print("subtraction",a-b)
# print("multiplai",a*b)
# print("Division",a/b)
# print("flooe division", a//b)
# print("modulus",a%b)
# #assignment opwrater
# a=5
# b=10
# print("sum is",a+b)
# a+=b
# print("sum is",a)
# a-=b
# print("subtraction is",a)
# a-=b
# print("division",a)
# a//=b
# print("floor devision",a)
# a%=b
# print("modulus is",a)
# a*=b
# print("maltiplication",a)
# #coparison operator
# a=5
# b=10
# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)
# print(a>=b)
# print(a<=b)
# ##logical operator
# a=5
# b=10
# #and operator
# print(a==b and a<b)
# print(b>=a and a<=b)
# #or operator
# print(a<b or b>a)
# print(a>=b or b<=a)
# #input function
# first_name=input("enter your first name")
# last_name=input("inter your last name")
# your_full_name=first_name +" "+last_name
# print("your full name is",your_full_name)
# #Bitwise operator
# a=8
# b=9
# #Bitwise and operator
# print(a&b)

# #Bitwise or operator
# print(a|b)

# #Bitwise xor operator
# print(a^b)

# #Membership operatop
# Number=[1,2,3,4,5,6]
# print(5 in Number)
# print(7 in Number)
# #string concetenation("+")
# first_name="aditya"
# last_name="kumar"
# full_name=first_name+' '+last_name
# print("full name is",full_name)
# #string replication
# print(first_name*9)


# ##2nd parameter
# ##indexing 
# #possitive indexing
# name="aditya" #a=1,d=2,i=3,t=4,y=5,a=6
# print(name[:])
# print(name[0:3])
# print(name[3:6])
# print(name[0:])

# ## negative indexing
# name="aditya" #a=-6,d=-5,i=-4,t=-3,y=-2,a=-1
# print(name[:])
# print(name[-3:-1])
# print(name[-6:-1])
# print(name[-6:])


# #3rd parameter
# name="adityakumar"
# print(name[0: :2])
# print(name[2: :3])
# print(name[:-1:2])#

# ##coditional statement
# a=2
# n=3
# if a<n:
#     print("a is less than to n")
# else:
#     print("a is less than to b")  

# age=int(input("hello,there enter your age"))
# Resident=input("enter you resident").title()
# if age>=18 and Resident=="Bihar":
#     print("you they can vote, there in bihar")
# elif age<18 and Resident=="Bihar":
#    print("you are not eligible for vote,because only they can vote 18+ ")
# else:
#   print("you are not eligible for vote, there in bihar ")   

# User_name=input("enter your User_name")
# Password=input("enter your password")
# if User_name=="aditya" and Password=="06/06/2006":
#         print("login sucsses full")
# elif User_name=="aditya" and Password=="06/06/06":
#       print("sorry, your password is wrong")
# else:
#        print("please enter your curect User_name and password")


# a=int(input("Enter you number"))
# if(a%2==0):
#   print("this is not odd number")
# else:
#   print("this is odd number")  
 
# proccess = "admition"
# marks_of_10th = int(input("Enter your marks of 10th (0-500): "))
# if marks_of_10th > 500 and marks_of_10th < 0:
#     print("Please enter your 10th marks between 0 and 500")
# elif marks_of_10th >= 300:
#     marks_of_12th = int(input("Enter your 12th marks (0-500): "))
#     if marks_of_12th > 500 and marks_of_12th < 0:
#         print("Please enter your 12th marks between 0 and 500")
#     elif marks_of_12th >= 300:
#         id_card = input("Do you have PAN card yes/no: ").strip().lower()
#         if id_card == "yes":
#             print("Congrats! you are eligible for admission")
#         else:
#             print("You are not eligible (PAN card required)")
#     else:
#         print("You are not eligible (12th marks below required threshold)")
# else:
#     print("You are not eligible (10th marks below required threshold)")