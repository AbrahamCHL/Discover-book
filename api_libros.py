from flask import Flask, jsonify, request as req, render_template
import pandas as pd
from sqlalchemy import *
# import json


engine = create_engine('mysql+pymysql://root:password@localhost/db_books', echo=False)

metadata = MetaData(bind=None)
app = Flask(__name__,static_folder='../static',template_folder="../templates")

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/entrenamiento_base_de_datos/', methods = ['GET'])
def create_table():
    
    datos_libros = pd.read_pickle("/home/supay/datos/datos_proyecto/DB-libros.pkl")
    datos_libros = datos_libros[['Name', 'Language']]
    datos_usuarios = pd.read_pickle('/home/supay/datos/datos_proyecto/datos-usuarios.pkl')
    datos_libros = datos_libros.drop(datos_libros[datos_libros.Language.isin(['jpn','mul', 'grc', 'enm', 'ara', 'zho', 'lat', 'srp','msa', 'glg', 'wel', 'swe', 'nor', 'kor', 'tur','gla', 'lit', 'per', 'pol', 'gle', 'afr', 'ind', 'frs','sco', 'cze', 'rum', 'raj', 'ang', 'eus', 'ypk', 'frm', 'nav','myn', 'gre', 'urd', 'elx', 'guj', 'epo', 'dan', 'nqo', 'cop','tel', 'gem', 'hun', 'haw', 'tib', 'heb', 'sam', 'bul', 'tlh','tah', 'slv', 'hin', 'slo', 'mar', 'mah', 'fro', 'aze', 'kan','non', 'tli', 'san', 'scr', 'fin', 'isl', 'mal', 'bos', 'hmn','tgl', 'cre', 'gmh', 'ave', 'mga', '--', 'lav', 'yid', 'nld','hye'])].index)

    datos_libros = datos_libros.head(50000)

    # datos_libros = datos_libros[datos_libros['Language'].notna()]
    # Limpieza de datos
    datos_usuarios = datos_usuarios.replace('did not like it',1)
    datos_usuarios = datos_usuarios.replace('it was ok',2)
    datos_usuarios = datos_usuarios.replace('liked it',3)
    datos_usuarios = datos_usuarios.replace('really liked it',4)
    datos_usuarios = datos_usuarios.replace('it was amazing',5)
    datos_usuarios = datos_usuarios.replace("This user doesn't have any rating",0)

    #print(datos_libros['PagesNumber'].describe())

    # print(datos_libros.keys())
    # print(len(datos_libros.Authors.unique()))

    # Contar los valores de la columna Language hay sin contar los nan
    # print(datos_libros.Language.value_counts())

    # Contar cuantos registros nan hay
    # print(datos_libros.Language.isna().sum())

    # print(len(datos_usuarios.ID.unique()))
    ratings = pd.merge(datos_libros, datos_usuarios)

    userRatings = ratings.pivot_table(index=['ID'],columns=['Name'],values='Rating')
    #print(userRatings)

    corrMatrix = userRatings.corr(method='pearson', min_periods=10)
    corrMatrix.to_pickle("/home/supay/datos/datos_proyecto/corrLibros.pkl")
    #print(corrMatrix.head())
    
    
    return 'Success data base!'

@app.route('/entrenamiento_pkl/', methods = ['GET'])
def entrenamiento_pkl():
    
    datos_libros = pd.read_pickle("/home/supay/datos/datos_proyecto/DB-libros.pkl")
    # datos_libros = datos_libros[['Name', 'Language']]
    datos_usuarios = pd.read_pickle('/home/supay/datos/datos_proyecto/ratings_usuarios.pkl')
    # datos_libros = datos_libros.drop(datos_libros[datos_libros.Language.isin(['jpn','mul', 'grc', 'enm', 'ara', 'zho', 'lat', 'srp','msa', 'glg', 'wel', 'swe', 'nor', 'kor', 'tur','gla', 'lit', 'per', 'pol', 'gle', 'afr', 'ind', 'frs','sco', 'cze', 'rum', 'raj', 'ang', 'eus', 'ypk', 'frm', 'nav','myn', 'gre', 'urd', 'elx', 'guj', 'epo', 'dan', 'nqo', 'cop','tel', 'gem', 'hun', 'haw', 'tib', 'heb', 'sam', 'bul', 'tlh','tah', 'slv', 'hin', 'slo', 'mar', 'mah', 'fro', 'aze', 'kan','non', 'tli', 'san', 'scr', 'fin', 'isl', 'mal', 'bos', 'hmn','tgl', 'cre', 'gmh', 'ave', 'mga', '--', 'lav', 'yid', 'nld','hye'])].index)

    # datos_libros = datos_libros.head(50000)

    # datos_libros = datos_libros[datos_libros['Language'].notna()]
    # Limpieza de datos
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
    ratings = pd.merge(datos_libros, datos_usuarios)

    userRatings = ratings.pivot_table(index=['ID'],columns=['Name'],values='Rating')
    #print(userRatings)

    corrMatrix = userRatings.corr(method='pearson', min_periods=10)
    corrMatrix.to_pickle("/home/supay/datos/datos_proyecto/corrLibros.pkl")
    #print(corrMatrix.head())
    
    return 'Success pkl!'


@app.route('/libros/recomendar_base_de_datos/', methods=['GET'])

def recomendar_libros_data_base():
    anime = req.args.get('anime')
    rating = req.args.get('rating')
    rating = int(rating)

    corrMatrix = pd.read_sql_table('anime', 'mysql+pymysql://root:password@localhost/anime', index_col=['name'])  
    
    simCandidates = pd.Series()
    # #print(simCandidates)
    # # Recuperar las pelis similares a las calificadas
    sims = corrMatrix[anime].dropna()
    # print(sims[0])
    # # Escalar la similaridad multiplicando por la calificación de la persona
    sims = sims.map(lambda x: x * rating)
    # # Añadir el puntaje a la lista de candidatos similares
    simCandidates = simCandidates.append(sims) 
    # #Mirar los resultados:
    # #print ("ordenando...")
    simCandidates.sort_values(inplace = True, ascending = False)
    #print(type(simCandidates))

    simCandidates = simCandidates.groupby(simCandidates.index).sum()
    simCandidates.sort_values(inplace = True, ascending = False)
    #print(simCandidates.head(10))

    #print(myRatings)
    filteredSims = simCandidates.drop(anime,errors='ignore')
    #print(type(filteredSims))
    filteredSims = filteredSims.head()
    print(filteredSims.head())
    result = filteredSims.to_dict()
    
    return jsonify(result)



@app.route('/libros/recomendar_pkl/', methods=['GET'])
# book = Harry Potter and the Philosopher's Stone --> Ejemplo
def recomendar_libros_pkl():
    book = req.args.get('libro')
    rating = int(req.args.get('rating'))
    simCandidates = pd.Series()
    # Recuperar las pelis similares a las calificadas
    sims = creando_matriz_sin_nan(book)
    # Escalar la similaridad multiplicando por la calificación de la persona
    sims = sims.map(lambda x: x * rating)
    # Añadir el puntaje a la lista de candidatos similares
    simCandidates = agregando_sims(sims, simCandidates)
    #Mirar los resultados:
    simCandidates.sort_values(inplace = True, ascending = False)
    simCandidates = agrupando_sim_Candidates(simCandidates)
    simCandidates.sort_values(inplace = True, ascending = False)
    filteredSims = drop_en_simCandidates(simCandidates, book)
    filteredSims = filteredSims.head(6)
    result = creando_json_ajax(filteredSims)
    return jsonify(result)

def extraer_atributos_de_un_libro(nombre_libro):
    datosLibros = pd.read_pickle("/home/supay/datos/datos_proyecto/DB-libros.pkl")
    datosLibros = datosLibros.dropna()

    dataframeLibro = datosLibros.loc[datosLibros['Name'] == nombre_libro]
    dataframeLibro = dataframeLibro.head(1)
    listaLibro = dataframeLibro.values.tolist()

    print(listaLibro)
    return listaLibro


def creando_matriz_sin_nan(book):
    corrMatrix = pd.read_pickle("/home/supay/datos/datos_proyecto/corrLibros.pkl")
    return corrMatrix[book].dropna()

def creando_json_ajax(filteredSims):
    array_to_json_ajax = {}
    for x in range(len(filteredSims.index)):
        listalibro = extraer_atributos_de_un_libro(filteredSims.index[x])
        array_to_json_ajax[x]= {"Name": filteredSims.index[x],"Autor": listalibro[0][2], "Idioma": listalibro[0][3], "Paginas": listalibro[0][4]}

    return array_to_json_ajax

def agregando_sims(sims, simCandidates):
    return simCandidates.append(sims)

def agrupando_sim_Candidates(simCandidates):
    return simCandidates.groupby(simCandidates.index).sum()

def drop_en_simCandidates(simCandidates, book):
    return simCandidates.drop(book,errors='ignore')

def ordenando_simCandidates(simCandidates):
    return simCandidates.sort_values(inplace = True, ascending = False)