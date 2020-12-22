import os
import glob
import pandas as pd

os.chdir("./datos")

extension = 'csv'
all_filenames_books = [i for i in glob.glob('book*.{}'.format(extension))]
#all_filenames_users = [i for i in glob.glob('user_rating*.{}'.format(extension))]

#Combina todos los archivos de libros
combined_book = pd.concat([pd.read_csv(f) for f in all_filenames_books ])
#Combina todos los archivos de usuarios
#combined_users = pd.concat([pd.read_csv(f) for f in all_filenames_users ])
#export to csv (libros)
combined_book.to_csv( "datos-libros.csv", index=False, encoding='utf-8-sig')
#export to csv (usuarios)
#combined_users.to_csv( "datos-usuarios.csv", index=False, encoding='utf-8-sig')