prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

topping = ""
# Perulangan berjalan selama nilai variabel topping bukan 'quit'
while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"Menambahkan {topping}!")