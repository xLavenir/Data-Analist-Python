# Hal yang perlu diketahui pada measuring dispersion adalah 
# sebaran nilai dengan menentukan nilai range, interquartile, range, variance dan standart deviation


# RANGE
# -- > Range ditentukan dengan perhitungan selisih nilai max dan min

import numpy as np

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

range = jumlah_kucing.max() - jumlah_kucing.min()

print(f'Nilai Range adalah', range)



# INTERQUARTILE RANGE

# Interquartile Range atau sering disingkat IQR merupakan parameter statistik yang
# menggambarkan selisih antara kuartil ketiga (Q3) dan kuartil pertama (Q1).
# Parameter ini mewakili nilai range atau rentang di mana sebagian besar titik data berada.

iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)

print(f'Nilai Interquartile Range adalah', iqr)

# VARIANCE

# Variance --> merupakan parameter yang digunakan untuk menggambarkan besar simpangan suatu titik data dari nilai mean-nya. 
# Sebelum menghitung nilai variance, kita membutuhkan nilai mean terlebih dahulu

import pandas as pd

jumlah_kucing_series = pd.Series(jumlah_kucing)
kucing_variance = jumlah_kucing_series.var()
print(f'Variance Kucing adalah', kucing_variance)

# STANDARD DEVIATION
# Standard deviation merupakan parameter yang paling sering digunakan para praktisi data untuk menilai sebaran atau simpangan dalam sebuah data. Semakin kecil nilai standard deviation,
# semakin kecil pula jarak antar titik data dengan nilai mean-nya sehingga bisa disimpulkan data tersebut memiliki sebaran yang sempit. Di sisi lain, semakin besar nilai standard deviation,
# semakin luas pula sebaran datanya. Selain itu, standard deviation juga sering digunakan untuk menilai seberapa baik parameter mean dalam merepresentasikan suatu data.

kucing_variance = jumlah_kucing_series.std()
print(f'Variance Kucing adalah', kucing_variance)