import time
import random





class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def attack(self):
        print(f"Your character used {self.name} to attack and dealth {self.damage} damage!")
    class CurrentWeapon:
        def __init__(self, current_weapon):
            self.current_weapon = current_weapon
        def replace(self, new_weapon):
            self.current_weapon = new_weapon
            print(f"Replaced current weapon to {new_weapon.name}")


Broom = Weapons("Broom", random.randint(5,10))
WaterGun = Weapons("Water Gun", random.randint(10,20))
Vaccum = Weapons("Vaccum", random.randint(30,50))
BleachBane = Weapons("Bleach Bane", random.randint(50, 100))

class Enemy:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health
    
    def attack(self):
        print(f"The {self.name} attacks you for {self.damage} damage")

    def attacked(self):
        print(f"The current health of {self.name} is {self.health}")
        if self.health <= 0:
            print(f"The {self.name} has died")
    

Pollutant = Enemy("Pollutant", 5, 20)
Toxigore = Enemy("Toxigore", 10, 15)
Contaminoid = Enemy("Contaminoid", 100, 50)
Pollutiax = Enemy("Pollutiax", 20, 500)


class Treasures:
    ...


class Character:
    
    alive = True
    def __init__(self, health):
        self.health = health
    
    def attacked(self):
        
        print(f"Your current health is {self.health}")
        if self.health <= 0:
            print("You have DIED!")
            alive = False


myCharacter = Character(100)

def main():
    prompt()

    if Character.alive == False:
        try_again = input("Play again?(Y/N)").upper()
        if try_again == 'Y':
            prompt




def prompt():
    print("TALES OF THE PURE: THE SANCTIFIED SKIRMISH")
    input("input any key to continue... \n")
 
    
    introduction = """Welcome to 'Tales of the Pure: The Sanctified Skirmish' a thrilling adventure game that takes you on a journey
to a world overrun by filth and plagued by dirty enemies. In this epic game, you assume the role of a 
determined hero on a mission to restore cleanliness and purity to a once-pristine realm now besieged by darkness.
        
As the protagonist, you must navigate through polluted landscapes, engage in challenging battles with nefarious 
adversaries, and collect treasures, all while armed with an arsenal of unique cleaning tools and gadgets. 
Your quest is to vanquish the vile forces of dirt and grime, and cleanse the world from their corrupting influence."""
    print_text_slowly(introduction)
    character_name = input(print_text_slowly("What is your characters name:"))
    print_text_slowly(f"GREETINGS {character_name}, your quest begins now!")




























def print_text_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return "> "

main()
