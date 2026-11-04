# 1. Pengujian kesetaraan (equality) dan ketidaksetaraan (inequality) dengan string
buah = 'mangga'
print("Apakah buah == 'mangga'? (True)")
print(buah == 'mangga')
print("Apakah buah != 'mangga'? (False)")
print(buah != 'mangga')
print("Apakah buah == 'jeruk'? (False)")
print(buah == 'jeruk')

# 2. Pengujian menggunakan metode lower()
mobil = 'Toyota'
print("\nApakah mobil.lower() == 'toyota'? (True)")
print(mobil.lower() == 'toyota')
print("Apakah mobil.lower() == 'honda'? (False)")
print(mobil.lower() == 'honda')

# 3. Pengujian numerik (angka)
umur = 25
print("\n--- Pengujian Numerik ---")
print("Apakah umur == 25? (True):", umur == 25)
print("Apakah umur != 25? (False):", umur != 25)
print("Apakah umur > 20? (True):", umur > 20)
print("Apakah umur < 15? (False):", umur < 15)
print("Apakah umur >= 25? (True):", umur >= 25)
print("Apakah umur <= 20? (False):", umur <= 20)

# 4. Pengujian menggunakan kata kunci 'and' (dan) serta 'or' (atau)
umur_budi = 22
umur_andi = 18
print("\n--- Pengujian 'and' dan 'or' ---")
# 'and' harus keduanya benar agar hasilnya True
print("Apakah umur_budi > 20 and umur_andi >= 18? (True):", umur_budi > 20 and umur_andi >= 18)
print("Apakah umur_budi > 25 and umur_andi >= 18? (False):", umur_budi > 25 and umur_andi >= 18)

# 'or' hanya butuh salah satu yang benar agar hasilnya True
print("Apakah umur_budi > 25 or umur_andi >= 18? (True):", umur_budi > 25 or umur_andi >= 18)
print("Apakah umur_budi < 20 or umur_andi < 15? (False):", umur_budi < 20 or umur_andi < 15)

# 5. Pengujian apakah sebuah item ada di dalam list (in)
menu_tersedia = ['nasi goreng', 'sate', 'soto']
print("\n--- Pengujian 'in' list ---")
print("Apakah 'soto' in menu_tersedia? (True):", 'soto' in menu_tersedia)
print("Apakah 'bakso' in menu_tersedia? (False):", 'bakso' in menu_tersedia)

# 6. Pengujian apakah sebuah item TIDAK ada di dalam list (not in)
pengguna_diblokir = ['andi', 'budi', 'cici']
pengguna_aktif = 'doni'
print("\n--- Pengujian 'not in' list ---")
print("Apakah 'doni' not in pengguna_diblokir? (True):", 'doni' not in pengguna_diblokir)
print("Apakah 'andi' not in pengguna_diblokir? (False):", 'andi' not in pengguna_diblokir)