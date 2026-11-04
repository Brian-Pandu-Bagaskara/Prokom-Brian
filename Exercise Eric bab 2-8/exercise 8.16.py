def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

    # 1. import module_name
import profil_maker
profil = profil_maker.build_profile('Brian', 'Pandu', jurusan='Teknik Industri')

# 2. from module_name import function_name
from profil_maker import build_profile
profil = build_profile('Brian', 'Pandu', jurusan='Teknik Industri')

# 3. from module_name import function_name as fn (menggunakan alias untuk fungsi)
from profil_maker import build_profile as bp
profil = bp('Brian', 'Pandu', jurusan='Teknik Industri')

# 4. import module_name as mn (menggunakan alias untuk modul)
import profil_maker as pm
profil = pm.build_profile('Brian', 'Pandu', jurusan='Teknik Industri')

# 5. from module_name import * (mengimpor SEMUA fungsi di dalam modul)
# Catatan: Pendekatan ini sebaiknya dihindari untuk proyek besar 
# agar nama fungsi tidak bentrok.
from profil_maker import *
profil = build_profile('Brian', 'Pandu', jurusan='Teknik Industri')