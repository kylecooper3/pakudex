from pakudex import *
from pakuri import *

#define menu
def menu():
    print('Pakudex Main Menu')
    print('-----------------')
    print('1. List Pakuri')
    print('2. Show Pakuri ')
    print('3. Add Pakuri')
    print('4. Evolve Pakuri')
    print('5. Sort Pakuri')
    print('6. Exit')
    print('')

#define main
def main():
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    while True:
        try:        #tries input for max capicty, if negative or non int raises ValueError
            max_capacity = int(input('Enter max capacity of the Pakudex: '))
            if max_capacity < 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('Please enter a valid size.')
    pakudex = Pakudex(max_capacity)     #initalizes Pakudex class as pakudex
    print(f'The Pakudex can hold {max_capacity} species of Pakuri.')
    print('')
    while True:
        menu()
        while True:
            try:            #tries menu inputs, if it is not 1-6 an Error is raised either by excepting value error or an elif statement later in the function
                option = int(input('What would you like to do? '))
                break
            except ValueError:
                print('Unrecognized menu selection!')
                print('')
                menu()
        if option == 1:     #if option is 1 print nothing in pakudex if it is empty, if there are pakuri in it iterate through the list and print out each one
            if pakudex.get_species_array() == None:
                print('No Pakuri in Pakudex yet!')
                print('')
            else:
                mylist = pakudex.get_species_array()
                print('Pakuri In Pakudex:')
                for x in range(len(mylist)):
                    print(f'{x+1}. {mylist[x]}')
        elif option == 2:       #if 2 inputted display species and stats if it exists
            species = input('Enter the name of the species to display: ')
            if species in pakudex.pakudexlist:
                print(f'Species: {species}')
                print(f'Attack: {pakuri.attack}')
                print(f'Defense: {pakuri.defense}')
                print(f'Speed: {pakuri.speed}')
                print('')
            else:
                print('Error: No such Pakuri!')
                print('')
            
        elif option == 3:       #if pakudex full print error, else add it to the list unless it is already in the pakudex
            if len(pakudex.pakudexlist) >= pakudex.capacity:
                print('Error: Pakudex is full!')
                print('')
                continue
            species = input('Enter the name of the species to add: ')
            if species not in pakudex.pakudexlist:
                if pakudex.add_pakuri(species):
                    pakuri = Pakuri(species)
                    print(f'Pakuri species {species} successfully added!')
                    print('')
            else:
                print('Error: Pakudex already contains this species!')
        elif option == 4:       #if pakuri in pakudex evolve species and change stats
            species = input('Enter the name of the species to evolve: ')
            if pakudex.evolve_species(species):
                pakuri.evolve()
                print(f'{species} has evolved!')
            else:
                print('Error: No such Pakuri!')
        elif option == 5: #sort pakudex
            pakudex.sort_pakuri()
            print('Pakuri have been sorted!')
            print('')
        elif option == 6: #exit program
            print('Thanks for using Pakudex! Bye!')
            break
        else: #if int is inputted but not 1-6 raise this error
            print('Unrecognized menu selection!')
if __name__ =='__main__':
    main()
