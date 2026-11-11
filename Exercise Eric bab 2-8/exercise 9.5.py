class Pengguna:
    """Model sederhana untuk profil pengguna."""

    def __init__(self, nama_depan, nama_belakang, umur, pekerjaan, lokasi):
        """Inisialisasi atribut profil pengguna."""
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.pekerjaan = pekerjaan
        self.lokasi = lokasi
        # Menambahkan atribut percobaan login dengan nilai default 0
        self.percobaan_login = 0

    def deskripsikan_pengguna(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"\nRingkasan Profil {self.nama_depan.title()} {self.nama_belakang.title()}:")
        print(f"- Umur      : {self.umur}")
        print(f"- Pekerjaan : {self.pekerjaan}")
        print(f"- Lokasi    : {self.lokasi}")

    def sapa_pengguna(self):
        """Menampilkan pesan sapaan khusus kepada pengguna."""
        print(f"Halo, {self.nama_depan.title()}! Selamat datang kembali.")

    def tambah_percobaan_login(self):
        """Menambah nilai percobaan login sebanyak 1."""
        self.percobaan_login += 1

    def reset_percobaan_login(self):
        """Mereset nilai percobaan login kembali ke 0."""
        self.percobaan_login = 0


# Membuat instance dari class Pengguna
pengguna_1 = Pengguna('Brian', 'Pandu', 20, 'Mahasiswa Teknik Industri', 'Surakarta')

print("--- Simulasi Percobaan Login ---")

# Memanggil metode tambah_percobaan_login() beberapa kali (misal: 4 kali)
pengguna_1.tambah_percobaan_login()
pengguna_1.tambah_percobaan_login()
pengguna_1.tambah_percobaan_login()
pengguna_1.tambah_percobaan_login()

# Mencetak nilai percobaan_login untuk memastikan nilainya bertambah
print(f"Jumlah percobaan login saat ini: {pengguna_1.percobaan_login}")

# Memanggil metode reset_percobaan_login()
pengguna_1.reset_percobaan_login()

# Mencetak kembali untuk memastikan nilainya sudah di-reset menjadi 0
print(f"Jumlah percobaan login setelah di-reset: {pengguna_1.percobaan_login}")