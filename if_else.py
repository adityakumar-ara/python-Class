instagram="login"
user_name="rajkumar@1223"
password="rajkumar@bihar"
input_username=input("enter your user_name:")
input_password=input("enter your password:")
if input_username==user_name and input_password==password:
    print("login successfull")
elif input_username==user_name and input_password!=password:
    print("password is wrong")
elif input_username!=user_name and input_password==password:
    print("user name is wrong is wrong")       

else:
    print("inviled username and password")

process = "admission"
marks_of_10th = int(input("Enter your 10th marks: "))
if marks_of_10th > 500 or marks_of_10th < 0:
    print("pythonInvalid marks! Please enter marks between 0 to 500.")
else:
    marks_of_12th = int(input("Enter your 12th marks: "))
    if marks_of_12th > 500 or marks_of_12th < 0:
        print("Invalid marks! Please enter marks between 0 to 500.")
    else:
        if marks_of_10th >= 300 and marks_of_12th >= 300:
            id = input("Do you have a PAN card (yes/no): ").lower()
            if id == "yes":
                print("Congrats! You are eligible for admission.")
            else:
                print(" You need a PAN card for admission.")
        else:
            print(" You are not eligible (marks too low).")

result="marks"
name="Rahul Kumar" #math=70,hindi=80,science=67,sanskrit=68,social science=89
Role_code="73069"
Role_number="2200150"

name="Kunal Kumar" #math=60,hindi=45,science=60,sanskrit=68,social science=46
Role_code="73069"
Role_number="2200151"

name="Aditya Kumar" #math=77,hindi=88,science=67,sanskrit=65,social science=89
Role_code="73069"
Role_number="2200152" 

name="Rani Kumari"  #math=70,hindi=74,science=57,sanskrit=68,social science=80
Role_code="73069"
Role_number="2200144"
input_name = input("enter your name: ")
input_Role_code = int(input("enter your role code: "))
input_Role_number = int(input("enter your roll number: "))

if input_name == "kunal kumar" and input_Role_code == 73069:
    if input_Role_number == 2200150:
        print("your marks is 189")
    else:
        print("invalid roll number")
else:
    print("plz enter viled input")



