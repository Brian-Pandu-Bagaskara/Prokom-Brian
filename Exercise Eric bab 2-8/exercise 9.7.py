# Class induk (dari Latihan 9-3)
class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, pekerjaan, lokasi):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.pekerjaan = pekerjaan
        self.lokasi = lokasi

    def deskripsikan_pengguna(self):
        print(f"\nProfil: {self.nama_depan.title()} {self.nama_belakang.title()}")

# Class terpisah untuk Hak Akses (Latihan 9-8)
class HakAkses:
    def __init__(self, daftar_hak_akses=None):
        """Inisialisasi atribut hak akses."""
        if daftar_hak_akses is None:
            self.daftar_hak_akses = [
                "bisa menambah postingan", 
                "bisa menghapus postingan", 
                "bisa memblokir pengguna"
            ]
        else:
            self.daftar_hak_akses = daftar_hak_akses

    def tampilkan_hak_akses(self):
        """Menampilkan daftar hak akses administrator."""
        print("Hak akses Admin:")
        for hak in self.daftar_hak_akses:
            print(f"- {hak}")

# Class anak yang mewarisi Pengguna
class Admin(Pengguna):
    def __init__(self, nama_depan, nama_belakang, umur, pekerjaan, lokasi):
        """Inisialisasi atribut class induk, lalu tambahkan atribut HakAkses."""
        super().__init__(nama_depan, nama_belakang, umur, pekerjaan, lokasi)
        # Menggunakan class HakAkses sebagai atribut (Komposisi)
        self.hak_akses = HakAkses()


# Membuat instance dari Admin
admin_1 = Admin('Brian', 'Pandu', 20, 'System Administrator', 'Surakarta')
admin_1.deskripsikan_pengguna()

# Memanggil metode dari atribut hak_akses
admin_1.hak_akses.tampilkan_hak_akses()