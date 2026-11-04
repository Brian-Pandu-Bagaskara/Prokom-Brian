"""Fungsi-fungsi yang berkaitan dengan pencetakan model 3D."""

def print_models(unprinted_designs, completed_models):
    """
    Mensimulasikan pencetakan setiap desain, sampai tidak ada yang tersisa.
    Memindahkan setiap desain ke completed_models setelah dicetak.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Menampilkan semua model yang telah selesai dicetak."""
    print("\nModel-model berikut telah selesai dicetak:")
    for completed_model in completed_models:
        print(completed_model)