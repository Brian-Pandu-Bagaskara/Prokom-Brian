def make_album(artis, judul):
    """Membangun dictionary yang mendeskripsikan album musik."""
    album = {
        'nama_artis': artis.title(),
        'judul_album': judul.title()
    }
    return album

# Perulangan while untuk meminta input dari pengguna
while True:
    print("\nSilakan masukkan data album musik:")
    print("(Ketik 'q' kapan saja untuk keluar)")
    
    input_artis = input("Siapa nama artisnya? ")
    # Mengecek kondisi keluar segera setelah input pertama
    if input_artis.lower() == 'q':
        break
        
    input_judul = input("Apa judul albumnya? ")
    # Mengecek kondisi keluar setelah input kedua
    if input_judul.lower() == 'q':
        break
    
    # Memanggil fungsi menggunakan input dari pengguna
    album_baru = make_album(input_artis, input_judul)
    
    # Mencetak dictionary yang telah dibuat
    print(f"\nAlbum berhasil dibuat: {album_baru}")