# Membuat tiga dictionary yang mewakili orang yang berbeda
orang_1 = {
    'first_name': 'Budi',
    'last_name': 'Santoso',
    'age': 28,
    'city': 'Surakarta'
}

orang_2 = {
    'first_name': 'Haikal',
    'last_name': 'Pratama',
    'age': 20,
    'city': 'Jakarta'
}

orang_3 = {
    'first_name': 'Kharis',
    'last_name': 'Munandar',
    'age': 21,
    'city': 'Bandung'
}

# Menyimpan semua dictionary ke dalam sebuah list
people = [orang_1, orang_2, orang_3]

# Melakukan perulangan (loop) pada list dan mencetak informasinya
for orang in people:
    nama_lengkap = f"{orang['first_name']} {orang['last_name']}"
    umur = orang['age']
    kota = orang['city']
    
    print(f"Nama: {nama_lengkap}")
    print(f"\tUmur: {umur} tahun")
    print(f"\tAsal Kota: {kota}\n")