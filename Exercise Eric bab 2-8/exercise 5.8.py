nama_pengguna = ['admin', 'haikal', 'kharis', 'fadhil', 'dicky']

for nama in nama_pengguna:
    if nama == 'admin':
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        # Menggunakan .title() agar huruf pertama kapital
        print(f"Halo {nama.title()}, terima kasih sudah login kembali.")