from convertion_donne.csv_to_dico import csv_to_dico
from convertion_donne.localisation import localisation
from convertion_donne.dico_to_map import dico_to_map
import pandas as pd
import webbrowser

# On convertit les fichiers CSV en dictionnaire
url = "base_donnee/data-parcoursup.csv"
df_CSV = pd.read_csv(url, sep=';', encoding="latin-1")

coordonne = "base_donnee/fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre.csv"
df_coordonne = pd.read_csv(coordonne, sep=';', encoding="latin-1")

if __name__ == '__main__':
    # On stocke les informations sur les lycées et des candidats dans une variable
    info_lyce = csv_to_dico(df_CSV,df_coordonne)[0]
    # On stocke la position (longitude, latitude) des lycées dans une autre variable
    position_lyce = csv_to_dico(df_CSV,df_coordonne)[1]

    # On génère une carte avec des marqueurs en renseignant la position et les informations des lycées
    # qui est ensuite stocker dans un fichier "index.html"
    dico_to_map(localisation(info_lyce, position_lyce))


    # On ouvre la page grace au module webbrowser
    webbrowser.open_new_tab("index.html")










