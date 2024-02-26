# Untuk mengakses data pada python, digunakan library pandas

# MEMBACA FILE CSV
# Untuk membaca file data csv pandas menyediakan fungsi read_csv()

# Contoh
# import pandas as pd

# df = pd.read_csv("data.csv", delimiter = ",")



# MEMBACA FILE XLSX atau XLS
# Untuk membaca file spreadsheet atau file excel, pandas menyediakan fungsi
# read.excel()

# Contoh

# import pandas as pd

# df = pd.read_excel("data.xlsx", sheet_name="Sheet1")


# MEMBACA FILE JSON
# Untuk membaca file json, pandas menyediakan fungsi read_json()

# Contoh

# import pandas as pd

# df = pd.read_json()

# MEMBACA FILE HTML
# Untuk membaca file HTML, pandas menyediakan fungsi read_html()

# Contoh

# import pandas as pd

# url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"

# df = pd.read_html(url)[0]

# print(df)

# MEMBACA FORMAT XML
# Untuk membaca format XML, pandas menyediakan fungsi read_xml()

# Contoh

# import pandas as pd

# df = pd.read_xml("https://www.w3schools.com/xml/books.xml")