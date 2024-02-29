class Pakuri:
    #initializes species and sets attack speed and defense stats
    def __init__(self, species):
        self.species = species
        self.attack = (len(self.species) * 7)+9
        self.defense = (len(self.species) * 5) + 17
        self.speed = (len(self.species) * 6) + 13
    #returns species
    def get_species(self):
        return self.species
    #returns attack
    def get_attack(self):
        return self.attack
    #returns defense
    def get_defense(self):
        return self.defense
    #returns speed
    def get_speed(self):
        return self.speed
    #sets self.attack to new attack
    def set_attack(self, new_attack):
        self.attack = new_attack
    #evolves stats
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3