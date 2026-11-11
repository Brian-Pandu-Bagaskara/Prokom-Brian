import json
from pathlib import Path

jalur_file = Path('angka_favorit.json')

# Membaca isi file JSON
isi = jalur_file.read_text()

# Mengubah kembali JSON menjadi format asli Python
angka_favorit = json.loads(isi)

print(f"Saya tahu angka favoritmu! Angkanya adalah {angka_favorit}.")