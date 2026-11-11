print("--- Program Penjumlahan Dasar ---")
angka_1 = input("Masukkan angka pertama: ")
angka_2 = input("Masukkan angka kedua: ")

try:
    hasil = int(angka_1) + int(angka_2)
except ValueError:
    print("Maaf, Anda harus memasukkan angka, bukan teks!")
else:
    print(f"Hasil penjumlahan: {hasil}")