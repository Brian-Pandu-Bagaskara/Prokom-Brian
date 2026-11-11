import json
from pathlib import Path

jalur_file = Path('angka_favorit.json')

# Mengecek apakah file sudah ada
if jalur_file.exists():
    isi = jalur_file.read_text()
    angka_favorit = json.loads(isi)
    print(f"Saya tahu angka favoritmu! Angkanya adalah {angka_favorit}.")
else:
    # Jika file belum ada, minta input dari pengguna
    angka_favorit = input("Berapa angka favoritmu? ")
    isi = json.dumps(angka_favorit)
    jalur_file.write_text(isi)
    print("Angka favoritmu telah disimpan!")