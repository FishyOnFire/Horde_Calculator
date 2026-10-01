import os
import calculator

def horde_calculator():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("Hello and welcome to the Horde Calculator \n 1. Start \n 2. About \n 3. Exit")
        command = input()
        match command:
            case "1":
                calculator.calculator()
            case "2":
                about()
            case "3":
                break
            case _:
                print("unknown command")


def about():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The horde calculator is a tool for DnD 5e that aims to give lower level monster more usability without simply throwing 200 goblins at the problem \n"
    "To achive this it converts low level monsters into Hordes, combineing many monsters into one. This keeps them easy for the GM to use and combat fast pased \n"
    "as too many monsters are more often anoying than thretening. \n"
    "Press Enter to continue")
    next_text = input()
    print("Most of the Hords statistis are the same as the regular monster and will not be touched on here as that would be anoying\n"
    "What is changed is the HP and attacks of the horde as well as the CR.\n" 
    "All hords share some traits:\n" 
    "   *   Attacks that only target a single creature can only deal as much damage as a member of the horde has HP\n"
    "   *   Vurnability towards area attacks\n"
    "   *   Condition Immunites: Charmed, Frightened, Paralysed, Petrified, Prone, Restrained, Stunned\n"
    "   *   The hord has advantage agains creatures that dont have an ally within 5 feet\n"
    "Spellcasters will not be covered in the calculator as they are more complex and are not the most suited for hordes, but one could be added as a support unit\n"
    "The horde calculator will use the official CR calcuations to then give an appropriate CR\n\n"
    "Press Enter to continue")
    next_text = input()

    print("The math itself is quite simpel. For offencive CR it uses ((dmg*1.5)/2) as its damage drops by half when bloodied.\n" \
    "Then for to hit it adds +1.25 as it is expected that it will have advantage (avrage +5) on 1/4 of all attacks it makes\n" \
    "The effective HP will be reduved by half during the CR calculations as the vurnability to AOE effects drasticly deccreses its survivability.\n\n" \
    "Press Enter to continue")
    next_text = input()
    os.system('cls' if os.name == 'nt' else 'clear')
