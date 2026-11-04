def make_shirt(ukuran='L', pesan='I love Python'):
    """Mencetak kaos dengan nilai bawaan untuk ukuran dan pesan."""
    print(f"Membuat kaos berukuran {ukuran} dengan cetakan pesan: '{pesan}'.")

# 1. Membuat kaos ukuran besar (L) dengan pesan bawaan
make_shirt()

# 2. Membuat kaos ukuran sedang (M) dengan pesan bawaan
make_shirt(ukuran='M')

# 3. Membuat kaos ukuran apa saja dengan pesan yang berbeda
make_shirt(ukuran='S', pesan='Keep Calm and Code On')