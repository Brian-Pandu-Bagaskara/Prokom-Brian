class User:
    """Model sederhana untuk profil pengguna."""

    def __init__(self, first_name, last_name, age, occupation, location):
        """Inisialisasi atribut profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.location = location

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"\nRingkasan Profil {self.first_name.title()} {self.last_name.title()}:")
        print(f"- Umur      : {self.age}")
        print(f"- Pekerjaan : {self.occupation}")
        print(f"- Lokasi    : {self.location}")

    def greet_user(self):
        """Menampilkan pesan sapaan khusus kepada pengguna."""
        print(f"Halo, {self.first_name.title()}! Selamat datang kembali.")


# Membuat beberapa instance pengguna
user_1 = User('Brian', 'Pandu', 20, 'Mahasiswa Teknik Industri', 'Surakarta')
user_2 = User('Hafidz', 'Ayatulloh', 20, 'Data Analyst', 'Jakarta')
user_3 = User('Dimas', 'Bowo', 21, 'Supply Chain Engineer', 'Semarang')

# Memanggil kedua metode untuk setiap pengguna
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()