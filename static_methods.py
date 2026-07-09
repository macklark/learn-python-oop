class Driver:
    increase_win = 1
    number_of_drivers = 0

    def __init__(self, first_name, last_name, team, wins):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.wins = wins

        Driver.number_of_drivers += 1

    # static methods do not take either the instance or class as a parameter, they are jack of all trades
    # when should I use a static method ?
    # when there is no requirement for a class or instance variable from constructor
    @staticmethod
    def is_driver_a_legend(number_of_wins):
        if number_of_wins > 50:
            return True
        return False


max = Driver("Max", "Verstappen", "ORBR", 71)
charles = Driver("Charles", "Leclerc", "Ferrari", 8)
oscar = Driver("Oscar", "Piastri", "Mclaren", 8)
lewis = Driver("Lewis", "Hamilton", "Mercedes", 108)

print(Driver.is_driver_a_legend(max.wins))
print(Driver.is_driver_a_legend(charles.wins))
print(Driver.is_driver_a_legend(oscar.wins))
print(Driver.is_driver_a_legend(lewis.wins))
