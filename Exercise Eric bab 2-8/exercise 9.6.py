# Class induk (dari Latihan 9-1)
class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Nama restoran ini adalah {self.nama_restoran}.")
        print(f"Restoran ini menyajikan masakan jenis {self.jenis_masakan}.")

# Class anak yang mewarisi Restoran
class KedaiEsKrim(Restoran):
    def __init__(self, nama_restoran, jenis_masakan='Es Krim'):
        """Inisialisasi atribut dari class induk, lalu tambah atribut khusus."""
        super().__init__(nama_restoran, jenis_masakan)
        self.rasa = ['vanila', 'cokelat', 'stroberi', 'matcha', 'oreo']

    def tampilkan_rasa(self):
        """Menampilkan daftar rasa es krim yang tersedia."""
        print(f"\n{self.nama_restoran} menyediakan varian rasa berikut:")
        for r in self.rasa:
            print(f"- {r.title()}")


# Membuat instance dari KedaiEsKrim
kedai_ku = KedaiEsKrim('Mixue')
kedai_ku.deskripsikan_restoran()
kedai_ku.tampilkan_rasa()