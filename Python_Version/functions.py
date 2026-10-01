import os
import math
import re

def get_name() ->str:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Enter the original monsters name")
    name = input()
    return name

def get_number(text, name) -> float:
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("Enter the " + name +"s " + text)
        number = input()
        if number.isdigit():
            return float(number)
        else:
            print("invalid number")

def get_damage(horde_size, name) -> tuple[str,float]:
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("Enter the " + name + "s damage in format xdx+x")
        damage = input()
        split_input = re.split(r'(\d+)', damage)
    
        if split_input[1].isdigit() and split_input[2] == "d" and split_input[3].isdigit and split_input[4] == "+" and split_input[5].isdigit:
            break
        else:
            print("wrong format used, try again")
    return calculate_damage(horde_size, split_input)

def calculate_damage(horde_size, split_input) -> tuple[str,float]:

    ammount_of_dice = float(split_input[1])
    dice_sice = int(split_input[3])
    damage_bonus = float(split_input[5])
    avrage_roll = (dice_sice/2) + 0.5

    avrage_damage = (avrage_roll*ammount_of_dice+damage_bonus) * horde_size

    new_dice = str(round(ammount_of_dice*(horde_size/2))) + "d" + str(int(dice_sice)) + "+" + str(round(damage_bonus*(horde_size/2)))
    return new_dice, avrage_damage

def get_offencive_cr(avrage_damage, hit_bonus) -> float:
    cr_table = get_cr_table()
    hit_bonus += 1.25
    avrage_damage = ((avrage_damage*1.5)/2)

    damage_cr = 0
    hit_bonus_cr = 0
    cr_difference = 0
    cr_spot = 0
    
        
    for values in cr_table:
        if avrage_damage <= values[4]:
            damage_cr = values[0]
            break
        cr_spot += 1
    
    
    if cr_table[cr_spot][3] == hit_bonus:
        pass
    elif cr_table[cr_spot][3] > hit_bonus:
        try:
            while cr_table[cr_spot][3] > hit_bonus:
                cr_spot -= 1
        except IndexError:
            cr_spot = 0
    elif cr_table[cr_spot][3] < hit_bonus:
        try:
            while cr_table[cr_spot][3] < hit_bonus:
                cr_spot += 1
        except IndexError:
            cr_spot = 33
    hit_bonus_cr = cr_table[cr_spot][0]

    cr_difference = hit_bonus_cr - damage_cr

    final_offencive_cr = damage_cr + (cr_difference/2)
    
    return math.ceil(final_offencive_cr)



def get_deffencive_cr(ac, hp) -> float:

    hp = hp/2
    cr_table = get_cr_table()
    
    hp_cr = 0
    ac_cr = 0
    cr_difference = 0
    cr_spot = 0

    
    for values in cr_table:
        if hp <= values[2]:
            hp_cr = values[0]
            break
        cr_spot += 1

    
    if cr_table[cr_spot][1] == ac:
        pass
    elif cr_table[cr_spot][1] > ac:
        try:
            while cr_table[cr_spot][1] > ac:
                cr_spot -= 1
        except IndexError:
            cr_spot = 0
    elif cr_table[cr_spot][1] < ac:
        try:
            while cr_table[cr_spot][1] < ac:
                cr_spot += 1
        except IndexError:
            cr_spot = 33
    ac_cr = cr_table[cr_spot][0]
    
    cr_difference = ac_cr - hp_cr


    final_deffencive_cr = hp_cr + (cr_difference/2)
    return final_deffencive_cr


def get_final_cr(offencive_cr, deffencive_cr) -> int:
    final_cr = (offencive_cr + deffencive_cr) /2
    return math.ceil(final_cr)

def get_cr_table():
    cr_table = [
    [0,    13,  6,   3,   1],
    [1/8,  13,  35,  3,   3],
    [1/4,  13,  49,  3,   5],
    [1/2,  13,  70,  3,   8],
    [1,    13,  85,  3,  14],
    [2,    13,  100, 3,   20],
    [3,    13,  115, 4,   26],
    [4,    14,  130, 5,   32],
    [5,    15,  145, 6,   38],
    [6,    15,  160, 6,   44],
    [7,    15,  175, 6,   50],
    [8,    16,  190, 7,   56],
    [9,    16,  205, 7,   62],
    [10,   17,  220, 7,   68],
    [11,   17,  235, 8,   74],
    [12,   17,  250, 8,   80],
    [13,   18,  265, 8,   86],
    [14,   18,  280, 8,   92],
    [15,   18,  295, 8,   98],
    [16,   18,  310, 9,   104],
    [17,   19,  325, 10,  110],
    [18,   19,  340, 10,  116],
    [19,   19,  355, 10,  122],
    [20,   19,  400, 10,  140],
    [21,   19,  445, 11, 158],
    [22,   19,  490, 11, 176],
    [23,   19,  535, 11, 194],
    [24,   19,  580, 12, 212],
    [25,   19,  625, 12, 230],
    [26,   19,  670, 12, 248],
    [27,   19,  715, 13, 266],
    [28,   19,  760, 13, 284],
    [29,   19,  805, 13, 302],
    [30,   19,  850, 14, 320],
    ]
    return cr_table


def show_horde(name, hp, ac, hit_mod, damage, offencive_cr, deffencive_cr, final_cr, amount, avrage_damage):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The " , name , "horde is a horde composed of " , amount , " " , name,"s.\n"
    "Its total HP is " , hp , "with an AC of " , ac , "and its attacks deal " , damage , "with " , hit_mod , "to their attacks resulting in an avrage damage of ",avrage_damage, " .\n"
    "This results in an offencive CR of " , offencive_cr , ", a deffencive CR of " , deffencive_cr , "giving a final CR of " , final_cr)
    print("\n\n Press enter to return")
    waiting = input()
    os.system('cls' if os.name == 'nt' else 'clear')