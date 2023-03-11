

def menu():
    print('[1] Organic Waste')
    print('[2] Plastic Waste')
    print('[3] E-Waste')
    print('[4] Glassware waste')
    print('[0] Exit')
    print("------------------")


menu()
option = input("Please make a choice >>")
if option == "1":
    print("Enter the weight of your organic waste")
elif option == "2":
    print("Enter the number of the bottles")
elif option == "3":
    print("Enter the weight of the E-Waste")
elif option == "4":
    print("Enter the weight of the Glassware waste")
else:
    print("Invalid option, try again:")
