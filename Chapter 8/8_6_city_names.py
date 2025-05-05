def city_country(city_name, country):
    full_name = f"{city_name}, {country}"
    return full_name.title()

city = city_country('santiago', 'chile')
print(city)