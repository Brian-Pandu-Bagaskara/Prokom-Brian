from employee import Employee

def test_give_default_raise():
    """Menguji bahwa kenaikan gaji default ($5000) berfungsi dengan benar."""
    # Membuat objek pegawai secara manual (misal: gaji awal 50.000)
    pegawai = Employee('Brian', 'Pandu', 50000)
    pegawai.give_raise()
    
    assert pegawai.annual_salary == 55000

def test_give_custom_raise():
    """Menguji bahwa kenaikan gaji kustom (selain default) berfungsi."""
    # Membuat objek pegawai lagi dari awal
    pegawai = Employee('Brian', 'Pandu', 50000)
    pegawai.give_raise(10000)
    
    assert pegawai.annual_salary == 60000