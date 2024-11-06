class Stadium:
    def __init__(self, spectators, name, lighting_power):
        self.spectators = spectators 
        self.name = name 
        self.lighting_power = lighting_power 

    def display_info(self):
        print(f"Назва стадіону: {self.name}")
        print(f"Кількість глядачів: {self.spectators}")
        print(f"Потужність освітлення: {self.lighting_power} люксів")

stadium = Stadium(50000, "Олімпійський", 1500)
stadium.display_info()