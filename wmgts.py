import time
# Functions


def display_disposal_history(disposal_history):
    """
    Given a disposal history as a list of tuples in the format (points, date), 
    display the points earned and the history for the disposal.
    """
    total_points = sum([points for points, _ in disposal_history])
    print(f"Total points earned: {total_points}\n")
    print("Disposal history:")
    for i, (points, date) in enumerate(disposal_history):
        print(f"{i+1}. {date}: {points} points")


# Rating Experience
def rating(number):
    print('After using our application, How would you rate the experience?,Rate from 1 to 10, 10 being you had the best experience\n')
    rate = input('Rating: ')
    message = 'We will keep that number in mind for future development.'
    return message

# The first part welcomes the user.


def menu():
    print('\n\nWelcome to Neg9 Solid Waste Management System.')
    time.sleep(1)
    print('Please Enter your name')
    name = input(':')
    time.sleep(1)
    print('Choose a number corresponding to the type of waste to dispose.')
    print('[1] Organic Waste')
    print('[2] Plastic Bottle')
    print('[3] E-Waste')
    print('[4] Glass Bottle')
    print('[0] Exit')


# Choosing options
menu()
choice = input(':')
if choice == '1':

    print("Confirm your selection is 1? (Yes/No)")
    # Choosing which bin to open
    choice = input(':')
    if choice == 'Yes':
        time.sleep(1)
        print('Remeber that: \n1 -> ORGANIC WASTE\n2 -> PLASTIC WASTE\n3 -> E-WASTE WASTE\n4 -> GLASSWARE WASTE\n')

        bin_color = int(input("\nEnter your choice (1-4): "))
        time.sleep(1)

        if bin_color == 1:
            print(
                "The green bin labeled 'ORGANIC WASTE' opens\n\nProceed to measure weight of the waste.\n")
        elif bin_color == 2:
            print(
                "The blue bin labeled 'PLASTIC WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 3:
            print(
                "The yellow bin labeled 'E-WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 4:
            print(
                "The brown bin labeled 'GLASSWARE WASTE' opens\nProceed to measure weight of the waste.\n")
        else:
            print("Invalid Choice!\nPlease enter values 1-4")

        # Enetering and recording the weight:
        def measureWeight(wasteType):

            quantity_weight = int(input('Enter weight of waste in Kg: '))
            return quantity_weight

        quantity_of_waste = measureWeight(12)
        # print(F'You entered {quantity_of_waste} Kg(s)')

        # Calculating Points earned

        time.sleep(2)

        if quantity_of_waste <= 20:
            print("\nYou have earned 100 points\n")
        elif quantity_of_waste >= 20 and quantity_of_waste <= 40:
            print("\nYou have earned 200 points\n")
        elif quantity_of_waste > 40:
            print("\nYou have earned 400 points\n")

        # Rating Experience

        print('Kindly Rate your experience, On a scale of 1 to 10, 1 being poor and 10 being Very Good.\n')
        rate = input('Rating: ')

        # Good bye
        time.sleep(1)
        print('\nTHANK YOU FOR USING OUR SERVICE.')

    elif choice == 'No':
        print('Go back to main menu')
    else:
        print("Invalid input. Please enter Y or N")

elif choice == '2':
    print("Confirm your selection is 2? (Yes/No):")
    # Choosing which bin to open
    choice = input(':')
    if choice == 'Yes':
        time.sleep(1)
        print('Remeber that: \n1 -> ORGANIC WASTE\n2 -> PLASTIC WASTE\n3 -> E-WASTE WASTE\n4 -> GLASSWARE WASTE\n')

        bin_color = int(input("\nEnter your choice (1-4): "))

        if bin_color == 1:
            print(
                "The green bin labeled 'ORGANIC WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 2:
            print(
                "The blue bin labeled 'PLASTIC WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 3:
            print(
                "The yellow bin labeled 'E-WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 4:
            print(
                "The brown bin labeled 'GLASSWARE WASTE' opens\nProceed to measure weight of the waste.\n")
        else:
            print("Invalid Choice!\nPlease enter values 1-4")

        # Enetering and recording the weight:
        def measureWeight(wasteType):

            quantity_weight = int(input('Enter weight of waste in Kg: '))
            return quantity_weight

        quantity_of_waste = measureWeight(12)
        # print(F'You entered {quantity_of_waste} Kg(s)')

        # Calculating Points earned

        time.sleep(2)

        if quantity_of_waste <= 20:
            print("\nYou have earned 100 points\n")
        elif quantity_of_waste >= 20 and quantity_of_waste <= 40:
            print("\nYou have earned 200 points\n")
        elif quantity_of_waste > 40:
            print("\nYou have earned 400 points\n")

        # Rating Experience

        print('Kindly Rate your experience, On a scale of 1 to 10, 1 being poor and 10 being Very Good.\n')
        rate = input('Rating: ')

        # Good bye
        time.sleep(1)
        print('\nTHANK YOU FOR USING OUR SERVICE.')


elif choice == '3':
    print("Confirm your selection is 3? (Yes/No):")
    # Choosing which bin to open
    choice = input(':')
    if choice == 'Yes':
        time.sleep(1)
        print('Remeber that: \n1 -> ORGANIC WASTE\n2 -> PLASTIC WASTE\n3 -> E-WASTE WASTE\n4 -> GLASSWARE WASTE\n')

        bin_color = int(input("\nEnter your choice (1-4): "))

        if bin_color == 1:
            print(
                "The green bin labeled 'ORGANIC WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 2:
            print(
                "The blue bin labeled 'PLASTIC WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 3:
            print(
                "The yellow bin labeled 'E-WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 4:
            print(
                "The brown bin labeled 'GLASSWARE WASTE' opens\nProceed to measure weight of the waste.\n")
        else:
            print("Invalid Choice!\nPlease enter values 1-4")

        # Enetering and recording the weight:
        def measureWeight(wasteType):

            quantity_weight = int(input('Enter weight of waste in Kg: '))
            return quantity_weight

        quantity_of_waste = measureWeight(12)
        # print(F'You entered {quantity_of_waste} Kg(s)')

        # Calculating Points earned
        time.sleep(2)
        if quantity_of_waste <= 20:
            print("\nYou have earned 100 points\n")
        elif quantity_of_waste >= 20 and quantity_of_waste <= 40:
            print("\nYou have earned 200 points\n")
        elif quantity_of_waste > 40:
            print("\nYou have earned 400 points\n")

        # Rating Experience

        print('Kindly Rate your experience, On a scale of 1 to 10, 1 being poor and 10 being Very Good.\n')
        rate = input('Rating: ')

        # Good bye
        time.sleep(1)
        print('\nTHANK YOU FOR USING OUR SERVICE.')
elif choice == '4':
    print("Confirm your selection is 4? (Yes/No):")
    # Choosing which bin to open
    choice = input(':')
    if choice == 'Yes':
        time.sleep(1)
        print('Remeber that: \n1 -> ORGANIC WASTE\n2 -> PLASTIC WASTE\n3 -> E-WASTE WASTE\n4 -> GLASSWARE WASTE\n')

        bin_color = int(input("\nEnter your choice (1-4): "))

        if bin_color == 1:
            print(
                "The green bin labeled 'ORGANIC WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 2:
            print(
                "The blue bin labeled 'PLASTIC WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 3:
            print(
                "The yellow bin labeled 'E-WASTE' opens\nProceed to measure weight of the waste.\n")
        elif bin_color == 4:
            print(
                "The brown bin labeled 'GLASSWARE WASTE' opens\nProceed to measure weight of the waste.\n")
        else:
            print("Invalid Choice!\nPlease enter values 1-4")

        # Enetering and recording the weight:
        def measureWeight(wasteType):

            quantity_weight = int(input('Enter weight of waste in Kg: '))
            return quantity_weight

        quantity_of_waste = measureWeight(12)
        # print(F'You entered {quantity_of_waste} Kg(s)')

        # Calculating Points earned

        time.sleep(2)

        if quantity_of_waste <= 20:
            print("\nYou have earned 100 points\n")
        elif quantity_of_waste >= 20 and quantity_of_waste <= 40:
            print("\nYou have earned 200 points\n")
        elif quantity_of_waste > 40:
            print("\nYou have earned 400 points\n")

        # Rating Experience

        print('Kindly Rate your experience, On a scale of 1 to 10, 1 being poor and 10 being Very Good.\n')
        rate = int(input('Rating: '))

        # Good bye
        time.sleep(1)
        print('\nTHANK YOU FOR USING OUR SERVICE.')

elif choice == '0':
    exit()
else:
    print("Invalid input. Please enter a valid number")
