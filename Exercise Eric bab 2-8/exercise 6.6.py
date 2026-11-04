# Dictionary yang sudah ada dari contoh di buku
bahasa_favorit = {
    'jenna': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Daftar orang yang seharusnya mengikuti polling
target_peserta = ['jenna', 'budi', 'sarah', 'andi', 'phil', 'eko']

# Loop melalui daftar target peserta
for orang in target_peserta:
    # Mengecek apakah nama orang tersebut ada di dalam kunci dictionary
    if orang in bahasa_favorit.keys():
        print(f"Terima kasih {orang.title()} karena telah mengikuti polling kami!")
    else:
        print(f"Halo {orang.title()}, kami mengundang Anda untuk mengambil polling bahasa favorit.")