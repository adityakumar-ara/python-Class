my_dict = {
    "name" : "Aditya Kumar",
    "vilaage name" : "Khadaha tola",
    "age" : 28,
    "Job" : "Goverment",
}
# print(my_dict.get("name"))
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# my_dict.update({"name":"aditya kushwaha"})
# print(my_dict)
# my_dict.update({"age":21})
# print(my_dict)
# my_dict.pop("name")
# print(my_dict.clear())

# ---------------------------string method empliy in dect---------------------------------------

# print(my_dict.get("name").upper())

# for key in my_dict.keys():
#  print(key.upper())

# for value in my_dict.values():
#   print(str(value).upper()) 

for value in my_dict.values():
  if isinstance(value,str):
    print(value.upper())
  else:
    print(value) 