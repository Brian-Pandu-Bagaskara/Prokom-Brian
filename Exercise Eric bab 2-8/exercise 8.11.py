def send_messages(messages, sent_messages):
    """
    Mencetak setiap pesan dan memindahkannya ke list sent_messages
    setelah dicetak.
    """
    while messages:
        pesan_saat_ini = messages.pop(0)
        print(f"Mengirim pesan: {pesan_saat_ini}")
        sent_messages.append(pesan_saat_ini)

pesan_singkat = [
    "Haikal, gambar CAD 2D udah direvisi?",
    "Jangan lupa kumpul laporan SSCM besok tim.",
    "Jadwal UTS Fisika Dasar jam berapa?"
]
pesan_terkirim = []

# Memanggil fungsi DENGAN SALINAN list (menggunakan [:])
send_messages(pesan_singkat[:], pesan_terkirim)

# Mencetak kedua list untuk menunjukkan bahwa list asli tetap utuh
print("\n--- Pengecekan List ---")
print(f"List pesan_singkat (asli tetap utuh):")
print(pesan_singkat)
print(f"\nList pesan_terkirim:")
print(pesan_terkirim)