from pakuri import *
class Pakudex:
    #initialize pakudex
    def __init__(self, capacity=20):
        self.pakudexlist = []
        self.capacity = capacity
    
    #gets size of pakudex by getting the length of the pakudex list and returns it
    def get_size(self):
        size = len(self.pakudexlist)
        return size
    #returns self capacity which was initialized in __init__
    def get_capacity(self):
        return self.capacity
    #if the pakudex is empty returns None, else returns the pakudex list
    def get_species_array(self):
        if self.pakudexlist == []:
            return None
        else:
            return self.pakudexlist
    #if species not in the pakudex returns none, else returns a list of the pakuri stats
    def get_stats(self, species):
        if species not in self.pakudexlist:
            return None
        else:
            pakuri = Pakuri(species)
            stats_list = [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
            return stats_list
    #sorts pakuri list
    def sort_pakuri(self):
        self.pakudexlist.sort()
    #adds pakuri to pakudex if capcity is not full and it is not already in pakudex
    def add_pakuri(self, species):
        if len(self.pakudexlist) >= self.capacity:
            return False
        if species in self.pakudexlist:
            return False
        else:
            pakuri_species = Pakuri(species)
            self.pakudexlist.append(pakuri_species.get_species())
            return True
    #if species is in the pakudex return true else return false
    def evolve_species(self, species):
        if species in self.pakudexlist:
            return True
        else:
            return False