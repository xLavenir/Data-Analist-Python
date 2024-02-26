# Measuring asymmetric merupakan konsep statistik yang digunakan untuk mengidentifikasi
# ketidaksimetrisan dalam sebuah distribusi data numerik. Parameter statistik yang umum
# digunakan dalam measuring asymmetric ialah skewness.

# Sebelum mempelajari skewness, perlu diketahui distribusi data
# Distribusi data atau data distribution merupakan sebuah konsep statistik yang digunakan untuk menunjukkan frekuensi suatu nilai muncul dalam sebuah data.
# Umumnya kita menggunakan grafik histogram untuk melihat distribusi suatu data. Grafik tersebut akan menunjukkan frekuensi kemunculan setiap nilai dalam sebuah data.

# Secara umum, berdasarkan bentuk grafik histogram yang terbentuk, kita bisa membagi distribusi data dalam tiga bentuk yaitu symmetric distribution,
# right-skewed distribution, dan left-skewed distribution

# 1. Symmetric distribution --> Distribusi data ini memiliki nilai mean, median, serta mode yang sama dan berada di sentral distribusi data (Ditengah Grafik)

# 2. Right-skewed distribution --> distribusi data yang memiliki sebagian besar populasi data yang terkonsentrasi pada bagian kiri. Distribusi data ini memiliki
# nilai mean lebih besar dari nilai median dan juga mode.

# 3. Left-skewed distribution --> distribusi data yang terjadi ketika sebagian besar populasi data berada pada bagian kanan. Umumnya distribusi ini memiliki
# nilai median dan mode yang lebih besar dari nilai mean.

# CONTOH GRAFIK DISTRIBUSI DATA

import numpy as np
import matplotlib.pyplot as plt
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
plt.hist(jumlah_kucing, bins=4)
plt.show()

# Grafik diatas menunjukkan left - skewed distribution yang kurang sempurna, karena data yang berantakan dan kotor



# SKEWNESS

# Selain melihatnya menggunakan grafik histogram, kita juga bisa mengukur ketidaksimetrisan dalam distribusi data menggunakan parameter skewness.
# Skewness merupakan parameter statistik yang digunakan untuk mengukur kesimetrisan sebuah distribusi data. Ia mampu memberikan kita gambaran
# tentang banyaknya data yang menyimpang dari symmetric distribution

# Nilai skewness positif menggambarkan data yang memiliki distribusi yang cenderung right-skewed.
# Nilai skewness nol menggambarkan data yang memiliki distribusi simetris sempurna.
# Nilai skewness negatif merepresentasikan data dengan distribusi yang cenderung left-skewed.

import pandas as pd

jumlah_kucing_series = pd.Series(jumlah_kucing)
skewness_data_kucing = jumlah_kucing_series.skew()
print('Skewness Data Kucing adalah', skewness_data_kucing)

# Kesimpulan : Nilai Skewness pada data kucing bernilai negatif
# Maka data cenderung Distribusi Left-Skewed