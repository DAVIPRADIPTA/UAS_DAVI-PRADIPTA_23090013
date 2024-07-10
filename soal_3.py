from modul import Antrian

antrian = Antrian()

while True :
    pilihan = int(input("masukan pilihan (1/2/3): "))
    if pilihan == 1:
        person = str(input("masukan nama :"))
        antrian.Enqueue(person)
    if pilihan == 2:
        antrian.Dequeue()
    if pilihan == 3:
        antrian.tampilkan_antrian()
        