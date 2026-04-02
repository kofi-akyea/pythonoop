class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time == 0:
            return 0
        return self.odometer / self.time


def main():
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?").upper()
        if action == "A":
            my_car.accelerate()
            print("Accelerating...")
        elif action == "B":
            my_car.brake()
            print("Braking...")
        elif action == "O":
            print(f"The car has driven {my_car.odometer} kilometers")
        elif action == "S":
            print(f"The average speed is {my_car.average_speed()} km/h")
        else:
            print("Invalid action. Try A, B, O, or S.")
        my_car.step()


if __name__ == "__main__":
    main()
