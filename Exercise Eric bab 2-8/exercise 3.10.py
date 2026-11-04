# Membuat list awal
bahasa = ["Python", "Java", "C++"]
print("List Awal:", bahasa)

# 1. append() - menambah di akhir
bahasa.append("JavaScript")
print("\nSetelah append:", bahasa)

# 2. insert() - menambah di indeks tertentu (misal indeks 1)
bahasa.insert(1, "PHP")
print("Setelah insert:", bahasa)

# 3. del - menghapus berdasarkan indeks (misal indeks 2)
del bahasa[2]
print("Setelah del:", bahasa)

# 4. pop() - mengeluarkan item terakhir
bahasa_terakhir = bahasa.pop()
print("Setelah pop:", bahasa)
print(f"(Bahasa yang dikeluarkan: {bahasa_terakhir})")

# 5. remove() - menghapus berdasarkan nama nilai
bahasa.remove("PHP")
print("Setelah remove:", bahasa)

# 6. sorted() - mengurutkan sementara
print("\nUrutan sementara (sorted):", sorted(bahasa))
print("List asli masih utuh:", bahasa)

# 7. reverse() - membalik urutan permanen
bahasa.reverse()
print("\nSetelah reverse (permanen):", bahasa)

# 8. sort() - mengurutkan abjad permanen
bahasa.sort()
print("Setelah sort (permanen):", bahasa)

# 9. len() - menghitung panjang list
jumlah_bahasa = len(bahasa)
print(f"\nTotal bahasa di list sekarang ada: {jumlah_bahasa}")