# Daftar tamu awal dari latihan 3-4
guest_list = ["Albert Einstein", "B.J. Habibie", "Soekarno"]

# Mencetak nama tamu yang batal hadir (misalnya B.J. Habibie di indeks 1)
batal_hadir = guest_list[1]
print(f"Sayang sekali, {batal_hadir} tidak bisa hadir.")

# Mengubah isi list (mengganti tamu di indeks 1 dengan tamu baru)
guest_list[1] = "Mohammad Hatta"

# Mencetak undangan baru
print(f"Halo {guest_list[0]}, saya mengundang Anda makan malam.")
print(f"Halo {guest_list[1]}, saya mengundang Anda makan malam.")
print(f"Halo {guest_list[2]}, saya mengundang Anda makan malam.")