import json
from pathlib import Path

def dapatkan_info_pengguna():
    """Meminta informasi pengguna dan mengembalikannya sebagai dictionary."""
    nama = input("Siapa nama Anda? ")
    jurusan = input("Apa jurusan kuliah Anda? ")
    kampus = input("Di mana Anda berkuliah? ")
    
    # Menyimpan dalam bentuk dictionary
    info_pengguna = {
        'nama': nama,
        'jurusan': jurusan,
        'kampus': kampus,
    }
    return info_pengguna

def ingat_pengguna():
    """Menyimpan atau memuat informasi profil pengguna."""
    jalur_file = Path('info_pengguna.json')
    
    if jalur_file.exists():
        isi = jalur_file.read_text()
        info = json.loads(isi)
        print(f"Selamat datang kembali, {info['nama']}!")
        print("Berikut adalah data yang saya ingat tentang Anda:")
        print(f"- Jurusan: {info['jurusan']}")
        print(f"- Kampus: {info['kampus']}")
    else:
        info = dapatkan_info_pengguna()
        isi = json.dumps(info)
        jalur_file.write_text(isi)
        print(f"Kami akan mengingat profil Anda saat kembali, {info['nama']}!")

# Memanggil fungsi
ingat_pengguna()