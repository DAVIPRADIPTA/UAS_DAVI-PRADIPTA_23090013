import pandas as pd

data = {
    'Nama': ['Mahasiswa1', 'Mahasiswa2', 'Mahasiswa3'],
    'Algoritma dan Struktur data 2': [90, 50, 65],
    'Matematika numerik': [80, 60, 70]
}


dataFrame = pd.DataFrame(data)

print("DataFrame:")
print(dataFrame)


rata_rata_matkul = dataFrame[['Algoritma dan Struktur data 2', 'Matematika numerik']].mean()

print("\nRata-rata nilai masing-masing mata kuliah:")
print(rata_rata_matkul)

dataFrame['Rata-rata Mahasiswa'] = dataFrame[['Algoritma dan Struktur data 2', 'Matematika numerik']].mean(axis=1)

print("\nDataFrame dengan rata-rata nilai masing-masing mahasiswa:")
print(dataFrame)



