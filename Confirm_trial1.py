# the confirm trial 1 prompts the user to confirm the type of waste they want to dispose 
#and if it is valid they continue with the operation so as to open the respective bins

import sys

print("Please confirm the option of waste you want to dispose:1,2,3,4")
choice = input()
if choice == '1':
    print('Continue')
elif choice == '2':
    print('Continue')
elif choice == '3':
    print('Continue')
elif choice == '4':
    print('Continue')
elif choice == '0':
    print('Exit')
else:
    print("Invalid input. Please enter a valid number")
