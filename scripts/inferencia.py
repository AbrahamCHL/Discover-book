
import pandas as pd

corrMatrix = pd.read_pickle("/home/supay/datos/datos_proyecto/corrLibros.pkl")
print(corrMatrix)


book = 'The Old Man and the Sea'
rating = 5

simCandidates = pd.Series()
#print(simCandidates)
# Recuperar las pelis similares a las calificadas
sims = corrMatrix[book].dropna()
# Escalar la similaridad multiplicando por la calificación de la persona
sims = sims.map(lambda x: x * rating)
# Añadir el puntaje a la lista de candidatos similares
simCandidates = simCandidates.append(sims)
    
#Mirar los resultados:
#print ("ordenando...")
simCandidates.sort_values(inplace = True, ascending = False)
#print (simCandidates.head())

simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
#simCandidates.head()

#print(myRatings)
filteredSims = simCandidates.drop(book,errors='ignore')
print(filteredSims.head(10))