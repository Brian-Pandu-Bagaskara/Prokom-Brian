from pathlib import Path

# Pastikan file buku_gutenberg.txt ada di folder yang sama
jalur_file = Path('buku_gutenberg.txt')

try:
    isi_teks = jalur_file.read_text(encoding='utf-8')
except FileNotFoundError:
    print("File teks tidak ditemukan. Pastikan Anda sudah membuat 'buku_gutenberg.txt'.")
else:
    # Menghitung kemunculan kata 'the' (ini akan menghitung juga 'then', 'there', 'they')
    jumlah_the = isi_teks.lower().count('the')
    
    # Menghitung kemunculan kata 'the ' (dengan spasi setelahnya, lebih akurat untuk kata tunggal)
    jumlah_the_spasi = isi_teks.lower().count('the ')
    
    print(f"Jumlah kemunculan string 'the'  : {jumlah_the}")
    print(f"Jumlah kemunculan string 'the ' : {jumlah_the_spasi}")