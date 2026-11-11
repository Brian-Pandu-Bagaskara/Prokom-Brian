from pathlib import Path

# Meminta input nama dari pengguna
nama = input("Silakan masukkan nama Anda: ")

# Menentukan nama file tujuan
jalur_file = Path('guest.txt')

# Menulis nama tersebut ke dalam file
jalur_file.write_text(nama)

print(f"Nama '{nama}' telah berhasil disimpan ke dalam guest.txt!")