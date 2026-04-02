# lab_week5.py
# Week 6 Lab: Inheritance, super(), **kwargs, Multiple Inheritance, Polymorphism


# Exercise 1: Simple Inheritance


class Vehicle:
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = max_range
        self.seats = seats

    def move(self, speed):
        print(f"The vehicle is moving at {speed} km/h")


class Car(Vehicle):
    def __init__(self, colour, weight, max_speed, form_factor, **kwargs):
        super().__init__(colour, weight, max_speed, **kwargs)
        self.form_factor = form_factor

    def move(self, speed):
        print(f"The car is driving at {speed} km/h")



# Exercise 2: super() — Electric and Petrol subclasses


class Electric(Car):
    def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed):
        range_info = f" with a maximum range of {self.max_range} km" if self.max_range else ""
        print(f"The electric car is driving at {speed} km/h{range_info}")


class Petrol(Car):
    def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed):
        range_info = f" with a maximum range of {self.max_range} km" if self.max_range else ""
        print(f"The petrol car is driving at {speed} km/h{range_info}")



# Exercise 3: **kwargs — Plane hierarchy


class Plane(Vehicle):
    def __init__(self, colour, weight, max_speed, wingspan, **kwargs):
        super().__init__(colour, weight, max_speed, **kwargs)
        self.wingspan = wingspan

    def move(self, speed):
        print(f"The plane is flying at {speed} km/h")


class Propeller(Plane):
    def __init__(self, colour, weight, max_speed, wingspan, propeller_diameter, **kwargs):
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.propeller_diameter = propeller_diameter

    def move(self, speed):
        print(f"The propeller plane is flying at {speed} km/h")


class Jet(Plane):
    def __init__(self, colour, weight, max_speed, wingspan, engine_thrust, **kwargs):
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.engine_thrust = engine_thrust

    def move(self, speed):
        print(f"The jet is flying at {speed} km/h")



# Section 3: Multiple Inheritance — FlyingCar


class FlyingCar(Car, Plane):
    def __init__(self, colour, weight, max_speed, form_factor, wingspan, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor=form_factor,
                         wingspan=wingspan, **kwargs)

    def move(self, speed):
        print(f"The flying car is driving or flying at {speed} km/h")



# Section 4: Polymorphism — Animal + polymorphic loop


class Animal:
    def move(self, speed):
        print(f"The animal is moving at a speed of {speed}")



# Main — create objects and demonstrate everything


if __name__ == "__main__":
    # Exercise 1
    generic_vehicle = Vehicle("red", 1000, 200)
    generic_vehicle.move(100)

    car = Car("blue", 1500, 250, "SUV")
    car.move(150)

    # Exercise 2 — max_range in move message
    electric_car = Electric("green", 1200, 200, "Hatchback", 100, max_range=400)
    electric_car.move(100)

    petrol_car = Petrol("red", 1500, 250, "SUV", 50, max_range=600)
    petrol_car.move(150)

    # Exercise 3 — **kwargs + seats + Plane hierarchy
    generic_electric_car = Electric("red", 1000, 200, "SUV", 100, max_range=500, seats=5)
    generic_electric_car.move(100)
    print(f"Seats: {generic_electric_car.seats}")

    propeller_plane = Propeller("white", 800, 300, 12.5, 2.0, max_range=800)
    propeller_plane.move(200)

    jet_plane = Jet("grey", 15000, 900, 30.0, 150.0, max_range=5000, seats=180)
    jet_plane.move(850)

    # Multiple inheritance
    generic_flying_car = FlyingCar("red", 1000, 200, "SUV", 30, seats=5)
    generic_flying_car.move(100)
    print(f"Seats: {generic_flying_car.seats} | Wingspan: {generic_flying_car.wingspan} m")

    # Polymorphism
    generic_animal = Animal()
    generic_animal.move(20)

    print("\n--- Polymorphic loop ---")
    for movable_object in [generic_vehicle, generic_electric_car, generic_flying_car, generic_animal]:
        movable_object.move(20)
