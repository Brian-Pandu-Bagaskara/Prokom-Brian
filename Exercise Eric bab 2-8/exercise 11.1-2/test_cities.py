from city_functions import get_city_country

def test_city_country():
    """Apakah nilai seperti 'santiago' dan 'chile' menghasilkan string yang benar?"""
    formatted_city = get_city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'

def test_city_country_population():
    """Apakah nilai dengan parameter populasi berfungsi dengan benar?"""
    formatted_city = get_city_country('santiago', 'chile', population=5000000)
    assert formatted_city == 'Santiago, Chile - population 5000000'