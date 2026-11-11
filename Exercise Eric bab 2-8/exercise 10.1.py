from pathlib import Path

# Mendefinisikan jalur (path) ke file teks
jalur_file = Path('learning_python.txt')

# Membaca seluruh isi file sebagai satu string besar
isi_file = jalur_file.read_text()

# Cara 1: Mencetak seluruh isi file sekaligus
print("--- Mencetak seluruh file sekaligus ---")
print(isi_file)

# Cara 2: Menyimpan baris ke dalam list dan melakukan perulangan (looping)
print("\n--- Mencetak dengan looping per baris ---")
baris_baris = isi_file.splitlines()
for baris in baris_baris:
    print(baris)