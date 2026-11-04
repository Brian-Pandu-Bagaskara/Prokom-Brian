# Contoh modifikasi dari program foods.py pada buku
my_foods = ['pizza', 'falafel', 'kue wortel']
friend_foods = my_foods[:]

# Menambahkan makanan agar listnya berbeda
my_foods.append('cannoli')
friend_foods.append('es krim')

# Menggunakan for loop untuk mencetak list pertama
print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

# Menggunakan for loop untuk mencetak list kedua
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")