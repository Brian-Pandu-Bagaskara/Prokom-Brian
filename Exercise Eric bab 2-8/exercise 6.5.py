sungai_negara = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'kapuas': 'indonesia'
}

# 1. Loop untuk mencetak kalimat tentang setiap sungai
print("--- Fakta Sungai ---")
for sungai, negara in sungai_negara.items():
    print(f"Sungai {sungai.title()} mengalir melewati {negara.title()}.")

# 2. Loop untuk mencetak nama setiap sungai (hanya kunci)
print("\n--- Daftar Sungai ---")
for sungai in sungai_negara.keys():
    print(sungai.title())

# 3. Loop untuk mencetak nama setiap negara (hanya nilai)
print("\n--- Daftar Negara ---")
for negara in sungai_negara.values():
    print(negara.title())