from pengguna import Admin

# Membuat instance Admin menggunakan data Brian
admin_sistem = Admin('Brian', 'Pandu', 20, 'Mahasiswa Teknik Industri', 'Surakarta')
admin_sistem.deskripsikan_pengguna()
admin_sistem.hak_akses.tampilkan_hak_akses()