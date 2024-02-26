# Data relationship merupakan konsep statistik untuk mengidentifikasi hubungan antar feature bertipe numerik dalam sebuah data.
# Untuk mengidentifikasi hubungan antar feature bertipe numerik, 
# kita bisa menggunakan dua parameter yaitu correlation dan covariance.


# CORRELATION

# Parameter ini digunakan untuk mengidentifikasi korelasi atau hubungan dari dua feature numerik dalam sebuah data.
# Korelasi ini digambarkan menggunakan nilai dengan rentang -1 hingga 1.
# Pada parameter correlation, nilai negatif menggambarkan korelasi berlawanan (negative correlation), sedangkan nilai positif merepresentasikan korelasi bersesuaian (positive correlation).
# Jika correlation dari dua feature bernilai nol, keduanya dinyatakan tidak memiliki korelasi (no correlation).

# CONTOH CODE UNTUK MENGHITUNG CORRELATION

import pandas as pd

sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}

df = pd.DataFrame(sample_data)
df_correlation = df.corr(numeric_only=True)

print(df_correlation)


# COVARIANCE

# covariance untuk mengidentifikasi hubungan antar dua feature dalam sebuah dataset
# Positive covariance yang menggambarkan dua feature yang berkorelasi positif atau bersesuaian.
# Negative covariance yang merepresentasikan dua feature yang berkorelasi negatif atau berlawanan.
# Zero covariance yang menandakan dua feature yang tidak berkorelasi satu sama lain.

# CONTOH CONDE MENGHITUNG COVARIANCE

sample_data_cov = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}

df_cov = pd.DataFrame(sample_data_cov)
df_covariance = df_cov.cov(numeric_only=True)

print(df_covariance)