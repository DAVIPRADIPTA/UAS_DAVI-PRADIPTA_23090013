data = []

def getData():       
    nim = str(input("masukan nim : "))
    nama = str(input("masukna nama : "))
    arr = []
    arr.append(nim)
    arr.append(nama)
    data.append(arr)

getData()
while True:
    pilihan = str(input("ingin tambah lagi?(Y/T) :").upper())
    if (pilihan == "Y"):
        getData()
    else :
        for index,value in enumerate(data):
            print(f"{index + 1} : {value}")
        exit()
        