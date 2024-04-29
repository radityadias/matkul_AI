#https://github.com/2black0/GA-Python

import numpy as np
import datetime

# Membuat gen baru
def gen_baru(panjang_target):
    nomor_acak = np.random.randint(32, 126, size=panjang_target)
    gen = ''.join([chr(i) for i in nomor_acak])
    return gen

# Menghitung kecocokan gen dengan target
def cek_kecocokan(gen, target, panjang_target):
    kecocokan = 0
    for i in range(panjang_target):
        if gen[i:i+1] == target[i:i+1]:
            kecocokan += 1
    kecocokan = kecocokan / panjang_target * 100
    return kecocokan

# Membuat populasi awal
def buat_populasi(target, max_populasi, panjang_target):
    populasi = {}
    for i in range(max_populasi):
        gen = gen_baru(panjang_target)
        gen_kecocokan = cek_kecocokan(gen, target, panjang_target)
        populasi[gen] = gen_kecocokan
    return populasi

# Proses seleksi
def seleksi(populasi):
    pop = dict(populasi)
    orang_tua = {}
    for i in range(2):
        gen = max(pop, key=pop.get)
        gen_kecocokan = pop[gen]
        orang_tua[gen] = gen_kecocokan
        if i == 0:
            del pop[gen]
    return orang_tua

# Crossover
def crossover(orang_tua, target, panjang_target):
    anak = {}
    titik_potong = round(len(list(orang_tua)[0])/2)
    for i in range(2):
        gen = list(orang_tua)[i][:titik_potong] + list(orang_tua)[1-i][titik_potong:]
        gen_kecocokan = cek_kecocokan(gen, target, panjang_target)
        anak[gen] = gen_kecocokan
    return anak

# Mutasi
def mutasi(anak, target, tingkat_mutasi, panjang_target):
    mutan = {}
    for i in range(len(anak)):     
        data = list(list(anak)[i])
        for j in range(len(data)):
            if np.random.rand(1) <= tingkat_mutasi:
                ch = chr(np.random.randint(32, 126))
                data[j] = ch
        gen = ''.join(data)
        gen_kecocokan = cek_kecocokan(gen, target, panjang_target)
        mutan[gen] = gen_kecocokan
    return mutan

# Membuat populasi baru dengan gen terbaik yang baru
def regenerasi(mutan, populasi):
    for i in range(len(mutan)):
        gen_buruk = min(populasi, key=populasi.get)
        del populasi[gen_buruk]
    populasi.update(mutan)
    return populasi

# Mendapatkan gen terbaik dalam populasi
def gen_terbaik(orang_tua):
    gen = max(orang_tua, key=orang_tua.get)
    return gen

# Mendapatkan kecocokan terbaik dalam populasi
def kecocokan_terbaik(orang_tua):
    kecocokan = orang_tua[max(orang_tua, key=orang_tua.get)]
    return kecocokan

# Menampilkan hasil
def tampilkan(orang_tua):
    selisih_waktu = datetime.datetime.now()-waktu_mulai
    print('{}\t{}%\t{}'.format(gen_terbaik(orang_tua), round(kecocokan_terbaik(orang_tua), 2), selisih_waktu))

# Program utama
target = input("Masukkan kalimat : ")
max_populasi = 10
tingkat_mutasi = 0.2

print('Kata Target :', target)
print('Max Populasi :', max_populasi)
print('Tingkat Mutasi :', tingkat_mutasi)

panjang_target = len(target)
waktu_mulai=datetime.datetime.now()
print('----------------------------------------------')
print('{}\t{}\t{}'.format('Terbaik','Kecocokan','Waktu'))
print('----------------------------------------------')
populasi = buat_populasi(target, int(max_populasi), panjang_target)
orang_tua = seleksi(populasi)

tampilkan(orang_tua)
while 1:
    anak = crossover(orang_tua, target, panjang_target)
    mutan = mutasi(anak, target, float(tingkat_mutasi), panjang_target)
    if kecocokan_terbaik(orang_tua) >= kecocokan_terbaik(mutan):
        continue
    populasi = regenerasi(mutan, populasi)
    orang_tua = seleksi(populasi)
    tampilkan(orang_tua)
    if kecocokan_terbaik(mutan) >= 100:
        break
