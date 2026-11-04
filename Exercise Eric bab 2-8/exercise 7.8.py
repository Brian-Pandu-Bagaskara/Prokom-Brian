# Membuat list pesanan dan list kosong untuk sandwich yang sudah jadi
sandwich_orders = ['tuna', 'ayam', 'keju', 'sapi panggang']
finished_sandwiches = []

# Melakukan perulangan selama list sandwich_orders belum kosong
while sandwich_orders:
    # Mengambil pesanan dari list (menggunakan pop untuk mengeluarkan dari list)
    sandwich_saat_ini = sandwich_orders.pop()
    
    print(f"Saya sedang membuat sandwich {sandwich_saat_ini} Anda...")
    
    # Memasukkan sandwich yang sudah dibuat ke list finished_sandwiches
    finished_sandwiches.append(sandwich_saat_ini)

# Menampilkan semua sandwich yang telah selesai dibuat
print("\n--- Daftar Pesanan Selesai ---")
for sandwich in finished_sandwiches:
    print(f"Sandwich {sandwich} telah selesai dibuat.")