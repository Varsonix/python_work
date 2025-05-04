cities = {
    'San Diego': {
        'country': 'USA',
        'population': 352903,
        'fact': 'Its sunny',
    },
    'Paris': {
        'country': 'France',
        'population': 33902,
        'fact': 'it is a place'
    },
    'Rome': {
        'country': 'Italy',
        'population': 23,
        'fact': 'it was built in a day'
    },
}

for city, city_info in cities.items():
    print(f"\n{city.title()} Info:")
    print(f"Country: {city_info['country'].title()}")
    print(f"Population: {city_info['population']}")
    print(f"Fun Fact: {city_info['fact'].title()}")
