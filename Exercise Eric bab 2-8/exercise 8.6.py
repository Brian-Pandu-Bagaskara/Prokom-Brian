def city_country(kota, negara):
    """Mengembalikan string dengan format 'Kota, Negara'."""
    hasil = f"{kota.title()}, {negara.title()}"
    return hasil

# Memanggil fungsi dengan tiga pasangan kota-negara dan mencetak hasilnya
print(city_country('santiago', 'chile'))
print(city_country('surakarta', 'indonesia'))
print(city_country('tokyo', 'jepang'))