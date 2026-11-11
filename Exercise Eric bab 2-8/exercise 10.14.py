import json
from pathlib import Path

def dapatkan_pengguna_tersimpan(jalur_file):
    """Mendapatkan nama pengguna yang tersimpan jika ada."""
    if jalur_file.exists():
        isi = jalur_file.read_text()
        return json.loads(isi)
    return None

def dapatkan_pengguna_baru(jalur_file):
    """Meminta nama pengguna baru dan menyimpannya."""
    nama = input("Siapa nama Anda? ")
    isi = json.dumps(nama)
    jalur_file.write_text(isi)
    return nama

def sapa_pengguna():
    """Menyapa pengguna berdasarkan nama, dan memverifikasi identitasnya."""
    jalur_file = Path('pengguna.json')
    nama_tersimpan = dapatkan_pengguna_tersimpan(jalur_file)
    
    if nama_tersimpan:
        # Memverifikasi identitas pengguna saat ini
        konfirmasi = input(f"Apakah benar Anda adalah {nama_tersimpan}? (y/n) ")
        if konfirmasi.lower() == 'y':
            print(f"Selamat datang kembali, {nama_tersimpan}!")
        else:
            # Jika bukan (jawaban 'n'), minta nama yang baru dan timpa file lama
            nama_baru = dapatkan_pengguna_baru(jalur_file)
            print(f"Kami akan mengingat Anda saat kembali, {nama_baru}!")
    else:
        # Jika file belum ada sama sekali
        nama_baru = dapatkan_pengguna_baru(jalur_file)
        print(f"Kami akan mengingat Anda saat kembali, {nama_baru}!")

# Menjalankan program utama
sapa_pengguna()