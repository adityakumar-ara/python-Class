# def odd(start,end):
#     for i in range(start,end):
#         if i%2!=0:
#              print(i)
# odd(20,50)             

# def even():
#     number=int(input("enter yur number"))

#     if number%2==0:
#         print("this is even ",number)
#     else:    
#         print("this is odd",number)
# even()
# def even(start,end):
#     for i in range(start,end):
#         if i%2!=0:
#              print(i)
# even(20,50)             


def ave():
          marks=[]
          number_Of_subject=int(input("NUMBER OF SUBJECT"))

          for i in range(number_Of_subject):
               subm=int(input("enter you marks"))
               marks.append(subm)
            #    print(sum(marks))
               print("total average marks",sum(marks)/len(marks))
              
ave()            