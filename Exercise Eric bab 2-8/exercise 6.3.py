glosarium = {
    'string': 'Serangkaian karakter atau teks.',
    'list': 'Kumpulan data atau item dalam urutan tertentu.',
    'dictionary': 'Kumpulan data yang terdiri dari pasangan kunci-nilai (key-value).',
    'float': 'Angka yang memiliki titik desimal (bilangan pecahan).',
    'boolean': 'Tipe data yang hanya memiliki dua nilai: True (Benar) atau False (Salah).'
}

# Menggunakan \n untuk baris kosong dan \t untuk indentasi (menjorok ke dalam)
kata = 'string'
print(f"{kata.title()}:\n\t{glosarium[kata]}\n")

kata = 'list'
print(f"{kata.title()}:\n\t{glosarium[kata]}\n")

kata = 'dictionary'
print(f"{kata.title()}:\n\t{glosarium[kata]}\n")

kata = 'float'
print(f"{kata.title()}:\n\t{glosarium[kata]}\n")

kata = 'boolean'
print(f"{kata.title()}:\n\t{glosarium[kata]}\n")