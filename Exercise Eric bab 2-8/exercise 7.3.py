angka = input("Masukkan sebuah angka, dan saya akan mengecek apakah itu kelipatan 10: ")
angka = int(angka)

# Mengecek apakah angka tersebut habis dibagi 10
if angka % 10 == 0:
    print(f"Angka {angka} adalah kelipatan dari 10.")
else:
    print(f"Angka {angka} bukan kelipatan dari 10.")