class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age must be positive!")
        else:
            self._age = value

# Example
person = Person("Alice", 25)
print("Age:", person.age)
person.age = 30
print("Updated Age:", person.age)
person.age = -5  # Validation logic
