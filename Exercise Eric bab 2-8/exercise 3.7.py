# 1. Masukkan hasil akhir daftar tamu dari latihan 3.6
guest_list = ["Isaac Newton", "Albert Einstein", "Marie Curie", "Mohammad Hatta", "Soekarno", "Nikola Tesla"]

print("Maaf semuanya, mejanya telat datang, saya hanya bisa mengundang dua orang saja.")

# 2. Mengeluarkan 4 tamu dari belakang menggunakan pop()
tamu_batal_1 = guest_list.pop()
print(f"Maaf {tamu_batal_1}, saya harus membatalkan undangannya.")

tamu_batal_2 = guest_list.pop()
print(f"Maaf {tamu_batal_2}, saya harus membatalkan undangannya.")

tamu_batal_3 = guest_list.pop()
print(f"Maaf {tamu_batal_3}, saya harus membatalkan undangannya.")

tamu_batal_4 = guest_list.pop()
print(f"Maaf {tamu_batal_4}, saya harus membatalkan undangannya.")

# 3. Menyisakan 2 orang tamu (Newton dan Einstein) dan memberitahu mereka
print(f"{guest_list[0]}, Anda masih terundang ke makan malam!")
print(f"{guest_list[1]}, Anda masih terundang ke makan malam!")

# 4. Menghapus dua tamu terakhir menggunakan del
del guest_list[0]
del guest_list[0] 

# 5. Membuktikan list sudah kosong
print("\nDaftar tamu saat ini:")
print(guest_list)