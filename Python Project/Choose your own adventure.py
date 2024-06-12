import time
name = input('Type your name: ')
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right.\nWhich way would you like to go?: ").lower()

if answer == 'left':
    answer = input("\nYou come to a river, you can walk around it or swim accross.\nWalk or Swim?: ").lower()
    if answer == "swim":
        print("\nYou swim accross and were eaten by an alligator.\nYou died")
    elif answer == "walk":
        print("\nYou walked for many miles...")
        time.sleep(3)
        print("\nRan out of water and you cannot move anymore.\nYou died")

elif answer == "right":
    answer = input("\nYou come to a bridge, it looks wobbly.\nCross or back?: ").lower()
    if answer == "back":
        print("\nYou go back and lose.\nYou died")
    elif answer == "cross":
        answer = input("\nYou cross the bridge and meet a stranger. Do you talk to them (yes/no)?: ").lower()
        if answer == 'yes':
            print("\nYou talked to the stranger and they gave you gold!/nYou win!!!")
        elif answer == 'no':
            print("\nYou ignored the stranger and they stabbed your back\nYou died")
        else:
            print('\nNot a valid option.\nYour adventure has been ended here:(')

else:
    print('\nNot a valid option.\nYour adventure has been ended here:(')

print("\nThank you for joining the adventure!")

