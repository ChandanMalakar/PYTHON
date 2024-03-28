class Car:
    """keyword pass is used for continuing to the next line"""

    # pass
    def __init__(self, dept, section='A'):
        self.name = "chandan"
        self.id = 526
        self.dept = dept
        self.section = section


car = Car("CSE", "B")

# including attributes in the class from oustide
# car.name = "chandan"
# car.id = 526

print(car.name)
print(car.id)
print(car.dept)
print(car.section)
#
# car2 = Car()
# car2.name = "chandan"
# car2.id = 526
# print(car2.name)
# print(car2.id)
