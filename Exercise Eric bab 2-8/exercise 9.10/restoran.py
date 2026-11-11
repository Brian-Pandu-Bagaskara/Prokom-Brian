"""Modul yang berisi class Restoran."""

class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Nama restoran ini adalah {self.nama_restoran}.")
        print(f"Restoran ini menyajikan masakan jenis {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sekarang sudah buka!")