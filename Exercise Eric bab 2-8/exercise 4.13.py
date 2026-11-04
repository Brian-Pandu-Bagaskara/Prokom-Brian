# Mendefinisikan tuple dengan 5 menu makanan dasar
menu_prasmanan = ('nasi goreng', 'ayam bakar', 'sate ayam', 'gado-gado', 'kerupuk')

print("Menu asli restoran:")
for makanan in menu_prasmanan:
    print(f"- {makanan}")

# PERCOBAAN MODIFIKASI (Jika baris di bawah ini dijalankan (tanpa tanda #), Python akan menghasilkan pesan error TypeError)
# menu_prasmanan[0] = 'nasi kuning'

# Restoran mengubah menu (mengganti 2 makanan)
# Karena tuple tidak bisa diubah isinya secara individual, kita harus menulis ulang seluruh tuple-nya
menu_prasmanan = ('nasi kuning', 'ikan bakar', 'sate ayam', 'gado-gado', 'kerupuk')

print("\nMenu restoran yang baru:")
for makanan in menu_prasmanan:
    print(f"- {makanan}")