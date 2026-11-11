from random import choice

def dapatkan_tiket_pemenang(kumpulan):
    """Fungsi pembantu untuk menghasilkan tiket acak."""
    tiket = []
    while len(tiket) < 4:
        item_acak = choice(kumpulan)
        if item_acak not in tiket:
            tiket.append(item_acak)
    return tiket

kumpulan_undian = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Ini adalah tiket tebakan kita
tiket_ku = [7, 3, 'A', 'E'] 

percobaan = 0
menang = False

print(f"Kombinasi tiket saya: {tiket_ku}")
print("Mulai mengundi... (Tunggu sebentar, ini bisa memakan ribuan percobaan)")

# Loop akan terus berjalan sampai tiket kita cocok dengan tiket pemenang
while not menang:
    tiket_baru = dapatkan_tiket_pemenang(kumpulan_undian)
    percobaan += 1
    
    # Kita menggunakan set() untuk membandingkan karena urutan angka/huruf
    # yang ditarik saat undian tidak penting, asalkan 4 isinya sama.
    if set(tiket_ku) == set(tiket_baru):
        menang = True
        print(f"\nBerhasil! Mesin akhirnya mengeluarkan kombinasi: {tiket_baru}")
        print(f"Dibutuhkan {percobaan} kali percobaan agar tiket Anda menang.")