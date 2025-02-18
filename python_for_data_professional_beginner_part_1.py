# -*- coding: utf-8 -*-
"""Python-for-Data-Professional-Beginner-Part 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G2cND42RypPFaDh7jGIAkEYVuI1rTgUe

**Program pertama: "Hello World"**
"""

print("Hello World!")

"""**Lebih Jauh dengan Print**"""

print("Halo Dunia")
print("Riset Bahasa Python")

"""Struktur Program Python - Part 1
1. Statements: Instruksi yang diberikan secara baris per baris untuk dijalankan oleh mesin
2. Variables: Lokasi penyimpanan yang dapat digunakan untuk menampung sebuah data atau informasi. Contoh: aku mempunyai variabel yang bernama bilangan1, bilangan2, dan kalimat1
3. Literals: Simbol-simbol yang dapat kita gunakan untuk mengisi suatu variabel. Pada kode yang telah dicontohkan di atas, angka 5 dan 10 serta 'Belajar Bahasa Python' disebut sebagai literal.
4. Operators: Simbol-simbol yang dapat digunakan untuk mengubah nilai dari satu variabel dengan melibatkan satu atau lebih variabel dan literal. Contoh: Tanda + merupakan salah satu contoh operator. Dengan menggunakan tanda +, aku berhasil menambahkan isi dari bilangan1 dan bilangan2!

Adapun operator yang lain selain operator + adalah sebagai berikut.
1. Operator - yang berfungsi sebagai operator pengurangan,
2. Operator * yang berfungsi sebagai operator perkalian, dan
3. Operator ** untuk pemangkatan
"""

# Statement
print("Belajar Python menyenangkan")
print("Halo Dunia")
print("Hello World!")
# Variables & Literals
bilangan1 = 5
bilangan2 = 10
kalimat1 = "Belajar Bahasa Python"
# Operators
print(bilangan1 + bilangan2)

"""**Tugas Praktek**
Tantangan belum berakhir. Aku diminta Senja untuk membuat program pengurangan sederhana dengan Python.

Tugas:
Deklarasi variable bilangan1 dengan 20, dan bilangan2 dengan 10 dan tampilkan hasil pengurangan bilangan1 & bilangan 2.
"""

bilangan1 = 20
bilangan2 = 10
print(bilangan1-bilangan2)

"""**Tugas Praktek**

“Saya lihat kamu cepat belajar. Gimana kalau kamu coba buat kalkulator sederhana untuk potongan harga dan pajak, Aksara?” komentar Senja padaku.

Tugas:
Aku diminta menghitung harga_setelah_potongan dan harga_final. harga_final diperoleh dengan mengalikan harga_setelah_potongan dengan angka 1.1 karena PPN sebesar 10% (100% + 10% = 110% atau 1.1)
Aku menggunakan variabel harga_asli dengan nilai 20000 dan variabel potongan dengan nilai 2000.
"""

harga_asli = 20000
potongan = 2000

# Menghitung harga_setelah_potongan
harga_setelah_potongan = harga_asli - potongan

# Menghitung harga_final dengan menambahkan PPN sebesar 10%
harga_final = harga_setelah_potongan * 1.1

print(harga_final)

"""**Sequence Type – Part 1**

Tugas:
Aku diberikan tugas untuk menerapkan variasi tipe data list dengan mengikuti petunjuk yang diberikan Senja. Berikut petunjuknya:

Petunjuk 1: Input data 1, 'dua', 3, 4.0, 5 ke dalam contoh_list
Petunjuk 2: Ambil Elemen pertama dari contoh_list untuk menampilkan output 1 menggunakan print statement
Petunjuk 3: Ambil Elemen ke empat dari contoh_list untuk menampilkan output 4.0 menggunakan print statement
Petunjuk 4: Input data 1, 'dua', 3, 4.0, 5 ke dalam contoh_list
Petunjuk 5: Ubah Elemen keempat dalam contoh_list menjadi 'empat'
Petunjuk 6: Tampilkan output elemen keempat yang telah diubah tersebut menggunakan print statement
"""

# Petunjuk 1: Input data 1, 'dua', 3, 4.0, 5 ke dalam contoh_list
contoh_list = [1, 'dua', 3, 4.0, 5]

# Petunjuk 2: Ambil Elemen pertama dari contoh_list untuk menampilkan output 1 menggunakan print statement
print(contoh_list[0])

# Petunjuk 3: Ambil Elemen ke empat dari contoh_list untuk menampilkan output 4.0 menggunakan print statement
print(contoh_list[3])

# Petunjuk 4: Input data 1, 'dua', 3, 4.0, 5 ke dalam contoh_list
contoh_list = [1, 'dua', 3, 4.0, 5]

# Petunjuk 5: Rubah Elemen keempat dalam contoh_list menjadi 'empat'
contoh_list[3] = 'empat'

# Petunjuk 6: Tampilkan output elemen keempat yang telah dirubah tersebut menggunakan print statement
print(contoh_list[3])

"""Sequence Type – Part 2

Tugas:
Sekarang aku diberikan tugas untuk menerapkan variasi tipe data tuple dengan mengikuti petunjuk yang diberikan Senja:

Petunjuk 1: Input data Januari sampai dengan April ke dalam contoh_tuple
Petunjuk 2: Ambil Elemen pertama dari contoh_tuple untuk menampilkan output 1 menggunakan print statement
Petunjuk 3: Input kembali data Januari sampai dengan April ke dalam contoh_tuple
Petunjuk 4: Ubah Elemen pertama dalam contoh_tuple menjadi 'Desember'

Ketika dijlankan ini akan menghasilkan error yaitu TypeError, silakan kamu submit dengan adanya error dari output pada Petunjuk 4 tersebut.
"""

# Petunjuk 1: Input data Januari sampai dengan April ke dalam contoh_tuple
contoh_tuple = ('Januari', 'Februari', 'Maret', 'April')

# Petunjuk 2: Ambil Elemen pertama dari contoh_tuple untuk menampilkan output 1 menggunakan print statement
print(contoh_tuple[0])

# Petunjuk 3: Input kembali data Januari sampai dengan April ke dalam contoh_tuple
contoh_tuple = ('Januari', 'Februari', 'Maret', 'April')

# Petunjuk 4: Rubah Elemen pertama dalam contoh_tuple menjadi 'Desember'
# Membuat tuple baru dengan elemen pertama diubah
contoh_tuple = ('Desember',) + contoh_tuple[1:]

# Menampilkan hasilnya
print(contoh_tuple)

"""**Set Type**

Tugas:
Sekarang aku diberikan tugas untuk menerapkan variasi set dan frozenset oleh Senja:

Tugas 1:Input data Dewi, Budi, Cici, Linda, Cici kedalam tipe data list dan tampilkan hasilnya
Tugas 2: Input data Dewi, Budi, Cici, Linda, Cici kedalam tipe data set dan tampilkan hasilnya
Tugas 3: Input data Dewi, Budi, Cici, Linda, Cici kedalam tipe data frozenset dan tampilkan hasilnya
"""

contoh_list = ['Dewi, Budi, Cici, Linda, Cici']
print(contoh_list)
contoh_set = ['Dewi, Budi, Cici, Linda, Cici']
print(contoh_set)
contoh_frozen_set = ({'Dewi, Budi, Cici, Linda, Cici'})
print(contoh_frozen_set)

"""**Mapping Type**

Tugas:
Menggunakan tipe data mapping, aku diminta Senja untuk menampilkan nama & pekerjaan John Doe, seorang Programmer.
"""

person = {'nama' : 'John Doe', 'pekerjaan' : 'Programmer'}
print(person['nama'])
print(person['pekerjaan'])

"""**Tugas Praktek**"""

# Mendeklarasikan variabel sepatu, baju, dan celana sebagai dictionary
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000}
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000}
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}

"""**Tugas Praktek**"""

sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000}
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000}
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}
daftar_belanja = [sepatu, baju, celana]

"""**Tugas Praktek**
Dengan data yang aku miliki, aku bisa menghitung total harga jual dengan potongan harga beserta pajak sebesar 10% dari nilai jual.

Untungnya Senja memberikan beberapa tips untuk menyelesaikan tugas ini:

Tips 1. # Data yang dinyatakan ke dalam dictionary
Tips 2. # Hitung harga masing-masing data setelah dikurangi diskon
Tips 3. # Hitung harga total
Tips 4. # Hitung harga kena pajak
Tips 5. # Cetak total_harga + total_pajak

"""

# Data yang dinyatakan ke dalam dictionary
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000}
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000}
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}

# Hitung harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]

# Hitung harga total
total_harga = harga_sepatu + harga_baju + harga_celana

# Hitung harga kena pajak
total_pajak = total_harga * 0.1

# Cetak total_harga + total_pajak
print(total_harga + total_pajak)

"""**Nilai Prioritas Operator dalam Python – Part 1**

Tugas:

Aku diminta Senja untuk menghitung harga yang harus dibayarkan menggunakan barang senilai 150,000, dengan diskon 30% dan pajak 10%, menggunakan cara yang aku gunakan awal dan cara lebih singkat yang diajarkan Senja.
"""

# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = 1 - potongan_harga # baris pertama
harga_bayar += total_harga # baris kedua
pajak_bayar = pajak * harga_bayar # baris ketiga
harga_bayar += pajak_bayar # baris ke-4
print("Kode awal - harga_bayar=", harga_bayar)
# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = (1 - potongan_harga) * total_harga #baris pertama
harga_bayar += harga_bayar * pajak # baris kedua
print("Penyederhanaan kode - harga_bayar=", harga_bayar)

"""**Tugas Praktek**

Tugas:
Dengan cara yang diajarkan Senja, aku akan membuat potongan kode diatas menjadi lebih simpel. Jangan lupa ada pajak 10%.
"""

sepatu = { "nama" : "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = { "nama" : "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = { "nama" : "Celana Lepis", "harga": 200000, "diskon": 60000 }
harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
total_harga = (harga_sepatu + harga_baju + harga_celana) * 1.1
print(total_harga)

"""**Python Conditioning for Decision – Part 2**"""

# Statement if
x = 4
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua") # statemen aksi lebih menjorok ke dalam
# Statement if ... elif ... else
x = 7
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")
elif x % 3 == 0: # jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi tiga")
elif x % 5 == 0: # jika sisa bagi x dengan 5 sama dengan 0
    print("x habis dibagi lima")
else:
    print("x tidak habis dibagi dua, tiga ataupun lima")

"""**Python Conditioning for Decision – Part 3**"""

jam = 13
if jam >= 5 and jam < 12: # selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam >= 12 and jam < 17: # selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam >= 17 and jam < 19: # selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else: # selain kondisi di atas
    print("Selamat malam!")

"""**Tugas Praktek**"""

tagihan_ke = 'Mr. Yoyo'
warehousing = { 'harga_harian': 1000000, 'total_hari':15 }
cleansing = { 'harga_harian': 1500000, 'total_hari':10 }
integration = { 'harga_harian':2000000, 'total_hari':15 }
transform = { 'harga_harian':2500000, 'total_hari':10 }
sub_warehousing = warehousing['harga_harian'] * warehousing['total_hari']
sub_cleansing = cleansing['harga_harian']*cleansing['total_hari']
sub_integration = integration['harga_harian']*integration['total_hari']
sub_transform = transform['harga_harian']*transform['total_hari']
total_harga = sub_warehousing+sub_cleansing+sub_integration+sub_transform
print("Tagihan kepada:")
print(tagihan_ke)
print("Selamat pagi, anda harus membayar tagihan sebesar:")
print(total_harga)

"""Tugas Praktek

Tugas:
Tolong masukkan variabel keterangan waktu tersebut di kodemu. Lalu, diatur dengan detail berikut:

Diatas jam 07 malam adalah salam 'selamat malam'
Diatas jam 05 sore adalah salam 'selamat sore'
Diatas jam 12 siang, adalah 'selamat siang'
dan selain itu 'selamat pagi'
"""

jam = 17
tagihan_ke = 'Mr. Yoyo'
warehousing = { 'harga_harian': 1000000, 'total_hari':15 }
cleansing = { 'harga_harian': 1500000, 'total_hari':10 }
integration = { 'harga_harian':2000000, 'total_hari':15 }
transform = { 'harga_harian':2500000, 'total_hari':10 }

sub_warehousing = warehousing['harga_harian'] * warehousing['total_hari']
sub_cleansing = cleansing['harga_harian'] * cleansing['total_hari']
sub_integration = integration['harga_harian'] * integration['total_hari']
sub_transform = transform['harga_harian'] * transform['total_hari']

total_harga = sub_warehousing + sub_cleansing + sub_integration + sub_transform

print("Tagihan kepada:")
print(tagihan_ke)

if jam > 19:
    print("Selamat malam, anda harus membayar tagihan sebesar:")
elif jam > 17:
    print("Selamat sore, anda harus membayar tagihan sebesar:")
elif jam > 12:
    print("Selamat siang, anda harus membayar tagihan sebesar:")
else:
    print("Selamat pagi, anda harus membayar tagihan sebesar:")

print(total_harga)

"""**Python while loops – Part 1**"""

# Tagihan
tagihan = [50000, 75000, 125000, 300000, 200000]

# Tanpa menggunakan while loop
total_tagihan = tagihan[0] + tagihan[1] + tagihan[2] + tagihan[3] + tagihan[4]
print(total_tagihan)

# Dengan menggunakan while loop
i = 0  # sebuah variabel untuk mengakses setiap elemen tagihan satu per satu
jumlah_tagihan = len(tagihan)  # panjang (jumlah elemen dalam) list tagihan
total_tagihan = 0  # mula-mula, set total_tagihan ke 0

while i < jumlah_tagihan:  # selama nilai i kurang dari jumlah_tagihan
    total_tagihan += tagihan[i]  # tambahkan tagihan[i] ke total_tagihan
    i += 1  # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya.

print(total_tagihan)

"""**Python while loops – Part 2**"""

tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # pengulangan akan dihentikan
    if tagihan[i] <0 :
        total_tagihan = -1
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan[i]
    i += 1
print(total_tagihan)

"""**Python while loops – Part 3**"""

tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # abaikan tagihan ke-i dan lanjutkan ke tagihan berikutnya
    if tagihan[i] < 0:
        i += 1
        continue
    total_tagihan += tagihan[i]
    i += 1
print(total_tagihan)

"""**Python for loops – Part 1**"""

list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan: # untuk setiap tagihan dalam list_tagihan
 total_tagihan += tagihan # tambahkan tagihan ke total_tagihan
print(total_tagihan)

"""**Python for loops – Part 2**"""

list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]

# For loops with break
print("For loops with break")
total_tagihan_break = 0  # Inisialisasi total_tagihan_break
for tagihan in list_tagihan:
    if tagihan < 0:  # Jika ditemukan angka minus
        print("Terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break  # Berhenti perhitungan
    total_tagihan_break += tagihan  # Tambahkan tagihan ke total_tagihan_break
print("Total tagihan %d." % total_tagihan_break)
print()

# For loops with continue
print("For loops with continue")
total_tagihan_continue = 0  # Inisialisasi total_tagihan_continue
for tagihan in list_tagihan:
    if tagihan < 0:  # Jika ditemukan angka minus
        print("Terdapat angka minus dalam tagihan, tagihan %d dilewati!" % tagihan)
        continue  # Lanjutkan ke tagihan berikutnya tanpa menambahkan tagihan yang negatif
    total_tagihan_continue += tagihan  # Tambahkan tagihan ke total_tagihan_continue
print("Total tagihan %d." % total_tagihan_continue)

"""**Python for loops – Part 3**"""

list_daerah = ['Malang', 'Palembang', 'Medan']
list_buah = ['Apel', 'Duku', 'Jeruk']
for nama_daerah in list_daerah:
    for nama_buah in list_buah:
        print(nama_buah+" "+nama_daerah)

"""**Tugas Praktek**

Tugas:
Program yang akan aku bangun akan mengolah sebuah list yang bernama list_cash_flow. Setiap elemen dari list_cash_flow berisikan pengeluaran (bilangan negatif) dan pemasukan (bilangan positif) pada perusahaan

Dari list_cash_flow ini, aku akan menghitung total_pengeluaran dan total_pemasukan perusahaan.
"""

list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran)
print(total_pemasukan)

"""**Mini Project**

Ekspedisi Pamanku
Aku menyambar ponsel di meja dan membuka pesan singkat dari paman tempo hari yang menjelaskan jika paman harus mengeluarkan uang sebesar 1,5 juta per mobil dalam sehari. Tapi, beliau selalu kebingungan dengan total pengeluaran per bulan karena adanya aturan ganjil-genap yang membuat pengoperasian mobil yang berbeda.

“Kalau begitu, aku akan masukkan variabel jumlah_hari berisi jumlah hari dalam sebulan dan variabel list_plat_nomor berisi seluruh nomor plat mobil milik paman,” gumamku sendiri. Kalau seperti ini paman hanya perlu mengganti variabel jumlah_hari atau modifikasi variabel list_plat_nomor untuk melacak total pengeluaran paman selama sebulan. Ide Cemerlang!


"""

# Data
uang_jalan = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]

# Pengecekan kendaraan dengan nomor pelat ganjil atau genap
kendaraan_genap = 0  # Mendefinisikan variabel kendaraan_genap
kendaraan_ganjil = 0  # Mendefinisikan variabel kendaraan_ganjil

for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:
        kendaraan_genap += 1
    else:
        kendaraan_ganjil += 1

# Total pengeluaran untuk kendaraan dengan nomor pelat ganjil dan genap dalam 1 bulan
i = 1
total_pengeluaran = 0
while i <= jumlah_hari:
    if i % 2 == 0:
        total_pengeluaran += (kendaraan_genap * uang_jalan)
    else:
        total_pengeluaran += (kendaraan_ganjil * uang_jalan)
    i += 1

# Cetak total pengeluaran
print(total_pengeluaran)