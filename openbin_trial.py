# the openbin trial function asks the user to input the number of the type of waste they want to dispose 
#and on entering the bin opens and they are asked to proceed to measure weight

choice = int(input("\nEnter your choice (1-5): "))

if choice == 1:
    print("The green bin labelled 'ORGANIC WASTE' opens\nProceed to measure weight")
elif choice == 2:
    print("The blue bin labelled 'PASTIC WASTE' opens\nProceed to measure weight")
elif choice == 3:
    print("The yellow bin labelled 'E-WASTE' opens\nProceed to measure weight")
elif choice == 4:
    print("The brown bin labelled 'GLASSWARE WASTE' opens\nProceed to measure weight")
elif choice == 5:
    print("Thank you for using our Solid Management System!\nWaste separation for cleaner cities!\nReturn Home")
    breakpoint
else:
    print("Invalid Choice!\nPlease enter values 1-5")
