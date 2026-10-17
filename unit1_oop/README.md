# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.



## Implementation Documentation

### Parent Class
I created a ParentClass to represent a vehicle. The class included a shared vehicle_type variable, a constructor that initialized the brand and model, and a display_info() method.

### Child Class and Inheritance
I implemented ChildClass using inheritance from ParentClass. I added the year and color attributes, a vehicle_category class variable, and a truck_details() method. I also overrode display_info() to provide information specific to pickup trucks.

### Namespaces
I created two truck objects to demonstrate class and instance namespaces. I accessed a class variable through both the class and an object. I also added an owner attribute to only one object and displayed their namespaces using __dict__.

### Shallow and Deep Copying
I created a dictionary containing a nested list of vehicle features. I used copy() and deepcopy() to compare copying behavior. After modifying the original list, I observed that the shallow copy reflected the change while the deep copy remained independent.

### Student-Created Extension
I added a calculate_age() method to ChildClass. This method calculated a vehicle's age using its manufacturing year and a supplied current year.

### Testing and Results
I tested the parent and child classes in main(). I also executed the namespace and copying demonstrations. The program completed successfully with exit code 0.


### Edge Case Testing and Error Handling

I added an additional test to verify how the program handled a vehicle with a future manufacturing year. I created a Ford F-150 with a manufacturing year of 2030 and tested it against the current year of 2026.

The calculate_age() method detected the invalid year and returned a descriptive error message instead of calculating a negative vehicle age.

I also verified that a valid vehicle manufactured in 2025 returned an age of one year. Both tests completed successfully, demonstrating basic input validation and improved program reliability.
