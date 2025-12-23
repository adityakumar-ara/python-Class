# class teacher:
#          a = 10
# class student(teacher):
#          b = 20
# student_obj = student()
# print(student_obj.b)
# print(student_obj.a)

# class student:
#     name = "aditya"
#     card_no = 25011
#     def student_info(self):
#         print("this student will be present tomorry")
# class teacher(student):
#      name = "raj kumar"
#      card_no = 2345
#      def teacher_info(self):
#          print("the theacher will be opsent today")
# teache_obj = teacher()
# print(teacher.name)       
# 
# 

# class Student:
#     name = "Aditya"

#     def info(self):
#         # यहाँ सिर्फ print(name) काम नहीं करेगा
#         print(self.name)    
# student_obj = Student()
# student_obj.info()        



# ______________________________________________Multiple Inheritence_____________________________________________________


class ram_father :
              property_of_father = "car, house , chocolate factory"
class ram :
        property_of_ram = "milk factory","rice factory"              

class sun_of_ram(ram_father ,ram) :
            property_of_sun = "sugar factory"

sun_obj = sun_of_ram()  
print(sun_obj.property_of_father)          
print(sun_obj.property_of_ram)          
print(sun_obj.property_of_sun)          