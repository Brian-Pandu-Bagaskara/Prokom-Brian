import json
from pathlib import Path

angka_favorit = input("Berapa angka favoritmu? ")

# Tentukan nama file JSON
jalur_file = Path('angka_favorit.json')

# Mengubah data ke format JSON dan menyimpannya ke file
isi = json.dumps(angka_favorit)
jalur_file.write_text(isi)

print("Angka favoritmu telah disimpan!")