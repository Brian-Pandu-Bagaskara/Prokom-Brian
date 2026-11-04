glosarium = {
    'string': 'Serangkaian karakter atau teks.',
    'list': 'Kumpulan data atau item dalam urutan tertentu.',
    'dictionary': 'Kumpulan data yang terdiri dari pasangan kunci-nilai (key-value).',
    'float': 'Angka yang memiliki titik desimal (bilangan pecahan).',
    'boolean': 'Tipe data yang hanya memiliki dua nilai: True (Benar) atau False (Salah).',
    # 5 istilah baru yang ditambahkan:
    'integer': 'Tipe data untuk bilangan bulat, tanpa desimal.',
    'tuple': 'Kumpulan data berurutan yang nilainya tidak dapat diubah (immutable).',
    'loop': 'Struktur perulangan untuk menjalankan blok kode berkali-kali.',
    'variable': 'Wadah yang digunakan untuk menyimpan suatu nilai data.',
    'if statement': 'Pernyataan bersyarat untuk mengeksekusi kode hanya jika kondisi tertentu bernilai benar.'
}

# Menggunakan loop untuk menelusuri kunci (kata) dan nilai (arti)
for kata, arti in glosarium.items():
    print(f"{kata.title()}:\n\t{arti}\n")