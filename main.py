import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.progress = 0
        self.money = 10
        self.alive = True

    def to_study(self):
        print("Studying...")
        self.progress += 0.12
        self.gladness -= 3
        self.money -= 1

    def to_sleep(self):
        print("Sleeping...")
        self.gladness += 3

    def to_chill(self):
        print("I will rest today")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 5

    def to_work(self):
        print("Working")
        self.gladness += 5
        self.money += 10

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed exams")
            self.alive = False

    def day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")
        print(f"Money - {round(self.money, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1 and self.money > 5:
            self.to_study()
        elif live_cube == 2 and self.money > 5:
            self.to_sleep()
        elif live_cube == 3 and self.money > 5:
            self.to_chill()
        elif live_cube == 4 or self.money <= 5:
            self.to_work()
        self.day()
        self.is_alive()


person = Student("Pavlo")

for day in range(1, 366):
    if person.alive == False:
        break
    person.live(day)