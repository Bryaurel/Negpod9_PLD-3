#This function measures the weight of the waste according to wastetype
#The weight of the waste is in kgs

def measureWeight(wasteType):
    if wasteType == 1:
        weight = int(input("Please enter the weight of the organic waste (in kg): "))
    elif wasteType == 2:
        weight = int(input("Please enter the weight of the plastic waste (in kg): "))
    elif wasteType == 3:
        weight = int(input("Please enter the weight of the E-waste (in kg): "))
    elif wasteType == 4:
        weight = int(input("Please enter the weight of the glassware waste (in kg): "))
    else:
        weight = 0
    return weight
    
print(measureWeight(1)) # Prompts user to enter weight of the organic waste
print(measureWeight(2)) # Prompts user to enter weight of the plastic waste
print(measureWeight(3)) # Prompts user to enter weight of the E-waste
print(measureWeight(4)) # Prompts user to enter weight of the glassware waste
print(measureWeight(0)) # returns 0