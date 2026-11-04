# Contoh penerapan PEP 8 pada program Pizza (4-11)

# 1. Panjang baris tidak lebih dari 80 karakter (komentar dan kode dibuat ringkas)
pizza_favorit = ['pepperoni', 'margherita', 'daging', 'jamur']
friend_pizzas = pizza_favorit[:]

pizza_favorit.append('sosis')
friend_pizzas.append('ayam BBQ')

# 2. Penggunaan baris kosong (blank lines) secukupnya untuk memisahkan bagian logika
print("Pizza favorit saya adalah:")

# 3. Indentasi menggunakan 4 spasi (bukan tab)
for pizza in pizza_favorit:
    print(f"- {pizza}")

print("\nPizza favorit teman saya adalah:")

for pizza in friend_pizzas:
    print(f"- {pizza}")