my_dict = {
    "name" : "Aditya Kumar",
    "vilaage name" : "Khadaha tola",
    "age" : 28,
    "Job" : "Goverment",
}
print(my_dict.get("name"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.update({"name":"aditya kushwaha"})
print(my_dict)
my_dict.update({"age":21})
print(my_dict)
my_dict.pop("name")
print(my_dict.clear())