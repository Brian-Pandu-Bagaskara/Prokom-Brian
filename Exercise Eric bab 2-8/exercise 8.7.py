def make_album(artis, judul, jumlah_lagu=None):
    """Membangun dictionary yang mendeskripsikan album musik."""
    album = {
        'nama_artis': artis.title(),
        'judul_album': judul.title()
    }
    
    # Jika argumen jumlah_lagu diberikan, tambahkan ke dalam dictionary
    if jumlah_lagu:
        album['jumlah_lagu'] = jumlah_lagu
        
    return album

# Membuat tiga dictionary yang mewakili album berbeda
album_1 = make_album('dewa 19', 'bintang lima')
album_2 = make_album('sheila on 7', 'kisah klasik untuk masa depan')
album_3 = make_album('tulus', 'manusia', jumlah_lagu=10) # Menggunakan parameter opsional

# Mencetak nilai kembalian untuk memastikan informasinya tersimpan dengan benar
print(album_1)
print(album_2)
print(album_3)