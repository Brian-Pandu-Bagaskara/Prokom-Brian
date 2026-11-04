jumlah_orang = input("Berapa banyak orang dalam rombongan makan malam Anda? ")

# Mengubah input string menjadi integer (bilangan bulat)
jumlah_orang = int(jumlah_orang)

# Menggunakan pernyataan if-else untuk mengevaluasi jumlah orang
if jumlah_orang > 8:
    print("Maaf, Anda harus menunggu hingga ada meja yang kosong.")
else:
    print("Meja Anda sudah siap.")