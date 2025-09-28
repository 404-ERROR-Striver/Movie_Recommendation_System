# import pandas as pd

# # your Kaggle dataset
# tmdb = pd.read_csv(r"C:\Users\ASUS\Downloads\tmdb_5000_movies.csv.zip")

# # the mapping file you downloaded
# mapping = pd.read_csv(r"C:\Users\ASUS\Downloads\archive.zip")

# import zipfile

# zip_path = r"C:\Users\ASUS\Downloads\tmdb_5000_movies.csv.zip"

# with zipfile.ZipFile(zip_path, 'r') as z:
#     print(z.namelist())  # lists all files inside the zip



# import pandas as pd

# zip_path = r"C:\Users\ASUS\Downloads\tmdb_5000_movies.csv.zip"
# csv_inside = "tmdb_5000_movies.csv"  # replace with exact name from namelist()

# tmdb = pd.read_csv(f"zip://{zip_path}!{csv_inside}")
# print(tmdb.head())


import pandas as pd

zip_path = r"C:\Users\ASUS\Downloads\tmdb_5000_movies.csv.zip"

import zipfile
with zipfile.ZipFile(zip_path, 'r') as z:
    print(z.namelist())  # check exact CSV name inside

csv_inside = "tmdb_5000_movies.csv"  # replace with exact name from above
tmdb = pd.read_csv(f"zip://{zip_path}!{csv_inside}")
print(tmdb.head())
