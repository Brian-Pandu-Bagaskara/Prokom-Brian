# Berasal dari program 4-1
pizza_favorit = ['pepperoni', 'margherita', 'daging']

# Membuat salinan (copy) list menggunakan slice [:]
friend_pizzas = pizza_favorit[:]

# Menambahkan pizza baru ke list asli
pizza_favorit.append('jamur')

# Menambahkan pizza yang berbeda ke list milik teman
friend_pizzas.append('ayam BBQ')

# Membuktikan bahwa kedua list tersebut terpisah
print("My favorite pizzas are:")
for pizza in pizza_favorit:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")