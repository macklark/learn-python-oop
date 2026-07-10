class Driver:
    # Inheritance is a property of OOP, where the variables and methods of parent class
    # can be inherited by the child class, and even override the variables or methods from child class.
    increase_wins = 1
    number_of_drivers = 0

    def __init__(self, first_name, last_name, team, wins):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.wins = wins

        Driver.number_of_drivers += 1

    def fullName(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_wins(self):
        self.wins = int(self.wins + self.increase_wins)

# Even without any variable or method being set inside F2Driver class
# just because it's being inherited from the Driver class we can use the attributes of Driver class directly
class F2Driver(Driver):
    # if increase_wins wasn't defined here then any instance using this class would take up the variable from the parent class
    # this is generally what overriding mean.
    # This changes are not mutable, and not destructive
    increase_wins = 2

    def __init__(self, first_name, last_name, team, wins, fav_track):
        # The super() let's us initiate the parent class attributes without explicitly defining them
        super().__init__(first_name, last_name, team, wins)
        self.fav_track = fav_track

class F3Driver(Driver):

    def __init__(self, first_name, last_name, team, wins):
        super().__init__(first_name, last_name, team, wins)


max = Driver('Max', 'Verstappen', 'ORBR', 71)
charles = Driver('Charles', 'Leclerc', 'Ferrari', 8)
# child class being inherited from the parent class
# since the child class accepts a extra attribute, it should also be passed
isack = F2Driver('Isack', 'Hadjar', 'ORBR', 0, 'Suzuka')

freddie = F3Driver('Freddie', 'Slater', 'Trident', 0)

print(max.fullName())
print(charles.fullName())
print(isack.fullName())
print(freddie.fullName())

# This help() function helps use visualize the Method resolution order
# which is just a fancy term of looking up the chain of class execution
# It helps use visualize the tree of class from where the current class is being inherited from
#print(help(F2Driver))

print(isack.wins)
isack.apply_wins()
print(isack.wins)

print(isack.fav_track)

# isinstance() is a method that returns a boolean if a instance is derived from a specified class or not
print(isinstance(max, Driver))
print(isinstance(charles, F2Driver))
print(isinstance(isack, F2Driver))

# issubclass() is a method that returns a boolean if a class is derived from another class or not
print(issubclass(F2Driver, Driver))
print(issubclass(F3Driver, Driver))
print(issubclass(F2Driver, F3Driver))
