# Benar: Tidak ada spasi di sekitar tanda '=' pada parameter (ukuran='L', pesan='I love Python')
def make_shirt(ukuran='L', pesan='I love Python'):
    """Mencetak ringkasan ukuran dan pesan pada kaos."""
    print(f"Membuat kaos ukuran {ukuran} dengan tulisan '{pesan}'.")

# Benar: Tidak ada spasi di sekitar tanda '=' pada argumen kata kunci saat pemanggilan
make_shirt(ukuran='M', pesan='Teknik Industri UNS')