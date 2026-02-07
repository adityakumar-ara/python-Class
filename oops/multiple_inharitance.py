class grandfather():
    name = 'Ramvachan singh'
    father_name = "XYZ singh"
    village_name ='hardiya'
    Pin_code = 802152
    Income_source = 'farmer'
    DOB = '2/1/1902'
    def info_of_grandfather(self):
        print(f"name{self.name}")
        print(f"father name:{self.father_name}")
        print(f"village name:{self.village_name}")
        print(f"pin code: {self.Pin_code}")
        print(f"income source: {self.Income_source}")
        print(f"date of birth: {self.DOB}")
class father_info():
    name = 'Surendra singh'
    father_name = 'Ramvachan singh'
    village_name = 'Hardiya'
    pin_code = 802152
    Income_source = 'Farmer'
    DOB = '1/1/1980'
    def info_of_father(self):
        print(f'name {self.name}')
        print(f'father name:  {self.father_name}')
        print(f'village name: {self.village_name}')
        print(f'pic code: {self.pin_code}')
        print(f'income source: {self.Income_source}')
        print(f'date of birth: {self.DOB}')
        print('-------------------------------------------------------------')
class aditya_info(father_info , grandfather):
    name = 'Aditya Kumar'
    Father_name = 'Surenda singh'
    village_name = 'Hardiya'
    Pin_code = 802152
    job = 'GOV.'
    salary = 50000
    DOB = '6/6/2006'
    def info_of_aditya(self):
        print(f"name:{self.name}")
        print(f"Father_name:{self.Father_name}")
        print(f"Village_name:{self.village_name}")
        print(f"pin_code:{self.Pin_code}")
        print(f"Job:{self.job}")
        print(f"salary:{self.salary}")
        print(f"date of birth:{self.DOB}")
        print('-------------------------------------------------------------')
my_obj = aditya_info()
my_obj.info_of_aditya()
my_obj.info_of_father()
my_obj.info_of_grandfather()