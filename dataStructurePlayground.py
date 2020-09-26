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