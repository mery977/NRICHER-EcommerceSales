# Analyse des facteurs influençant les ventes de matelas

# Analyse de la corrélation entre les variables
correlation_matrix = df_matelas.corr()

# Visualisation de la corrélation avec un heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Corrélation entre les variables')
plt.show()

# Analyse des tendances temporelles des ventes
df_matelas['Mois'] = df_matelas['Date de commande'].dt.month
monthly_sales = df_matelas.groupby('Mois')['Quantité'].sum()

# Visualisation des tendances mensuelles des ventes
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Tendances mensuelles des ventes de matelas')
plt.xlabel('Mois')
plt.ylabel('Quantité Vendue')
plt.show()

# Analyse des ventes en fonction de l'univers
univers_sales = df_matelas.groupby('Univers')['Quantité'].sum()

# Visualisation des ventes par univers
plt.figure(figsize=(10, 6))
univers_sales.plot(kind='bar', color='lightcoral')
plt.title('Ventes de matelas par univers')
plt.xlabel('Univers')
plt.ylabel('Quantité Vendue')
plt.show()

# Analyse des ventes en fonction du vendeur
vendeur_sales = df_matelas.groupby('Vendeur')['Quantité'].sum()

# Visualisation des ventes par vendeur
plt.figure(figsize=(12, 6))
vendeur_sales.plot(kind='bar', color='lightgreen')
plt.title('Ventes de matelas par vendeur')
plt.xlabel('Vendeur')
plt.ylabel('Quantité Vendue')
plt.show()
