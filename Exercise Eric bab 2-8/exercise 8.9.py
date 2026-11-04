def show_messages(messages):
    """Mencetak setiap pesan teks yang ada di dalam list."""
    for message in messages:
        print(message)

# Membuat list berisi pesan-pesan singkat
pesan_singkat = [
    "Haikal, gambar CAD 2D udah direvisi?",
    "Jangan lupa kumpul laporan SSCM besok tim.",
    "Jadwal UTS Fisika Dasar jam berapa?"
]

# Memanggil fungsi dan meneruskan list ke dalamnya
show_messages(pesan_singkat)