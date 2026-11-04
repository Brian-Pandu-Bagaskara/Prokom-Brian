def describe_city(kota, negara='Indonesia'):
    """Mencetak kalimat sederhana tentang letak suatu kota."""
    print(f"{kota.title()} berada di {negara.title()}.")

# Memanggil fungsi untuk tiga kota berbeda (dua menggunakan default, satu diubah)
describe_city('surakarta')
describe_city('bandung')
describe_city('tokyo', negara='jepang')