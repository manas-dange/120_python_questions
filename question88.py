class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"{self.year} {self.make} {self.model}")

# Example
car = Car("Toyota", "Corolla", 2021)
car.display_details()
