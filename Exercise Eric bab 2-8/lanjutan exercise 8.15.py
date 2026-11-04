# Mengimpor modul yang sudah kita buat sebelumnya
import printing_functions

unprinted_designs = ['casing hp', 'liontin robot', 'dodecahedron']
completed_models = []

# Memanggil fungsi menggunakan sintaks namemodul.namafungsi()
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)