def build_profile(first, last, **user_info):
    """Membangun dictionary berisi segala hal yang diketahui tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Memanggil fungsi dengan nama depan, nama belakang, dan tiga pasangan key-value lainnya
profil_saya = build_profile(
    'Brian Pandu', 'Bagaskara',
    jurusan='Teknik Industri',
    universitas='Universitas Sebelas Maret',
    laptop='Axioo Hype 7 X8-21'
)

print(profil_saya)