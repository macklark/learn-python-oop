class Driver:
    increase_win = 1
    number_of_drivers = 0

    # Instance variables are unique for each instance of the class
    # for example. 'max' is a instance of Driver with first_name as 'Max' & last_name as 'Verstappen'
    # if another instance of the class is initiated for 'charles' then the variable can be unique the first_name logically should be 'Charles' & last_name as 'Leclerc'
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


max = Driver("Max", "Verstappen", "ORBR", 71)
charles = Driver("Charles", "Leclerc", "Ferrari", 8)
oscar = Driver("Oscar", "Piastri", "Mclaren", 8)

# print(max.apply_win())

# If we are trying to access a attribute from a instance, it checks if the attribute is assigened in the instance if not then it will check for the attribute in the class
# , and then in any inherited class
# That is why we can access the class variable from both the instance as well as the class
# print(Driver.increase_win)
# print(max.increase_win)
# print(charles.increase_win)

max.increase_win = 2

# print(max.__dict__)
# print(Driver.__dict__)

# print(max.increase_win)
# print(charles.increase_win)
# print(Driver.increase_win)

print(Driver.number_of_drivers)
