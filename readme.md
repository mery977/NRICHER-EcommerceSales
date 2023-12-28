Analyse des Ventes d'E-commerce
Ce script Python a été développé dans le cadre d'une analyse des ventes du site d'e-commerce NRICHER. L'objectif est d'explorer, nettoyer les données, et générer des visualisations pour comprendre les tendances de vente.

Instructions
1. Installation des Dépendances
Exécuter les commandes suivantes pour installer les bibliothèques Python nécessaires : pip install pandas plotly seaborn matplotlib

2. Exécution du Script
Lancer le script Python avec la commande suivante :

$$python sales.py

3. Fonctionnalités
* Nettoyage des Données
Le script effectue une opération de nettoyage pour éliminer les lignes avec des valeurs manquantes, assurant ainsi des analyses précises.

* Recatégorisation
J'ai éxécuté une fonction spécifique pour corriger les catégories mal étiquetées dans la colonne 'Nature'.

* Extraction de Dimensions et Couleurs
J'ai réalisé une fonction dédiée permettant d'extraire les informations de dimensions et couleurs à partir de la colonne 'Libellé produit'.

* Graphique d'Évolution des Ventes de Matelas
Le script génère un graphique interactif illustrant l'évolution des ventes de matelas au fil du temps, offrant une vue claire des tendances. PS: Méme si, ya un script qui génére des graphiques, tous les graphes ont été réalisé par Tableau Software

4. Fichiers de Sortie
Nouveaux-dimensions-couleurs.csv : Fichier contenant les données après recatégorisation et extraction de dimensions et couleurs. NETTOYAGE.csv : Fichier contenant les données après le processus de nettoyage.

5. Structure du Projet
sales.py : Le script principal pour l'analyse des ventes. README.md : Le fichier que vous lisez actuellement, fournissant des informations détaillées sur le projet.

Auteur : EL ALAOUI HASSANI Meryem Date : 27/12/2023
