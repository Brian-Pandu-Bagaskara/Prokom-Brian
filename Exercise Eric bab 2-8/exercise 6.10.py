angka_favorit = {
    'Andi': [7, 11, 21],
    'Siti': [24, 8],
    'Joko': [9],
    'Dewi': [42, 12, 15],
    'Eko': [100, 99]
}

for nama, daftar_angka in angka_favorit.items():
    # Menyesuaikan kalimat jika angkanya hanya satu atau lebih dari satu
    if len(daftar_angka) > 1:
        print(f"\nAngka-angka favorit {nama.title()} adalah:")
    else:
        print(f"\nAngka favorit {nama.title()} adalah:")
        
    for angka in daftar_angka:
        print(f"- {angka}")