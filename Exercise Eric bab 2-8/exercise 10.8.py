from pathlib import Path

# Daftar nama file yang ingin dibaca
daftar_file = ['kucing.txt', 'anjing.txt']

for nama_file in daftar_file:
    jalur_file = Path(nama_file)
    
    try:
        # Membaca isi file (encoding utf-8 disarankan untuk teks)
        isi_file = jalur_file.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"\nMaaf, file '{nama_file}' tidak dapat ditemukan di direktori ini.")
    else:
        print(f"\nIsi dari file {nama_file}:")
        print(isi_file)