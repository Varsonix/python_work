# Learning about Tuples (Immutable lists)
dimensions = (200, 50)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

# Redefining the Tuple as an entirely new one
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print('\n')

# Tuple exercise
buffet = ('pizza', 'broccoli', 'burger', 'fries', 'coke')

print("Menu:")
for item in buffet:
    print(item.title())

buffet = ('potato', 'salad', 'burger', 'fries', 'coke')
print("\nUpdated Menu:")
for item in buffet:
    print(item.title())