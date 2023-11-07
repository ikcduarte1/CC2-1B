import time
import random



class Enemy:
    ...


def main():
    prompt()




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




























def print_text_slowly(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return "> "

main()