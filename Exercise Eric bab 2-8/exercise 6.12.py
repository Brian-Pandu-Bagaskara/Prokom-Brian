# Ekstensi: Mengubah konteks program menjadi data anggota tim proyek akademik
tim_proyek = [
    {
        'nama': 'Haykal', 
        'peran': 'desainer cad 2d', 
        'perangkat_lunak': 'Autodesk Fusion 360'
    },
    {
        'nama': 'Dicky', 
        'peran': 'analis rantai pasok', 
        'perangkat_lunak': 'Excel & Python'
    },
    {
        'nama': 'Fadhil', 
        'peran': 'quality control', 
        'perangkat_lunak': 'Minitab'
    }
]

print("=== DAFTAR ANGGOTA TIM PROYEK TEKNIK INDUSTRI ===\n")

for anggota in tim_proyek:
    nama = anggota['nama']
    peran = anggota['peran'].upper() # Format output dikembangkan dengan huruf kapital
    software = anggota['perangkat_lunak']
    
    print(f"Anggota : {nama}")
    print(f"Peran   : {peran}")
    print(f"Software: Menggunakan {software}")
    print("-" * 40) # Menambahkan garis pembatas agar output lebih rapi