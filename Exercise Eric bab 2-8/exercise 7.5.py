prompt = "\nBerapa umur Anda?"
prompt += "\n(Ketik 'quit' jika sudah selesai) "

while True:
    umur = input(prompt)
    
    if umur == 'quit':
        break
        
    umur = int(umur) # Mengubah input string menjadi integer
    
    if umur < 3:
        print("Tiket Anda gratis!")
    elif umur <= 12:
        print("Harga tiket Anda adalah $10.")
    else:
        print("Harga tiket Anda adalah $15.")