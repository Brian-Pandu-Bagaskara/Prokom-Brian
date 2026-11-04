pengguna_saat_ini = ['Haikal', 'Kharis', 'fadhil', 'dicky', 'admin']
pengguna_baru = ['dhimas', 'fikri', 'Kharis', 'kelvin', 'DICKY']

# Membuat salinan daftar pengguna_saat_ini dengan huruf kecil semua 
# (case-insensitive) menggunakan list comprehension
pengguna_saat_ini_lower = [pengguna.lower() for pengguna in pengguna_saat_ini]

for pengguna in pengguna_baru:
    # Mengecek dengan mengubah pengguna baru menjadi huruf kecil juga
    if pengguna.lower() in pengguna_saat_ini_lower:
        print(f"Maaf, nama pengguna '{pengguna}' sudah digunakan. Silakan masukkan nama baru.")
    else:
        print(f"Nama pengguna '{pengguna}' tersedia.")