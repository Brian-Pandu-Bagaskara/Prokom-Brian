# Membuat dictionary untuk beberapa hewan peliharaan
hewan_1 = {
    'jenis': 'kucing persia',
    'pemilik': 'Siti'
}

hewan_2 = {
    'jenis': 'anjing golden retriever',
    'pemilik': 'Dicky'
}

hewan_3 = {
    'jenis': 'burung kenari',
    'pemilik': 'Fadhil'
}

# Menyimpannya dalam list
pets = [hewan_1, hewan_2, hewan_3]

# Loop untuk mencetak informasi setiap hewan
for pet in pets:
    jenis_hewan = pet['jenis'].title()
    nama_pemilik = pet['pemilik'].title()
    print(f"{nama_pemilik} memiliki seekor peliharaan berjenis {jenis_hewan}.")