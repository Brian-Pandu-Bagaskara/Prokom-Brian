"""Modul yang hanya berisi class Pengguna."""

class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, pekerjaan, lokasi):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.pekerjaan = pekerjaan
        self.lokasi = lokasi

    def deskripsikan_pengguna(self):
        print(f"\nProfil: {self.nama_depan.title()} {self.nama_belakang.title()}")