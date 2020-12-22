import pandas as pd
# Lectura de los datos
datos_libros = pd.read_pickle("/home/supay/datos/datos_proyecto/DB-libros.pkl")
# datos_libros = datos_libros[['Name', 'Language']]
datos_usuarios = pd.read_pickle('/home/supay/datos/datos_proyecto/ratings_usuarios.pkl')

corrMatrix = pd.read_pickle('/home/supay/datos/datos_proyecto/corrLibros.pkl')

# print(datos_usuarios)
# datos_libros = datos_libros.drop(datos_libros[datos_libros.Language.isin(['jpn','mul', 'grc', 'enm', 'ara', 'zho', 'lat', 'srp','msa', 'glg', 'wel', 'swe', 'nor', 'kor', 'tur','gla', 'lit', 'per', 'pol', 'gle', 'afr', 'ind', 'frs','sco', 'cze', 'rum', 'raj', 'ang', 'eus', 'ypk', 'frm', 'nav','myn', 'gre', 'urd', 'elx', 'guj', 'epo', 'dan', 'nqo', 'cop','tel', 'gem', 'hun', 'haw', 'tib', 'heb', 'sam', 'bul', 'tlh','tah', 'slv', 'hin', 'slo', 'mar', 'mah', 'fro', 'aze', 'kan','non', 'tli', 'san', 'scr', 'fin', 'isl', 'mal', 'bos', 'hmn','tgl', 'cre', 'gmh', 'ave', 'mga', '--', 'lav', 'yid', 'nld','hye'])].index)

# datos_libros = datos_libros.head(50000)

# # datos_libros = datos_libros[datos_libros['Language'].notna()]
# # Limpieza de datos
# datos_libros = datos_libros.replace("#","",regex=True)
# datos_usuarios = datos_usuarios.replace("#","",regex=True)
# datos_usuarios = datos_usuarios.replace('did not like it',1)
# datos_usuarios = datos_usuarios.replace('it was ok',2)
# datos_usuarios = datos_usuarios.replace('liked it',3)
# datos_usuarios = datos_usuarios.replace('really liked it',4)
# datos_usuarios = datos_usuarios.replace('it was amazing',5)
# datos_usuarios = datos_usuarios.replace("This user doesn't have any rating",0)

#print(datos_libros['PagesNumber'].describe())

# print(datos_libros.keys())
# print(len(datos_libros.Authors.unique()))

# Contar los valores de la columna Language hay sin contar los nan
# print(datos_libros.Language.value_counts())

# Contar cuantos registros nan hay
# print(datos_libros.Language.isna().sum())

# print(len(datos_usuarios.ID.unique()))
# ratings = pd.merge(datos_libros, datos_usuarios)

# userRatings = ratings.pivot_table(index=['ID'],columns=['Name'],values='Rating')
#print(userRatings)

"""
CREACION DE PKLS

"""

# datos_usuarios.to_pickle("/home/supay/datos/datos_proyecto/ratings_usuarios.pkl")
# datos_libros.to_pickle("/home/supay/datos/datos_proyecto/DB-libros.pkl")

# corrMatrix = userRatings.corr(method='pearson', min_periods=10)
# corrMatrix.to_pickle("/home/supay/datos/datos_proyecto/corrLibros.pkl")
#print(corrMatrix.head())

