class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        info = f'Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}'
        return info

class Mangga(Buah):
    def __init__(self, nama=None, warna=None, rasa=None, vitamin=None):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        parent_info = super().information()
        info = f'{parent_info}, Vitamin: {self.vitamin}'
        return info


buah = Mangga()

buah.setNama("Mangga")
buah.setWarna("hijau")
buah.setRasa("Manis")

buah.setVitamin("Vitamin C")

print(buah.information())
