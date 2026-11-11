# Mengimpor class Admin dari modul admin_hak_akses
from admin_hak_akses import Admin

# Membuat instance dan mengecek apakah semuanya berjalan lancar
admin_baru = Admin('Brian', 'Pandu', 20, 'Super Admin', 'Surakarta')
admin_baru.deskripsikan_pengguna()
admin_baru.hak_akses.tampilkan_hak_akses()