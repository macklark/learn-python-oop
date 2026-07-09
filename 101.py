class Driver:
    def __init__(self, first_name, last_name, team):
        # The following below are all attributes of our class.
        self.first_name = first_name
        self.last_name = last_name
        self.team = team

    def fullName(self):
        return "{} {}".format(self.first_name, self.last_name)


max = Driver("Max", "Verstappen", "ORBR")
charles = Driver("Charles", "Leclerc", "Ferrari")

print(max.team)
print(charles.team)
print(max.fullName())
print(charles.fullName())

# In the background this is what happens, the instance get's passed to the function as self
print(Driver.fullName(charles))
