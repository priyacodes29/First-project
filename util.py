class Person:
    def __init__(self, name, address, gender, age):
        self.name = name
        self.address = address
        self.gender = gender
        self.age = age


persons = []

for i in range(5):
    name = input("Enter name: ")
    address = input("Enter address: ")
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))

    person = Person(name, address, gender, age)
    persons.append(person)