# Dictionary kosong untuk menyimpan data hasil polling
hasil_polling = {}

# Variabel bendera (flag) untuk mengontrol perulangan
polling_aktif = True

while polling_aktif:
    # Meminta nama dan respons dari pengguna
    nama = input("\nSiapa nama Anda? ")
    tempat = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")
    
    # Menyimpan respons ke dalam dictionary (nama sebagai kunci, tempat sebagai nilai)
    hasil_polling[nama] = tempat
    
    # Mengecek apakah ada orang lain yang ingin mengikuti polling
    lanjut = input("Apakah ada orang lain yang ingin merespons polling ini? (ya/tidak) ")
    
    # Jika tidak, ubah flag menjadi False agar perulangan berhenti
    if lanjut.lower() == 'tidak':
        polling_aktif = False

# Polling selesai, tampilkan hasilnya
print("\n--- Hasil Polling Liburan Impian ---")
for nama, tempat in hasil_polling.items():
    print(f"{nama.title()} sangat ingin mengunjungi {tempat.title()}.")