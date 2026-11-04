# List pesanan dengan kemunculan 'pastrami' minimal 3 kali
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ayam', 'keju', 'pastrami', 'sapi panggang']
finished_sandwiches = []

print("Mohon maaf, kedai kami sedang kehabisan sandwich pastrami.\n")

# Menghapus semua pesanan 'pastrami' dari list sebelum diproses
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Memproses sisa pesanan sandwich
while sandwich_orders:
    sandwich_saat_ini = sandwich_orders.pop()
    print(f"Saya sedang membuat sandwich {sandwich_saat_ini} Anda...")
    finished_sandwiches.append(sandwich_saat_ini)

print("\n--- Daftar Pesanan Selesai ---")
for sandwich in finished_sandwiches:
    print(f"Sandwich {sandwich} telah selesai dibuat.")