from random import randint

class Dadu:
    """Model sederhana dari sebuah dadu."""

    def __init__(self, sisi=6):
        """Inisialisasi dadu, defaultnya 6 sisi."""
        self.sisi = sisi

    def lempar_dadu(self):
        """Mengembalikan angka acak antara 1 dan jumlah sisi dadu."""
        return randint(1, self.sisi)

# 1. Membuat dadu 6 sisi dan melemparnya 10 kali
dadu_6_sisi = Dadu()
print("Hasil lemparan dadu 6 sisi (10 kali):")
for _ in range(10):
    print(dadu_6_sisi.lempar_dadu(), end=" ")
print("\n")

# 2. Membuat dadu 10 sisi dan melemparnya 10 kali
dadu_10_sisi = Dadu(10)
print("Hasil lemparan dadu 10 sisi (10 kali):")
for _ in range(10):
    print(dadu_10_sisi.lempar_dadu(), end=" ")
print("\n")

# 3. Membuat dadu 20 sisi dan melemparnya 10 kali
dadu_20_sisi = Dadu(20)
print("Hasil lemparan dadu 20 sisi (10 kali):")
for _ in range(10):
    print(dadu_20_sisi.lempar_dadu(), end=" ")
print("\n")