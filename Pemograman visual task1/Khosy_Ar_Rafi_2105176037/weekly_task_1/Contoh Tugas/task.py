class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Kelas: {self.kelas}")
        print(f"Prodi: {self.prodi}")
        print(f"Fakultas: {self.fakultas}")
        print(f"Tempat Tinggal: {self.tempat_tinggal}")
        print(f"Asal: {self.asal}")


# Contoh penggunaan
mhs1 = Mahasiswa("Khosy Ar Rafi", "2021 B", "Pendidikan Komputer", "FKIP", "Perjuangan 3", "Samarinda")
mhs1.tampilkan_info()
