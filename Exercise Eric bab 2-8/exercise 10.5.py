from pathlib import Path

# String kosong untuk mengumpulkan semua nama tamu
daftar_tamu = ""

print("--- Buku Tamu Digital ---")
print("(Ketik 'keluar' jika sudah selesai memasukkan nama)\n")

# Perulangan untuk terus menanyakan nama
while True:
    nama = input("Silakan masukkan nama Anda: ")
    
    # Kondisi untuk menghentikan perulangan
    if nama.lower() == 'keluar':
        break
    else:
        # Menambahkan nama ke string daftar_tamu, diakhiri dengan baris baru (\n)
        daftar_tamu += f"{nama}\n"
        print(f"Halo, {nama}! Nama Anda telah ditambahkan.\n")

# Menentukan nama file tujuan
jalur_file = Path('guest_book.txt')

# Menulis seluruh string yang terkumpul ke dalam file
jalur_file.write_text(daftar_tamu)

print("\nSemua daftar tamu telah berhasil disimpan ke dalam guest_book.txt!")