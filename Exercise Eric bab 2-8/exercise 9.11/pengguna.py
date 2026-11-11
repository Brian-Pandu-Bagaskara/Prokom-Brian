"""Modul yang berisi class Pengguna, HakAkses, dan Admin."""

class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, pekerjaan, lokasi):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.pekerjaan = pekerjaan
        self.lokasi = lokasi

    def deskripsikan_pengguna(self):
        print(f"\nProfil: {self.nama_depan.title()} {self.nama_belakang.title()}")

class HakAkses:
    def __init__(self, daftar_hak_akses=None):
        if daftar_hak_akses is None:
            self.daftar_hak_akses = [
                "bisa menambah postingan", 
                "bisa menghapus postingan", 
                "bisa memblokir pengguna"
            ]
        else:
            self.daftar_hak_akses = daftar_hak_akses

    def tampilkan_hak_akses(self):
        print("Hak akses Admin:")
        for hak in self.daftar_hak_akses:
            print(f"- {hak}")

class Admin(Pengguna):
    def __init__(self, nama_depan, nama_belakang, umur, pekerjaan, lokasi):
        super().__init__(nama_depan, nama_belakang, umur, pekerjaan, lokasi)
        self.hak_akses = HakAkses()