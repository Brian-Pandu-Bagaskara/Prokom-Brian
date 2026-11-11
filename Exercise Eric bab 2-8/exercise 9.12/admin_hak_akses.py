"""Modul yang berisi class HakAkses dan Admin."""

# Mengimpor class Pengguna dari modul pengguna_dasar
from pengguna_dasar import Pengguna

class HakAkses:
    def __init__(self, daftar_hak_akses=None):
        if daftar_hak_akses is None:
            self.daftar_hak_akses = [
                "bisa mengubah database", 
                "bisa mengatur server", 
                "bisa mereset password"
            ]
        else:
            self.daftar_hak_akses = daftar_hak_akses

    def tampilkan_hak_akses(self):
        print("Hak akses Admin Super:")
        for hak in self.daftar_hak_akses:
            print(f"- {hak}")

class Admin(Pengguna):
    def __init__(self, nama_depan, nama_belakang, umur, pekerjaan, lokasi):
        super().__init__(nama_depan, nama_belakang, umur, pekerjaan, lokasi)
        self.hak_akses = HakAkses()