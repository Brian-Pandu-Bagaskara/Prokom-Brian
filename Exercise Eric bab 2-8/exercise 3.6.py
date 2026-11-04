# 1. Kamu harus mendefinisikan list-nya terlebih dahulu di file ini
guest_list = ["Albert Einstein", "Mohammad Hatta", "Soekarno"]

print("Kabar baik! Saya menemukan meja yang lebih besar, jadi ada tambahan tamu.")

# 2. Menambah tamu di awal list (indeks 0)
guest_list.insert(0, "Isaac Newton")

# 3. Menambah tamu di tengah list (indeks 2)
guest_list.insert(2, "Marie Curie")

# 4. Menambah tamu di akhir list
guest_list.append("Nikola Tesla")

# 5. Mencetak undangan baru untuk ke-6 tamu
print(f"Halo {guest_list[0]}, mari makan malam.")
print(f"Halo {guest_list[1]}, mari makan malam.")
print(f"Halo {guest_list[2]}, mari makan malam.")
print(f"Halo {guest_list[3]}, mari makan malam.")
print(f"Halo {guest_list[4]}, mari makan malam.")
print(f"Halo {guest_list[5]}, mari makan malam.")