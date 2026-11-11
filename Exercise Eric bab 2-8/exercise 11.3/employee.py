class Employee:
    """Model sederhana untuk merepresentasikan seorang pegawai."""

    def __init__(self, first_name, last_name, annual_salary):
        """Inisialisasi nama depan, nama belakang, dan gaji tahunan."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Menambahkan kenaikan gaji. Default-nya adalah $5.000."""
        self.annual_salary += amount