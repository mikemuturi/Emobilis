class Fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def display(self):
        print(f'I love to eat {self.name} and it costs {self.price}, mostly {self.color}')

myObject = Fruits("Apple", 30.0, "Pink")

myObject.display()

myObject2 = Fruits("Mangoes", 50.0, "Yellow")
myObject2.display()

# object is a just a variable

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def display(self):
        print(f'I am {self.name}, {self.age} years old {self.gender}')

myPerson = Person("Mike Muturi", 25, "Man")

myPerson.display()
