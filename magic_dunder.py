class Driver:
    increase_wins = 1
    number_of_drivers = 0

    def __init__(self, first_name, last_name, team, wins):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.wins = wins

    def fullName(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # __repr__ is a special method which returns a meaningful string when the object is called upon through class
    def __repr__(self):
        return "Driver('{}', '{}', '{}', {})".format(self.first_name, self.last_name, self.team, self.wins)

    # __str__ is a special method which is also used to return something meaningful as a string
    def __str__(self):
        return "{} -> {}".format(self.fullName(), self.team)

    def __add__(self, other):
        return int(self.wins + other.wins)

max = Driver('Max', 'Verstappen', 'ORBR', 71)
charles = Driver('Charles', 'Leclerc', 'Ferrari', 8)

print(max) # __repr__ -> Driver('Max', 'Verstappen', 'ORBR', 71) & __str__ -> Max Verstappen -> ORBR & either of them are not defined in the class then <__main__.Driver object at 0x109066fd0>

# Alternatives

print(repr(max))
print(str(max))

# which is basically

print(max.__repr__())
print(max.__str__())

print(3 + 16) # whenever we say something like this, the addition operation is carried out using a special method called __add__()
print('M' + 'C')

print(int.__add__(3, 16)) # 19
# In the same way
print(str.__add__('M', 'C')) # MC

# This is because we've a special dunder method in our class __add__() which is returning the sum of both the drivers wins
print(max.wins + charles.wins) # 79
