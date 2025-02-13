import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

notas = pd.read_csv('ratings.csv')
notas

notas.shape

notas.columns = ['usuarioID', 'filmeID', 'nota', 'momento']

notas["nota"].unique()

notas["nota"].value_counts()

notas["nota"].mean()

notas["nota"].plot(kind='hist')

notas["nota"].median()

mediana = notas["nota"].median()
media = notas["nota"].mean()
print(f"Mediana é {mediana}")
print(f"Média é {media}")

notas["nota"].describe()

sns.boxplot(notas["nota"])
