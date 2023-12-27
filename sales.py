import csv
import pandas as pd
import re
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\ADMIN\Desktop\PROJECTS\NRICHER_PROJECTS\20210614Ecommercesales.csv',encoding='latin-1', sep=';')
print(df.head())
print(df.columns)

# Fonction de recatégorisation
def recategoriser_lignes(df):
    # Trouver les catégories uniques dans la colonne 'Nature'
    categories_uniques = df['Nature'].unique()

    # Parcourir toutes les catégories uniques
    for categorie in categories_uniques:
        if pd.notna(categorie):  # Ignorer les valeurs NaN
            # Filtrer les lignes mal catégorisées pour une catégorie donnée
            lignes_mal_categorisees = (df['Nature'].str.lower() == categorie.lower()) & (df['Nature'] != categorie)

            # Recatégoriser les lignes mal catégorisées avec la catégorie actuelle
            df.loc[lignes_mal_categorisees, 'Nature'] = categorie

# Appliquer la fonction de recatégorisation
#recategoriser_lignes(df)

# Fonction pour extraire dimensions et couleurs
df.to_csv(r'C:\Users\ADMIN\Desktop\PROJECTS\NRICHER_PROJECTS\NouveauFichier.csv', index=False, encoding='latin-1', sep=';')

# Fonction pour extraire dimensions et couleurs
def extraire_dimensions_couleurs(description):
    dimensions_pattern = re.compile(r'(\d{2,3}\s?[xX]\s?\d{2,3})')
    couleurs_pattern = re.compile(r'(bleu|rouge|vert|jaune|orange|violet|marron|noir|blanc|gris)')

    dimensions_match = dimensions_pattern.search(description)
    couleurs_match = couleurs_pattern.finditer(description)

    dimensions = dimensions_match.group(1) if dimensions_match else None
    couleurs = [match.group(1) for match in couleurs_match] if couleurs_match else None

    return dimensions, couleurs

# Exemple d'utilisation
description_exemple = "Canapé avec des coussins rouges et bleus, dimensions 140x190 cm"
dimensions, couleurs = extraire_dimensions_couleurs(description_exemple)

print("Dimensions:", dimensions)
print("Couleurs:", couleurs)

# Appliquer la recatégorisation
recategoriser_lignes(df)

# Appliquer l'extraction des dimensions et couleurs
df[['Dimensions', 'Couleurs']] = df['Libellé produit'].apply(extraire_dimensions_couleurs).apply(pd.Series)

df.to_csv(r'C:\Users\ADMIN\Desktop\PROJECTS\NRICHER_PROJECTS\Nouveaux.csv', index=False, encoding='latin-1', sep=';')

# Remplacer les valeurs manquantes dans la colonne 'Nature' par une chaîne vide
df['Nature'] = df['Nature'].fillna('')

# Filtrer les lignes pour les matelas
df_matelas = df[df['Nature'].str.lower().str.contains('matelas')]

# Nettoyer les données en supprimant les lignes avec des valeurs manquantes
df_matelas = df_matelas.dropna(subset=['Date de commande', 'Quantité'])

df.to_csv(r'C:\Users\ADMIN\Desktop\PROJECTS\NRICHER_PROJECTS\NETTOYAGE.csv', index=False, encoding='latin-1', sep=';')

# Créer le graphique d'évolution des ventes pour les matelas
fig = make_subplots(rows=1, cols=1, subplot_titles=['Évolution des Ventes de Matelas'])

# Ajouter le graphique d'évolution des ventes
fig.add_trace(go.Scatter(x=df_matelas['Date de commande'], y=df_matelas['Quantité'],
                         mode='lines+markers', name='Ventes de Matelas'))

# Mettre à jour la mise en page du graphique
fig.update_layout(title_text='Évolution des Ventes de Matelas', xaxis_title='Date', yaxis_title='Quantité Vendue')

# Afficher le graphique
fig.show()



