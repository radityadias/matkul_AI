def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Mengembalikan indeks jika target ditemukan
    return -1  # Mengembalikan -1 jika target tidak ditemukan

# Contoh penggunaan:
data = [4, 2, 7, 1, 9, 5, 3]
target = int(input("Masukkan Angka : "))
hasil = linear_search(data, target)
if hasil != -1:
    print("Target ditemukan di indeks:", hasil)
else:
    print("Target tidak ditemukan dalam array.")
