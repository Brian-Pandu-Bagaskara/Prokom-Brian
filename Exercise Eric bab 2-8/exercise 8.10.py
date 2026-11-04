def send_messages(messages, sent_messages):
    """
    Mencetak setiap pesan dan memindahkannya ke list sent_messages
    setelah dicetak.
    """
    while messages:
        pesan_saat_ini = messages.pop(0) # Mengambil pesan dari urutan pertama
        print(f"Mengirim pesan: {pesan_saat_ini}")
        sent_messages.append(pesan_saat_ini)

# List awal dan list kosong untuk menampung pesan terkirim
pesan_singkat = [
    "Haikal, gambar CAD 2D udah direvisi?",
    "Jangan lupa kumpul laporan SSCM besok tim.",
    "Jadwal UTS Fisika Dasar jam berapa?"
]
pesan_terkirim = []

# Memanggil fungsi
send_messages(pesan_singkat, pesan_terkirim)

# Mencetak kedua list untuk memastikan pesan telah dipindahkan dengan benar
print("\n--- Pengecekan List ---")
print(f"List pesan_singkat (seharusnya kosong): {pesan_singkat}")
print(f"List pesan_terkirim (berisi pesan): {pesan_terkirim}")