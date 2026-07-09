class Driver:
    increase_win = 1
    number_of_drivers = 0

    def __init__(self, first_name, last_name, team, wins):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.wins = wins

        Driver.number_of_drivers += 1

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def apply_win(self):
        return int(self.wins + self.increase_win)

    # generally a method defined under a class takes in the instance as it's first parameter
    # but a class method makes sure that the method takes in the class itself as it's first parameter
    @classmethod
    def set_increase_win(cls, new_win):
        cls.increase_win = new_win

    # There is a way to use classmethods as alternate constructors, they can be returned using the default cls parameter
    @classmethod
    def from_string(cls, driver_str):
        first_name, last_name, team, wins = driver_str.split("-")
        return cls(first_name, last_name, team, wins)


max = Driver("Max", "Verstappen", "ORBR", 71)
charles = Driver("Charles", "Leclerc", "Ferrari", 8)
oscar = Driver("Oscar", "Piastri", "Mclaren", 8)

Driver.set_increase_win(2)

driver_str_george = "George-Russel-Mercedes-6"
driver_str_lewis = "Lewis-Hamilton-Ferrari-106"

print(Driver.number_of_drivers)

# print(Driver.increase_win)
# print(max.increase_win)
# print(charles.increase_win)
# print(oscar.increase_win)

Driver.from_string(driver_str_george)
Driver.from_string(driver_str_lewis)
