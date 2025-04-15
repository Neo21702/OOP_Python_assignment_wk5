# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}, and I use my power of {self.power}!"

    def fight_crime(self):
        return f"{self.name} is fighting crime using {self.power} 💥"

# Subclass with inheritance
class Supervillain(Superhero):
    def __init__(self, name, power, city, evil_plan):
        super().__init__(name, power, city)
        self.evil_plan = evil_plan

    def introduce(self):
        return f"I am {self.name}, and {self.evil_plan} will soon succeed in {self.city}! 😈"

    def fight_hero(self):
        return f"{self.name} is battling a hero with {self.power}!"

# Create objects
hero = Superhero("PhotonMan", "light speed", "Metropolis")
villain = Supervillain("DarkFlame", "shadow manipulation", "Metropolis", "total darkness")

# Run some methods
print(hero.introduce())
print(hero.fight_crime())
print(villain.introduce())
print(villain.fight_hero())
