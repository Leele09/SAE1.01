import folium as fo
from folium.plugins import MarkerCluster
import pandas as pd



def dico_to_map(Dico_lycee):
    '''
    Fonction qui place des marqueurs sur une map(openstreet map) avec le dictionnaire de localisation pour chaque lycée
    ainsi que leurs information dans un popup
    :return: un fichier .html contenant les marqueur de lycées
    '''

    # on initialise la map
    zone_map = fo.Map(location=[48.856614, 2.352222], zoom_start=12)

    # on place le marqueur de l'iut
    fo.Marker(location=[48.77698507990875, 2.3757302721547573],
              tooltip="UAI : 0942072S<br><h3>IUT UPEC Ivry</h3><br>122 rue Paul Armangot,<br>Parc Chérioux 94400 Vitry-sur-Seine ",
              icon=fo.Icon(color="red", icon='school')).add_to(zone_map)

    # on crée le cluster, c'est ce qui va regrouper les marqueurs
    marker_cluster = MarkerCluster().add_to(zone_map)

    # dans cette boucle on va parcourir le dico et récuperer les informations pour placer les marqueurs
    for lycee, localisation in Dico_lycee.items():
        # on verifie que l'emplacement des coordonnes n'est pas vide
        if localisation[4] is not None:
            # on stock les données des étudiants qui correspond à localisation[3] sous forme de dataframe dans une variable
            html = pd.DataFrame(localisation[3])

            # cette variable on l'a converti en html et on en crée un iframe
            iframe = fo.IFrame(html.to_html())

            # on définie que le popup contient l'iframe, et on definie ses dimensions
            popup = fo.Popup(iframe,
                             min_height=300,
                             max_height=300,
                             min_width=500,
                             max_width=500)

            # on peut maintnant placer le marqueur on prend la longitude et latitude qui correspond à localisation[4][0], localisation[4][1]
            fo.Marker(location=(localisation[4][0], localisation[4][1]),

                      # tooltip correspond au popup provisoire avec les infos de l'établissement
                      tooltip=(
                          f"UAI : {localisation[2]}<h3>{lycee}</h3>{localisation[1]}<br>Département : {int(localisation[0])}"),

                      # on definie le popup avec la variable que nous avions definie avec le iframe
                      # et on additionne le marqueurs au cluster
                      popup=popup).add_to(marker_cluster)

    # pour finir on sauvegarde le fichier html
    return zone_map.save('index.html')