class Antrian:
    def __init__(self):
        self.antrian = []

    def Enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f'Pesanan "{pesanan}" telah ditambahkan dalam antrian.')

    def Dequeue(self):
        if self.antrian:
            pesanan_dihapus = self.antrian.pop(0)
            print(f'Pesanan "{pesanan_dihapus}" telah dihapus dari antrian.')
        else:
            print('Antrian kosong, tidak ada pesanan yang dapat dihapus.')

    def tampilkan_antrian(self):
        if self.antrian:
            print('Daftar antrian saat ini:')
            for i, pesanan in enumerate(self.antrian, start=1):
                print(f'{i}. {pesanan}')
        else:
            print('Antrian kosong.')

