# class father_pro():
#     father_name = "suendra singh"
#     father_pro = "car ,'two bigha of land', water park"
# sun_obj = father_pro()
# print(sun_obj.father_pro)
# print(sun_obj.father_name)

# ----------------------------------------------------------------------------------

class employee():
    emp_name = 'Aditya kumar'
    emp_salary = 40000
    def show_detail(self):
        print(f"name:{self.emp_name}")
class manager(employee):
    department = 'IT department'
    def show_detail(self):
        print(f"department{self.department}")
emp_obj = manager()
emp_obj.show_detail()  


class employee():
    emp_name = 'Aditya kumar'
    emp_salary = 40000
    
    def show_detail(self):
        
        print(f"name: {self.emp_name}") 

class manager(employee):
    department = 'IT Department' 
    
    def show_detail(self):
     
        print(f"department: {self.department}")

emp_obj = manager()


emp_obj.show_detail()