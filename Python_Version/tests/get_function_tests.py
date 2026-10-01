from Python_Version import functions
# sit in Horde_Calculator folder and run python -m Python_Version.tests.get_function_tests

result = functions.get_deffencive_cr(13,90)
assert result == 1/4
print("got correct deffencive CR")

result = functions.get_final_cr(7,1/4)
assert result == 4
print("got correct final CR")

result = functions.get_offencive_cr(57,5)
assert result == 7
print("got correct offencive CR")
damage_dice, damage = functions.calculate_damage(6,[" ", "1", "d", "12","+","3"," "])

new_damage, avrage_damage = functions.calculate_damage(6,[" ", "1", "d", "12","+","3"," "])

offencive_cr = functions.get_offencive_cr(avrage_damage, 5)
deffencive_cr = functions.get_deffencive_cr(13, 90)
final_cr = functions.get_final_cr(offencive_cr,deffencive_cr)
assert offencive_cr == 7
assert deffencive_cr == 1/4
assert final_cr == 4
print("functionality test succeded")