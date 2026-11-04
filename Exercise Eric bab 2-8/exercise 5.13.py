# Program Analisis Sustainable Supply Chain Management (SSCM)
print("=== Evaluasi Pemasok Kedelai (Pendekatan Triple Bottom Line) ===")

# 1. Mengambil data dari pengguna
nama_pemasok = input("Masukkan nama pemasok: ")
biaya_per_ton = float(input("Masukkan biaya bahan baku per ton (dalam juta Rupiah): "))
jejak_karbon = float(input("Masukkan estimasi jejak karbon per ton (kg CO2): "))
skor_sosial = int(input("Masukkan skor kesejahteraan/upah adil petani (1-100): "))

# 2. Menetapkan Standar Kriteria Perusahaan
batas_biaya = 15.0       # Maksimal anggaran biaya per ton
batas_karbon = 200.0     # Maksimal emisi yang ditoleransi
minimal_sosial = 75      # Minimal skor kesejahteraan sosial

print(f"\n--- Hasil Analisis Pemasok: {nama_pemasok} ---")

# 3. Menganalisis pemasok menggunakan rantai if-elif-else
if biaya_per_ton <= batas_biaya and jejak_karbon <= batas_karbon and skor_sosial >= minimal_sosial:
    print("Keputusan: SANGAT DIREKOMENDASIKAN")
    print("Alasan   : Pemasok ini lulus semua kriteria keberlanjutan (Ekonomi, Lingkungan, dan Sosial terpenuhi).")

elif jejak_karbon > batas_karbon and skor_sosial < minimal_sosial:
    print("Keputusan: DITOLAK MUTLAK")
    print("Alasan   : Pemasok melanggar batas emisi lingkungan dan memiliki standar sosial yang buruk bagi petani.")

elif biaya_per_ton > batas_biaya and jejak_karbon <= batas_karbon and skor_sosial >= minimal_sosial:
    print("Keputusan: DIPERTIMBANGKAN BERSYARAT (NEGOSIASI HARGA)")
    print("Alasan   : Pemasok sangat baik dalam praktik ramah lingkungan dan sosial, namun biayanya melebihi anggaran.")

elif biaya_per_ton <= batas_biaya and (jejak_karbon > batas_karbon or skor_sosial < minimal_sosial):
    print("Keputusan: DITOLAK (RISIKO REPUTASI)")
    print("Alasan   : Secara ekonomi memang murah, tetapi akan merugikan keberlanjutan lingkungan atau sosial.")

else:
    print("Keputusan: PERLU AUDIT LANJUTAN")
    print("Alasan   : Data pemasok berada di area abu-abu dan memerlukan peninjauan lapangan.")