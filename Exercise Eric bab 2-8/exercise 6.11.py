cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '±522.000',
        'fact': 'Dikenal sebagai pusat kebudayaan Jawa dan memiliki dua keraton.'
    },
    'tokyo': {
        'country': 'jepang',
        'population': '±14 juta',
        'fact': 'Merupakan wilayah metropolitan terpadat di dunia.'
    },
    'new york': {
        'country': 'amerika serikat',
        'population': '±8.3 juta',
        'fact': 'Memiliki patung Liberty yang merupakan hadiah dari Prancis.'
    }
}

for kota, info_kota in cities.items():
    negara = info_kota['country'].title()
    populasi = info_kota['population']
    fakta = info_kota['fact']
    
    print(f"\nKota: {kota.title()}")
    print(f"\tNegara: {negara}")
    print(f"\tPopulasi: {populasi}")
    print(f"\tFakta menarik: {fakta}")