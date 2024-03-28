class Car:
    def __init__(self):
        self.seats = 5

    def enter_race_mode(self):
        self.seats = 2


car = Car()

print(car.seats)

car.enter_car_mode()
print(car.seats)
