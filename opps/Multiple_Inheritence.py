# ______________________________________________Multiple Inheritence_____________________________________________________


# class ram_father :
#               property_of_father = "car, house , chocolate factory"
# class ram :
#         property_of_ram = "milk factory","rice factory"              

# class sun_of_ram(ram_father ,ram) :
#             property_of_sun = "sugar factory"

# sun_obj = sun_of_ram()  
# print(sun_obj.property_of_father)          
# print(sun_obj.property_of_ram)          
# print(sun_obj.property_of_sun)          


# class father:
#     father_name= "surender singh"
# class mother:
#     mother_name = "phulkimari devi"
# class son (father , mother):
#      son_name = "aditya"
# son_obj = son()
# print(son_obj.father_name)            
# print(son_obj.mother_name)  
# 

# -------------------------------------------------------------------------------------------
# class grandfather:
#       property_of_grandfather = "milk_van , car,bus"
# class father:
#       father_property = "shoes factory"   
# class son(father,grandfather) :
#       son_property = "daily milk"  

# son_obj = son()
# print("property of granfahter:", son_obj.property_of_grandfather)
# print("property of granfahter:", son_obj.father_property)
# print("property of granfahter:", son_obj.son_property)