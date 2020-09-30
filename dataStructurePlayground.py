colorSetA = set(["Red", "Blue", "Green", "Black"])
colorSetB = set(["Black","Green", "Yellow", "Orange"])

unifyColorSets = colorSetA.union(colorSetB)

intersectColorSets = colorSetA.intersection(colorSetB)

separateDifferencesColorSets = colorSetA.difference(colorSetB)

print(colorSetA)
print(colorSetB)
print(f"When we unify the sets we get {unifyColorSets}")
print(f"When we determine the commonalities, we get {intersectColorSets}")
print(f"The differences are {separateDifferencesColorSets}")

#This is a method where you can call on variables in one fell swoop instead of having to call them 
#individually like the above lines
print('{0}\n{1}\n{2}'.format( unifyColorSets, intersectColorSets, separateDifferencesColorSets))

print("True or False? colorSetA is a super set of intersectColorSets")
print(colorSetA.issuperset(intersectColorSets))

print("True or False? colorSetA is a sub set of unifyColorSets.")
print(colorSetA.issubset(unifyColorSets))

colorSetA.add("Purple")
print("We used the add() to add Purple to set A.")
print("Is Set A still a sub set of unifyColorSets?")
print(colorSetA.issubset(unifyColorSets))

#PYTHON THE HARDWAY Exercise 38 pgs. 134-

product_specialist_names = "Luke Eddy Sophie Rosy Angelo"

seperated_names = product_specialist_names.split(' ')

other_product_specialists = ["Jim", "Mike", "Sara", "Craig", "Kim"]

while len(seperated_names) != 10:
    next_name = other_product_specialists.pop()
    print(f"Adding: {next_name}")
    seperated_names.append(next_name)
    print(f"There are {len(seperated_names)} product specialists in the array now.")

print(f"There we go: {seperated_names}")

print("Let's rearrange the  names in our list.")

print(f"The specialist in the second index is {seperated_names[1]}")

print(f"The product specialist at the end of the list is {seperated_names[-1]}.")

print(seperated_names.pop())
print("The pop() method 'pops' out the name at the end of the list.")

print(' '.join(seperated_names))
print("That was the join() method.")
print('#'.join(seperated_names[3:5]))



#but first we have to separate the names again

#seperated_names = seperated_names.split(' ')

print(seperated_names)


#Now let's create our first product specialist 'object' with a dictionary and manipulate the data
#let's add some PEP for readibility here
product_specialist = {
    'Name': seperated_names[1], 
    'Age' : 37, 
    'Height' : round(((6-0.4)*12 + 2), 2)
}

#let's create a function for converting feet into cm to improve readibility
#lower case with _ and should have verb for clarity
def convert_feet_to_centimeters(height_in_feet):
    return round((height_in_feet*12 + 2), 2) 


height_of_product_specialist = convert_feet_to_centimeters(5.4)

#Let's change the height of the product specialist in the dictionary
product_specialist["Height"] = height_of_product_specialist

print(product_specialist)


print(product_specialist["Name"])
print(product_specialist["Age"])
print(product_specialist["Height"])

product_specialist[4] = "Favorite Movie"
product_specialist[5] = "Favorite Song"

print(product_specialist[4])

del product_specialist[5]

#EXERCISE 39 PAGE 141

# Create mapping to associate on thing with another

zoned_product_specialists = {
    'Mark' : 'Zone 1',
    'Jimbo' : 'Zone 2',
    'Eddy' : 'Zone 3'
}

# Map zones to the cars in that zone

car_zones = {
    'Zone 1' : 'SUVs',
    'Zone 2' : 'Compacts',
    'Zone 3' : 'AlternativeFuelVehicles'
}

# If it is a really big show, we can add more zones

car_zones['Zone 4'] = "Hero Vehicles"
car_zones['Zone 5'] = "Swag Activation"

#Let's get more specific here
car_zones['Zone 1'] = [
    "Santa Fe",
    "Tucson",
    "Palisade"
]

print("Zone 1 has: ", car_zones['Zone 1'])

# This prints whatever is in the str ten times. Very cool.
print('-' * 10)

# what are in all the zones again
print("Zone 2 has: ", car_zones["Zone 2"])
print("Zone 3 has: ", car_zones['Zone 3'])
print("Zone 4 has: ", car_zones["Zone 4"])



#CHALLENGE: Collect and list of product specialist from the user
#Assign them all equally to a zone between 1-3

#Set up our containers for our list of production specialists
product_specialists_on_duty = []

#Set up our containers for our zone that will house array of product 
    #specialists.
zone_1 = []
zone_2 = []
zone_3 = []

#Greet the user and provide instruction
print("""Hello, Angelo. Please insert the first name of each product specialist on duty this shift.
     Please include a space between each name.""")

#Ask the user for names of product specialist (how will we exit this loop?)
product_specialists_on_duty = input("List product specialists now: ")

#Show user the list input
print(f"To be clear, we have: {product_specialists_on_duty}.")

#Take the str and separate into individuals in an array
product_specialists_on_duty = product_specialists_on_duty.split(" ")
print(product_specialists_on_duty)


while len(product_specialists_on_duty)  != 10:
    #pop() the name of a products specialist and assign it to zone one
    collected_ps_name = product_specialists_on_duty.pop()
    zone_1.append(collected_ps_name)
    print(f"Zone 1 now has: ", zone_1)
#Add an integer to the zone and go to zone 2    
#pop() next PS and add to zone 2
    collected_ps_name = product_specialists_on_duty.pop()
    zone_2.append(collected_ps_name)
    print(f"Zone 2 now has: ", zone_2)
#Move to zone 3
#pop() next PS and add to zone 3
    collected_ps_name = product_specialists_on_duty.pop()
    zone_3.append(collected_ps_name)
    

print("Once again, Zone 1 has: ", zone_1)
print("Zone 2 has: ", zone_2)
print("Zone 3 has: ", zone_3)