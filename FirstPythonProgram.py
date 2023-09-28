#Coded by Duarte, Ivar Klyde C.
#BSCS Section 1-B

pounds = float(input("Weight in pounds(lbs): "))
convert_to_kilos = round(pounds * 0.453592, 2)
print("Weight converted to Kilograms(kg): ", convert_to_kilos)
print("===========================================")
length_in_miles = float(input("Length in Miles: "))
length_in_kilometers = round(length_in_miles * 1.60934, 2)
print("Length in Kilometers: ", length_in_kilometers)
print("===========================================")
total_age = 0
for i in range(1, 10 + 1):
    age = int(input(f"Age of Student {i}: "))
    total_age += age
average_age = total_age / 10
print(total_age)
print("The average age of students is : ", average_age)
print("===========================================")
main_character = "Mr.White"
side_character = "Jesse"
main_antagonist = "Gustavo"
witch = "Sally Goodman"
extra = "Mike"

fantasy_story = f"""
"Someone cooked here" {main_character} said to {side_character}, "SCIENCE!" {side_character} yelled. 
Suddenly they hear a blood-curdling scream. {witch} appears out of nowhere "You shouldn't be here!!!" she exclaimed.
"He's coming for you!". {main_character} and {side_character} look at each other with fear. {main_character}
suddenly started aging so quick that in a matter of seconds he has gray hair. "This is the work of that witch"
{side_character} enraged, he pulls out his Glockernator 3000 and shot that witch. "How dare you do that"
{main_antagonist} uttered. "You will pay for that!". {main_antagonist} sends {extra} to kill them both. 
But {main_character} was already dead from old age. {side_character} cried, he started transforming into a 
killing-machine wearing a pink suit, he calls this form the "PINKMAN". He instantly kills {extra} and had 
his toughest battle yet with {main_antagonist}. But at the end {side_character} won, but not without a
cost, his master and head cook {main_character} was lifeless on the floor.
"""
print(fantasy_story)