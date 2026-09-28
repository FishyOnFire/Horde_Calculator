import math
import os
import re

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    get_offencive_cr(200, 14)

    while True:
        print("Hello and welcome to the Horde Calculator \n 1. Start \n 2. About \n 3. Exit")
        command = input()
        match command:
            case "1":
                calculator()
            case "2":
                about()
            case "3":
                break
            case _:
                print("unknown command")

def calculator():
    hp = get_number("hp")
    ac = get_number("ac")
    hit_mod = get_number("to hit bonus")
    amount = get_number("group size")
    
    new_damage, avrage_damage = get_damage(amount)
    

def get_number(text) -> float:
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("Enter the Monsters " + text)
        number = input()
        if number.isdigit():
            return float(number)
        else:
            print("invalid number")

def get_damage(horde_size) -> tuple[str,float]:
    while True:
        print("Enter the monsters damage in format xdx+x")
        damage = input()
        split_input = re.split(r'(\d+)', damage)
    
        if split_input[1].isdigit() and split_input[2] == "d" and split_input[3].isdigit and split_input[4] == "+" and split_input[5].isdigit:
            break
        else:
            print("wrong format used, try again")

    ammount_of_dice = float(split_input[1])
    dice_sice = int(split_input[3])
    damage_bonus = float(split_input[5])
    avrage_roll = (dice_sice/2) + 0.5

    avrage_damage = (avrage_roll*ammount_of_dice+damage_bonus) * horde_size

    new_dice = str(round(ammount_of_dice*(horde_size/2))) + "d" + str(int(dice_sice)) + "+" + str(round(damage_bonus*(horde_size/2)))
    
    return new_dice, avrage_damage

def get_offencive_cr(avrage_damage, hit_bonus) -> float:
    damage_cr_table = [
    [3, 1],    # 0
    [3, 14],   # 1
    [3, 20],   # 2
    [4, 26],   # 3
    [5, 32],   # 4
    [6, 38],   # 5
    [6, 44],   # 6
    [6, 50],   # 7
    [7, 56],   # 8
    [7, 62],   # 9
    [7, 68],   # 10
    [8, 74],   # 11
    [8, 80],   # 12
    [8, 86],   # 13
    [8, 92],   # 14
    [8, 98],   # 15
    [9, 104],  # 16
    [10, 110], # 17
    [10, 116], # 18
    [10, 122], # 19
    [10, 140], # 20
    [11, 158], # 21
    [11, 176], # 22
    [11, 194], # 23
    [12, 212], # 24
    [12, 230], # 25
    [12, 248], # 26
    [13, 266], # 27
    [13, 284], # 28
    [13, 302], # 29
    [14, 320], # 30
]
    damage_cr = 0
    hit_bonus_cr = 0
    cr_difference = 0

    for cr, values  in enumerate(damage_cr_table):
        if avrage_damage <= values[1]:
            damage_cr = cr
            break

    hit_bonus_cr = damage_cr
    
    if damage_cr_table[damage_cr][0] == hit_bonus:
        pass
    elif damage_cr_table[damage_cr][0] > hit_bonus:
        while damage_cr_table[hit_bonus_cr][0] > hit_bonus:
            hit_bonus_cr -= 1
    elif damage_cr_table[damage_cr][0] < hit_bonus:
        while damage_cr_table[hit_bonus_cr][0] < hit_bonus:
            hit_bonus_cr += 1

    cr_difference = hit_bonus_cr - damage_cr

    final_cr = damage_cr + (cr_difference/2)

    return final_cr
        

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
    os.system('cls' if os.name == 'nt' else 'clear')

    
if __name__ == "__main__":
    main()