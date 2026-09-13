people_list = []

class Person:
    def __init__(self, name, age, address, course, city):
        self.name = name
        self.age = age
        self.address = address
        self.course = course
        self.city = city


for i in range(5):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    course = input("Enter your course: ")
    city = input("Enter your city: ")

    person = Person(name, age, address, course, city)

    people_list.append(person)