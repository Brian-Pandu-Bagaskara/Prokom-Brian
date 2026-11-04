def buat_sandwich(*bahan_bahan):
    """Mencetak ringkasan sandwich yang sedang dipesan."""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for bahan in bahan_bahan:
        print(f"- {bahan}")

# Memanggil fungsi tiga kali dengan jumlah argumen yang berbeda
buat_sandwich('telur', 'keju')
buat_sandwich('daging sapi panggang', 'selada', 'tomat', 'mayones')
buat_sandwich('selai kacang', 'stroberi')