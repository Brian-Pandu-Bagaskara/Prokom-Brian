from random import choice

# Kumpulan 10 angka dan 5 huruf
kumpulan_undian = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

tiket_pemenang = []
print("Mengundi tiket pemenang...")

# Mengambil 4 kombinasi unik (tidak boleh ada yang ganda/sama)
while len(tiket_pemenang) < 4:
    item_acak = choice(kumpulan_undian)
    # Cek agar tidak ada angka/huruf duplikat di dalam tiket pemenang
    if item_acak not in tiket_pemenang:
        tiket_pemenang.append(item_acak)

print(f"Selamat! Tiket yang memiliki kombinasi ini memenangkan hadiah:")
print(tiket_pemenang)