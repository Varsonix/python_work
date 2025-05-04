person = {
    'first_name': 'jordan',
    'last_name': 'gibbard',
    'age': 35,
    'city': 'escondido'
    }

print(person)

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())
print(person.get('last_name', 'Last Name not found.').title())
