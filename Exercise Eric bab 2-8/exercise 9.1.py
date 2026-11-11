class Restoran:
    """Model sederhana dari sebuah restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        """Inisialisasi atribut nama dan jenis masakan."""
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        """Menampilkan informasi tentang restoran."""
        print(f"Nama restoran ini adalah {self.nama_restoran}.")
        print(f"Restoran ini menyajikan masakan jenis {self.jenis_masakan}.")

    def buka_restoran(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.nama_restoran} sekarang sudah buka!")


# --- Latihan 9-1 ---
print("--- Latihan 9-1 ---")
restoran_ku = Restoran('Sate Khas Senayan', 'Nusantara')

# Mencetak dua atribut secara individual
print(f"Nama restoran: {restoran_ku.nama_restoran}")
print(f"Jenis masakan: {restoran_ku.jenis_masakan}\n")

# Memanggil kedua metode
restoran_ku.deskripsikan_restoran()
restoran_ku.buka_restoran()


# --- Latihan 9-2 ---
print("\n--- Latihan 9-2 ---")
# Membuat tiga instance restoran yang berbeda
restoran_1 = Restoran('Pizza Hut', 'Italia')
restoran_2 = Restoran('Sushi Tei', 'Jepang')
restoran_3 = Restoran('Warteg Kharisma Bahari', 'Rumahan')

# Memanggil metode deskripsi untuk setiap instance
restoran_1.deskripsikan_restoran()
print()
restoran_2.deskripsikan_restoran()
print()
restoran_3.deskripsikan_restoran()