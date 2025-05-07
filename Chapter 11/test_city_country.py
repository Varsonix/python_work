from city_functions import get_city_country


def test_city_country_function():
    """Does a simple 'Santiago, Chile' work?"""
    organized_name = get_city_country('santiago', 'chile')
    assert organized_name == 'Santiago, Chile'