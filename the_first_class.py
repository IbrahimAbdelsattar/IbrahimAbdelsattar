#The_first_class
class names:
    not_allowed_name=["homos","balood" , "7enqesh"]
    users_num=0
    def __init__(self,first_name,second_name,last_name,gender):
        self.fname=first_name
        self.sname=second_name
        self.lname=last_name
        self.gender=gender
        names.users_num+=1
    def get_full_name(self):
        if self.fname in names.not_allowed_name:
            raise ValueError("Name not allowed")
        else:
            return f"{self.fname} {self.sname} {self.lname}"
    
    def name_with_title(self):
        if self.gender=="male":
            return f"Hello Mr {self.fname}"
        elif self.gender=="female":
            return f"Hello Miss {self.fname}"
        else:
            return f"Hello {self.fname}"
        
    def get_all_info(self):
        return f"{self.name_with_title()} ,your full name is: {self.get_full_name()}"
    
    def delete_user(self):
        names.users_num-=1
        return f" User {self.fname} is deleted"
    
    @classmethod
    def count_users(cls):
        pass

    @staticmethod
    def say_hello():
        print("Hello from the class")

print(names.users_num)
The_first_person=names("ibrahim"," abdelsattar"," abdelsattar","male")
The_second_person=names("mohamed"," abdelsattar"," abdelsattar","male")
The_third_person=names("hapipa"," abdelsattar"," abdelsattar","female")

print(The_first_person.get_all_info())
print(The_second_person.get_all_info())
print(The_third_person.get_all_info())

print(The_first_person.fname,The_first_person.sname,The_first_person.lname)
print(The_second_person.fname,The_second_person.sname,The_second_person.lname)
print(The_third_person.fname,The_third_person.sname,The_third_person.lname)

print(names.users_num)
print(The_third_person.delete_user())
print(names.users_num)
names.say_hello()

class Cars:  # Base class
    def __init__(self, type, country):
        self.type = type
        self.country = country
    @staticmethod
    def model():
        print("The model of this car is 2024")
    
    def __str__(self):
        return f"{self.type} is made in {self.country}"

class CheckCar(Cars):  # Derived class
    def __init__(self, type, country):
        super().__init__(type, country)
    

    def __str__(self):
        return f"{self.type} made {self.country}"

# Creating objects
car1 = Cars("BMW", "Germany")
car2 = CheckCar("Germany", "BMW")

# Output
print(car1)  # Output: BMW is made in Germany
print(car2)  # Output: Mercedes made in Germany

from abc import ABCMeta , abstractmethod
class programming(metaclass=ABCMeta):
    @abstractmethod
    def has_opp(self):
        pass
    @abstractmethod
    def has_name(self):
        pass

class python(programming):
    def has_opp(self):
        return "yes"
    def has_name(self):
        return "python"
    
class pascal(programming):
    def has_opp(self):
        return "no"
    def has_name(self):
        return "pascal"

one=python()
print(one.has_opp())
print(one.has_name())


from dataclasses import dataclass

class person():
    name:str= "Ibrahim Abdelsattar"
    age:int= 19
    height:float= 183.5
    email:str= "ibrahimabdelsattar042@gmail.com"

one=person()
print(one.name)
print(one.age)
print(one.height)
print(one.email)
print(pascal.mro())