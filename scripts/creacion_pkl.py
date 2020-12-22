import pickle
import pandas as pd

datos_libros = pd.read_csv("./datos/datos-libros.csv")
datos_libros = datos_libros.head(600000)
datos_libros.to_pickle("./datos/datos-libros.pkl")