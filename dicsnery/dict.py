# # print("hello")
# c
#     "city": "Bangalore",
#     "roll_no": 101
# }
# # my_dict.update({"name":"aditya"})
# # print("name is:",my_dict["name"].upper())
# # print("name is:",my_dict.get("name").upper())
# # print("name is:",my_dict.get("age"))
# # print("name is:",my_dict.pop("age"))
# # print("name is:",my_dict.pop("name"))
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# -------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------------------------------
# student_result={}
# while True:
#     print("when wnant you exit then write exit")
#     key=input("enter key")
#     if key.lower()=='exit':
#           break
#     value=input(f"enter value for {key}")
#     student_result[key]=value
# print("student result",student_result)

# -------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------------------------------

# user_dict = {}
# n = int(input("How many entries do you want to add? "))

# for i in range(n):
#     key = input(f"Enter key {i+1}: ")
#     value = input(f"Enter value for {key}: ")
    
#     user_dict[key] = value

# print("\nYour Dictionary:", user_dict)

# <<<<<<<<<<--------using list and dict-------------->>>>>>>>>>>>

# my_library=[
#    {"Book_name": "Python Programming", "price": 500 ,"quantity":2},
#    {"Book_name": "Data Science", "price": 700 , "quantity": 2}
# ]
# print(my_library)
# while True:
#     print("1.add Book")
#     print("2.book essues")
#     print("3.you want do you exit")

#     user_input=int(input("choose"))
#     if user_input==1:
#       print("welcome to add book")
#       n=int(input("enter yur number of book"))
#       for i in range(n):
#         Book=input("enter Book name:")
#         price=int(input("enter price :"))
#         quantity=int(input("enter quantity :"))
#         books={
#                  "Book_name":Book,
#                  "price":price,
#                  "quantity":quantity
#               }
#         my_library.append(books)
#         print("-----Book added successfully-----")
#         print(my_library)
#     elif user_input==2:
#        print("welcome to issue book")
#        if len(my_library )==0:
#           print("Not book available")
#        else:
#            print(my_library) 
#            print("-------------------------------------------------------------------")
#            input_book_name=input("enter your book name")
#            for book in my_library:
#             if book["Book_name"] == input_book_name:
#                   n=int(input("enter how many books you want to issue"))
#                   if book["quantity"] >= n:
#                    book["quantity"]-=n
#                    print("-----Book issue successfull")
#                    print("my_library after issuing:", my_library)
#                   else:
#                      print(f"Book availeble {book['quantity']}")
#                   break
#             # else:
#             #    print("invalid book name")
#            else:
#             print("invalid book name")
#     elif user_input == 3:
#         break         
#     else:
#        print("your number is wrong pzl enter write number")