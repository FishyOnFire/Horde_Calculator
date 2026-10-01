import functions

def calculator():
    name = functions.get_name()
    hp = functions.get_number("hp", name)
    ac = functions.get_number("ac", name)
    hit_mod = functions.get_number("to hit bonus", name)
    amount = functions.get_number("group size", name)

    hp = hp * amount

    new_damage, avrage_damage = functions.get_damage(amount, name)

    offencive_cr = functions.get_offencive_cr(avrage_damage, hit_mod)
    deffencive_cr = functions.get_deffencive_cr(ac, hp)
    final_cr = functions.get_final_cr(offencive_cr,deffencive_cr)

    functions.show_horde(name, hp, ac, hit_mod, new_damage, offencive_cr, deffencive_cr, final_cr, amount, avrage_damage) 




    