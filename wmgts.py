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
    print('\nChoose a number corresponding to the type of waste to dispose.')
    print('[1] Organic Waste')
    print('[2] Plastic Bottle')
    print('[3] E-Waste')
    print('[4] Glass Bottle')
    print('[0] Exit')
    return name


# Choosing options
menu()
choice = input(':')
if choice == '1':

    print("\nConfirm your selection is 1? (Yes/No)")
    # Choosing which bin to open
    choice = input(':')
    if choice == 'Yes':
        time.sleep(2)

        print("\nThe green bin labeled 'ORGANIC WASTE' opens.\n")

        time.sleep(2)
        print('Proceed to measure weight of the waste.\n')

        # Enetering and recording the weight:

        def measureWeight(wasteType):

            quantity_weight = int(input('Enter weight of waste in Kg: '))
            return quantity_weight

        quantity_of_waste = measureWeight(12)
        # print(F'You entered {quantity_of_waste} Kg(s)')

        # Calculating Points earned

        time.sleep(2)

        if quantity_of_waste <= 20:
            print("\nYou have earned 100 points,\n")
        elif quantity_of_waste >= 20 and quantity_of_waste <= 40:
            print("\nYou have earned 200 points,\n")
        elif quantity_of_waste > 40:
            print("\nYou have earned 400 points,\n")

        # Rating Experience

        print('Kindly Rate your experience, On a scale of 1 to 10, 1 being poor and 10 being Very Good.\n')
        rate = input('Rating: ')

        # Good bye
        time.sleep(1)
        print('\nTHANK YOU FOR USING OUR SERVICE.\n')

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

        print("\nThe blue bin labeled 'PLASTIC WASTE' opens.\n\nProceed to measure weight of the waste.\n")

        # Enetering and recording the weight:

        def measureWeight(wasteType):

            quantity_weight = int(input('Enter weight of waste in Kg: '))
            return quantity_weight

        quantity_of_waste = measureWeight(12)
        # print(F'You entered {quantity_of_waste} Kg(s)')

        # Calculating Points earned

        time.sleep(2)

        if quantity_of_waste <= 20:
            print("\nYou have earned 100 points,\n")
        elif quantity_of_waste >= 20 and quantity_of_waste <= 40:
            print("\nYou have earned 200 points,\n")
        elif quantity_of_waste > 40:
            print("\nYou have earned 400 points,\n")

        # Rating Experience

        print('Kindly Rate your experience, On a scale of 1 to 10, 1 being poor and 10 being Very Good.\n')
        rate = input('Rating: ')

        # Good bye
        time.sleep(1)
        print('\nTHANK YOU FOR USING OUR SERVICE.\n')


elif choice == '3':
    print("Confirm your selection is 3? (Yes/No):")
    # Choosing which bin to open
    choice = input(':')
    if choice == 'Yes':
        time.sleep(1)
        print("\nThe yellow bin labeled 'E-WASTE' opens.\nProceed to measure weight of the waste.\n")

        # Enetering and recording the weight:
        def measureWeight(wasteType):

            quantity_weight = int(input('Enter weight of waste in Kg: '))
            return quantity_weight

        quantity_of_waste = measureWeight(12)
        # print(F'You entered {quantity_of_waste} Kg(s)')

        # Calculating Points earned
        time.sleep(2)
        if quantity_of_waste <= 20:
            print("\nYou have earned 100 points,\n")
        elif quantity_of_waste >= 20 and quantity_of_waste <= 40:
            print("\nYou have earned 200 points,\n")
        elif quantity_of_waste > 40:
            print("\nYou have earned 400 points,\n")

        # Rating Experience

        print('Kindly Rate your experience, On a scale of 1 to 10, 1 being poor and 10 being Very Good.\n')
        rate = input('Rating: ')

        # Good bye
        time.sleep(1)
        print('\nTHANK YOU FOR USING OUR SERVICE.\n')
elif choice == '4':
    print("Confirm your selection is 4? (Yes/No):")
    # Choosing which bin to open
    choice = input(':')
    if choice == 'Yes':
        time.sleep(1)

        print(
            "\nThe brown bin labeled 'GLASSWARE WASTE' opens.\nProceed to measure weight of the waste.\n")

        # Enetering and recording the weight:
        def measureWeight(wasteType):

            quantity_weight = int(input('Enter weight of waste in Kg: '))
            return quantity_weight

        quantity_of_waste = measureWeight(12)
        # print(F'You entered {quantity_of_waste} Kg(s)')

        # Calculating Points earned

        time.sleep(2)

        if quantity_of_waste <= 20:
            print("\nYou have earned 100 points,\n")
        elif quantity_of_waste >= 20 and quantity_of_waste <= 40:
            print("\nYou have earned 200 points,\n")
        elif quantity_of_waste > 40:
            print("\nYou have earned 400 points,\n")

        # Rating Experience

        print('Kindly Rate your experience, On a scale of 1 to 10, 1 being poor and 10 being Very Good.\n')
        rate = int(input('Rating: '))

        # Good bye
        time.sleep(1)
        print('\nTHANK YOU FOR USING OUR SERVICE.\n')


elif choice == '0':
    exit()
else:
    print("Invalid input. Please enter a valid number")
