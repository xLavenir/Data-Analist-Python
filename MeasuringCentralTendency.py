# Measuring central tendency merupakan sekumpulan parameter statistik untuk
# menggambarkan nilai khas atau sentral yang mewakili keseluruhan observasi atau data.
# Nilai khas atau sentral tersebut direpresentasikan menggunakan tiga
# parameter statistik yaitu mean, median, dan mode [5].
# Mari kita melihat ketiga parameter statistik tersebut secara detail.


import numpy as np
from scipy import stats

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

modeJumlahKucing = stats.mode(jumlah_kucing)[0]

print(f'Mean Jumlah Kucing', np.mean(jumlah_kucing))
print(f'Mode Jumlah Kucing', np.median(jumlah_kucing))
print(f'Mode Jumlah Kucing', modeJumlahKucing)


