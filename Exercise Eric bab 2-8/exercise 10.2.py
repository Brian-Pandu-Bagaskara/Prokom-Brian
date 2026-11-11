from pathlib import Path

jalur_file = Path('learning_python.txt')
isi_file = jalur_file.read_text()

baris_baris = isi_file.splitlines()

print("--- Mengganti kata Python dengan C ---")
for baris in baris_baris:
    # Mengganti kata 'Python' menjadi 'C'
    baris_modifikasi = baris.replace('Python', 'C')
    print(baris_modifikasi)