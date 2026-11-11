def get_city_country(city, country, population=None):
    """Mengembalikan string dengan format 'City, Country' atau beserta populasinya."""
    if population:
        full_string = f"{city.title()}, {country.title()} - population {population}"
    else:
        full_string = f"{city.title()}, {country.title()}"
    return full_string