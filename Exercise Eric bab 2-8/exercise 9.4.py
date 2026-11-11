class Restoran:
    """Model sederhana dari sebuah restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        """Inisialisasi atribut nama, jenis masakan, dan jumlah terlayani."""
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_terlayani = 0  # Nilai default 0

    def deskripsikan_restoran(self):
        """Menampilkan informasi tentang restoran."""
        print(f"Nama restoran ini adalah {self.nama_restoran}.")
        print(f"Restoran ini menyajikan masakan jenis {self.jenis_masakan}.")

    def buka_restoran(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.nama_restoran} sekarang sudah buka!")

    # --- Metode Baru (Latihan 9-4) ---
    def atur_jumlah_terlayani(self, jumlah):
        """Mengatur jumlah pelanggan yang telah dilayani."""
        self.jumlah_terlayani = jumlah

    def tambah_jumlah_terlayani(self, tambahan):
        """Menambah jumlah pelanggan yang telah dilayani."""
        self.jumlah_terlayani += tambahan


# Membuat instance dari class Restoran
restoran_ku = Restoran('Sate Khas Senayan', 'Nusantara')

# 1. Mencetak nilai awal (default)
print(f"Pelanggan awal terlayani: {restoran_ku.jumlah_terlayani}")

# 2. Mengubah nilai secara langsung dan mencetaknya
restoran_ku.jumlah_terlayani = 45
print(f"Pelanggan terlayani (diubah langsung): {restoran_ku.jumlah_terlayani}")

# 3. Menggunakan metode atur_jumlah_terlayani() (set_number_served)
restoran_ku.atur_jumlah_terlayani(125)
print(f"Pelanggan terlayani (setelah diatur via metode): {restoran_ku.jumlah_terlayani}")

# 4. Menggunakan metode tambah_jumlah_terlayani() (increment_number_served)
# Misalnya hari ini ada tambahan 50 pelanggan
restoran_ku.tambah_jumlah_terlayani(50)
print(f"Pelanggan terlayani (setelah ditambah 50): {restoran_ku.jumlah_terlayani}")