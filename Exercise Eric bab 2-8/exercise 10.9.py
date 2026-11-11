from pathlib import Path

daftar_file = ['kucing.txt', 'burung.txt', 'anjing.txt'] # Saya sengaja menambahkan 'burung.txt' yang tidak ada

for nama_file in daftar_file:
    jalur_file = Path(nama_file)
    
    try:
        isi_file = jalur_file.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Gagal secara senyap, program akan lanjut ke file berikutnya tanpa pesan error
        pass
    else:
        print(f"\nIsi dari file {nama_file}:")
        print(isi_file)