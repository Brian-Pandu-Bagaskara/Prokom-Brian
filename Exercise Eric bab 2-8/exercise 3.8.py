# 1. Membuat list 5 tempat (tidak sesuai abjad)
lokasi = ["Makkah", "Tokyo", "Swiss", "Kairo", "Bali"]

# 2. Cetak list asli
print("List Asli:")
print(lokasi)

# 3. Cetak sesuai abjad (sementara) menggunakan sorted()
print("\nSesuai Abjad (Sementara):")
print(sorted(lokasi))

# 4. Buktikan list asli belum berubah
print("\nList Asli (Belum Berubah):")
print(lokasi)

# 5. Cetak kebalikan abjad (sementara) menggunakan sorted() dengan reverse=True
print("\nKebalikan Abjad (Sementara):")
print(sorted(lokasi, reverse=True))

# 6. Buktikan list asli masih belum berubah
print("\nList Asli (Masih Belum Berubah):")
print(lokasi)

# 7. Balik urutan secara permanen menggunakan reverse()
print("\nDibalik Permanen (Bukan Berdasarkan Abjad):")
lokasi.reverse()
print(lokasi)

# 8. Balik lagi urutannya agar kembali ke awal
print("\nDibalik Lagi (Kembali ke Urutan Awal):")
lokasi.reverse()
print(lokasi)

# 9. Urutkan sesuai abjad secara permanen menggunakan sort()
print("\nSesuai Abjad (Permanen):")
lokasi.sort()
print(lokasi)

# 10. Urutkan kebalikan abjad secara permanen menggunakan sort() dengan reverse=True
print("\nKebalikan Abjad (Permanen):")
lokasi.sort(reverse=True)
print(lokasi)