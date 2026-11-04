def make_shirt(ukuran, pesan):
    """Mencetak ringkasan tentang ukuran dan pesan pada kaos."""
    print(f"Membuat kaos berukuran {ukuran} dengan cetakan pesan: '{pesan}'.")

# 1. Memanggil fungsi menggunakan argumen posisional (berdasarkan urutan)
make_shirt('M', 'Teknik Industri')

# 2. Memanggil fungsi menggunakan argumen kata kunci (keyword arguments)
make_shirt(pesan='Python Programmer', ukuran='XL')