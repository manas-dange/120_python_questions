class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says 'Woof!'")

# Example
animal = Animal("Generic Animal")
dog = Dog("Buddy")
animal.speak()
dog.speak()