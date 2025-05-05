def describe_city(city_name, country='usa'):
    print(f"{city_name.title()} is in {country.upper()}")

describe_city('rome', 'italy')
describe_city(city_name='paris', country='france')
describe_city('Austin')
