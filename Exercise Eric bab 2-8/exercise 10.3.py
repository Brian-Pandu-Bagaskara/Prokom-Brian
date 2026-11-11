from pathlib import Path

jalur_file = Path('learning_python.txt')
isi_file = jalur_file.read_text()

print("--- Kode yang lebih ringkas (tanpa variabel sementara) ---")
# Langsung melakukan looping pada isi_file.splitlines()
for baris in isi_file.splitlines():
    baris_modifikasi = baris.replace('Python', 'C++')
    print(baris_modifikasi)