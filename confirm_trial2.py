# Confirm trial 2 asks the user if they are sure of their input.
# If yes they continue to open the specific bin and if no they are prompted to go back to the main menu.


print("Confirm your selection is 1? (Y/N)")
choice = input()
if choice == 'Y':
    print('Continue')
elif choice == 'N':
    print('Go back to the main menu')
else:
    print("Invalid input. Please enter Y or N")
