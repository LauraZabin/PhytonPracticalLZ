# 1.Create a class named Car that has the following attributes: make, model, and year. 
# It should also have a method called get_info() that returns a string with the car's make, model, and year.



# class Car:
#     
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def say_car(self):
#         print(f"Car was made by:{self.make}, model: {self.model}, year: {self.year} ({self.engine})")

# # --------

# Car_1 = Car("Toyota", "Avensis", 2006)
# Car_2 = Car("BMW", "X3", 2023)

# Car_2.say_car()
# Car_1.say_car()


# 2.Create a class named Rectangle that has the following attributes: width and height. 
# It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, respectively.

# class Rectangle:
#     def __init__(self, width, height):
#          self.width = width
#          self.height = height 

#     def area(self):
#          plotas=self.width * self.height
#          return plotas
    
#     def perimeter(self):
#          peri = 2 * (self.width + self.height)
#          return peri
    
# def print_Rectangles(staciakampis:Rectangle):
#      print(f"Area of reactangle is: {staciakampis.area()} and its perimeter is: {staciakampis.perimeter()}")
    
# Rec_1 = Rectangle(7, 6)
# Rec_2 = Rectangle(8, 11)

# print_Rectangles(Rec_1)
# print_Rectangles(Rec_2)

# 3.Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name. 
# It should also have methods called deposit() and withdraw() that update the balance accordingly.

# class BankAccount:
#     def __init__(self, account_number, balance, owner_name):
#          self.account_number = account_number
#          self.balance = balance
#          self.owner_name = owner_name

#     def deposit(self):
#         amount=int(input("Enter amount to be Deposited: "))
#         self.balance += amount
        
          
#     def withdraw(self):
#         amount = int(input("Enter amount to be Withdrawn: "))
#         if self.balance>=amount:
#             self.balance-=amount
#         else:
#             print("\n Insufficient balance  ")
 
#     def New_balance(self):
#         print("Account number " + self.account_number + " of " + self.owner_name + " New Balance=",self.balance)


# My_acc = BankAccount("LT11 3000 4000 5000 6000", 20, "Laura")
# My_acc.deposit()   
# My_acc.withdraw()
# My_acc.New_balance()


# 4.Create a class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address.

# class Person:
#     def __init__(self, name, age, address):
#          self.name = name
#          self.age = age
#          self.address = address

#     def __str__(self):
#          return f"{self.name}, {self.age},{self.address}"

# p1 = Person("Laura", 40, " Upes st. Vilnius")    
# p2 = Person("Lina", 30, " Juros st. Vilnius")
# p3 = Person("Laima", 20, " Pilies st. Vilnius")
# print(p1)
# print(p2)
# print(p3)


# 5.Create a class named Animal that has the following attributes: name and species. 
# It should also have a method called speak() that returns a string with the animal's sound.

# class Animal:
#     def __init__(self, name, species):
#          self.name = name
#          self.species = species
#     def speak(self):
#         if self.species == "Dog":
#             speaks = "Woof woof"
#         elif self.species == "Cat":
#             speaks ="Meooow"
#         else:
#             speaks = "No such sound in database :)"
#         return speaks
#     def print(self):
#         print(f"animal {self.species}, name: {self.name}, sounds: {self.speak()}  ")
        
            
# animal_1 = Animal("Amsis", "Dog")
# animal_2 = Animal("Rainis", "Cat")
# animal_3 = Animal("Tractor", "Horse")

# animal_3.print()


# 8.Write a Python program that reads a JSON file containing a list of dictionaries, 
# sorts the list by a specific key, and writes the sorted list back to the file.

# import json

# data = [{"name": "Arturs", "last_name": "Olekss", "age": 25},
#  {"name": "Jack", "last_name": "Sparrow", "age": 35}, {"name": "Michael",
#   "last_name": "Peters", "age": 56}, {"name": "Leo", "last_name": "Valdara", "age": 34}]

# # with open("data.json", "w") as f:
# #  json.dump(data, f)

# with open("data.json", "r") as f:
#  data = json.load(f)

# data_sort = sorted(data, key = lambda x: x['age']) 

# with open("data.json", "w") as f:
#  json.dump(data_sort, f)


# 9.Write a Python program that reads a CSV file containing student grades, calculates their average score, and writes the average to a new file. 

# import csv
# from statistics import mean
# with open("student.csv", "r") as f:
#     reader = csv.reader(f, delimiter=';')
#    # print(mean([float(i[1]) for i in reader if i[1].isnumeric()]))
#     A = mean([float(i[1]) for i in reader if i[1].isnumeric()])
# print(A)

# with open("student_average.csv", "w", newline='') as f:
#     csvlines = csv.writer(f, delimiter=';')
#     csvlines.writerow(['Average', A])
   

# 10.Write a Python program that reads a CSV file containing student grades and
# writes a new CSV file with the grades sorted by student name.

# import csv

# with open("student_grades.csv", "r") as f:
#     reader = csv.reader(f, delimiter=',')
#     csv_list = list(reader)
#     csv_sorted_list = sorted(csv_list, key=lambda d: d[1])    
# # print(csv_sorted_list)

# with open("Students_by_names.csv", "w") as f:
#     f.writelines(str(csv_sorted_list))


# 7.Create a base class named Person that has the following attributes: name, age, and address.
# It should also have a method called get_info() that returns a string with the person's name, age, and address. 
# Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes and methods specific to each role.    

class Person:
   def __init__(self, name, age, address):
          self.name = name
          self.age = age
          self.address = address

   def __str__(self):
        return f"{self.name}, {self.age},{self.address}"
   
class Student(Person):
     def __init__(self, name, age, address, lname):
          super().__init__(name, age, address)   
          self.last_name = lname

     def welcome(self):
          print("Welcome", self.name, self.last_name)     

# p1 = Person("Laura", 40, " Upes st. Vilnius")    
# p2 = Person("Lina", 30, " Juros st. Vilnius")
# p3 = Person("Laima", 20, " Pilies st. Vilnius")

p1 = Student("Laura", 40, " Upes st. Vilnius", "Gile")
p2 = Student("Lina", 30, " Juros st. Vilnius", "Bude")
p3 = Student("Laima", 20, " Pilies st. Vilnius", "Vale")
print(p1.welcome())
print(p2.welcome())
print(p3.welcome())