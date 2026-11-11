print("--- Kalkulator Penjumlahan ---")
print("(Ketik 'q' kapan saja untuk keluar)")

while True:
    angka_1 = input("\nMasukkan angka pertama: ")
    if angka_1 == 'q':
        break
        
    angka_2 = input("Masukkan angka kedua: ")
    if angka_2 == 'q':
        break

    try:
        hasil = int(angka_1) + int(angka_2)
    except ValueError:
        print("Kesalahan: Harap pastikan Anda memasukkan angka yang valid!")
    else:
        print(f"Hasil penjumlahan: {hasil}")