"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.


class ParentClass:
    vehicle_type = "Vehicle"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}"



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.


class ChildClass(ParentClass):
    vehicle_category = "Pickup Truck"

    def __init__(self, brand, model, year, color):
        super().__init__(brand, model)
        self.year = year
        self.color = color

    def truck_details(self):
        return f"Year: {self.year}, Color: {self.color}"

    def display_info(self):
        return f"Pickup Truck: {self.brand} {self.model} ({self.year})"

    # Student-created extension: calculate vehicle age
    def calculate_age(self, current_year):
        return current_year - self.year



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    truck1 = ChildClass("RAM", "1500", 2025, "Black")
    truck2 = ChildClass("Ford", "F-150", 2024, "Blue")

    print("Class variable:", ChildClass.vehicle_category)
    print("Class variable through object:", truck1.vehicle_category)

    truck1.owner = "Adrian"

    print("Truck 1 namespace:", truck1.__dict__)
    print("Truck 2 namespace:", truck2.__dict__)

    print("Class namespace:", list(ChildClass.__dict__.keys()))



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    # Original object with nested mutable data
    original = {
        "vehicle": "RAM 1500",
        "features": ["Bluetooth", "Navigation", "Backup Camera"]
    }

    # Shallow copy: shares the nested list with the original
    shallow_copy = copy(original)

    # Deep copy: creates an independent copy of the nested list
    deep_copy = deepcopy(original)

    print("Before modification:")
    print("Original:", original)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep_copy)

    # Modify the nested list in the original object
    original["features"].append("Heated Seats")

    print("\nAfter modification:")
    print("Original:", original)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep_copy)

    # The shallow copy reflects changes to shared nested objects.
    # The deep copy preserves its independent nested objects.



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.


def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test an object from the parent class
    print("\n=== Parent Class Demonstration ===")
    vehicle = ParentClass("Toyota", "Camry")
    print(vehicle.display_info())
    print("Vehicle type:", vehicle.vehicle_type)

    # Create and test an object from the child class
    print("\n=== Child Class Demonstration ===")
    truck = ChildClass("RAM", "1500", 2025, "Black")
    print(truck.display_info())
    print(truck.truck_details())
    print("Vehicle type:", truck.vehicle_type)
    print("Vehicle category:", truck.vehicle_category)

    # Test the student-created extension
    print("Vehicle age:", truck.calculate_age(2026), "year(s)")

    # Demonstrate namespaces and object copying
    demonstrate_namespaces()
    demonstrate_copying()



if __name__ == "__main__":
    main()