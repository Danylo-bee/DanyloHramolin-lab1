class Stadium:
    def __init__(self, spectators, name, light_power):
        self.__spectators = spectators
        self.__name = name
        self.__light_power = light_power

    def get_spectators(self):
        return self.__spectators
    def get_name(self):
        return self.__name 
    def get_light_power(self):
        return self.__light_power
    
    def set_spectators(self, spectators):
        self.__spectators = spectators
    def set_name(self, name):
        self.__name = name
    def set_light_power(self, lighr_power):
        self.__light_power = lighr_power

    def __str__(self):
        return (f"The number of spectators = {self.__spectators}, "
               f"Stadium name is {self.__name}, "
                f"Number of lighted seats: {self.__light_power}")  
      
    def __repr__(self):
        print("Calling repr")
        return self.__str__()

    def __del__(self):
        print (f"Info about {self.__name} was deleted ")   

def main():
    stadium1 = Stadium(50000, "Ukraine", 1500)            
    stadium2 = Stadium(250000, "Lviv arena", 1500)
    stadium3 = Stadium(1000, "Sil`mash", 0)

    print(stadium1)
    print(stadium2)
    print(stadium3)

main()
