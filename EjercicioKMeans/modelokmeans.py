#Importar las librerías necesarias.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

#Cargar el dataset.
df = pd.read_csv("Mall_Customers.csv")
print(df.head(10))
print(df.shape)# Para ver filas y columnas

print(df.info())
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Lista para almacenar la suma de los errores cuadráticos (WCSS)
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(8,5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.title('Método del Codo para encontrar el K óptimo')
plt.show()

#Aplico el k más optimo según la curvatura del gráfico anterior.
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X)
print("Centroides de los clusters:\n", kmeans.cluster_centers_)

plt.figure(figsize=(8,6))
sns.scatterplot(x=df['Annual Income (k$)'], y=df['Spending Score (1-100)'], 
                hue=df['Cluster'], palette='viridis', s=100)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            s=300, c='red', label='Centroides', marker='X')
plt.xlabel('Ingresos Anuales(k$) de clientes')
plt.ylabel('Puntuación de Gastos de cliente')
plt.title('Agrupación de los clientes con K-Means')
plt.legend()
plt.show()