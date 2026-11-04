tempat_favorit = {
    'Fikri': ['Bali', 'Lombok', 'Yogyakarta'],
    'Dimas': ['Surakarta'],
    'Kelvin': ['Tokyo', 'Seoul']
}

for nama, daftar_tempat in tempat_favorit.items():
    print(f"\nTempat favorit {nama.title()} adalah:")
    for tempat in daftar_tempat:
        print(f"- {tempat.title()}")