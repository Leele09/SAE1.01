from geopy.geocoders import Nominatim

def localisation(dico_lycee, dico_UAI):
    '''
    Fonction qui établit une jointure entre le dictionnaire des lycées avec le dico d'UAI à partir des UAI
    correspondant.
    :return Un dictionnaire contenant les informations sur les lycées avec leurs localisations
    '''
    # Remplissage des coordonnées pour chaque lycee
    for c, v in dico_lycee.items():
        # Cas ou l'UAI ne se trouve pas dans la base de donnée du gouv ou que l'UAI du lycée est inconnu --> recherche par geopy
        if v[2] not in dico_UAI or v[2] is None:
            adresse = str(c) + " , France"
            geolocator = Nominatim(user_agent="myGeocoder", timeout=3)
            location = geolocator.geocode(adresse)
            if location is not None:
                v.append((location.latitude, location.longitude))
            else:
                v.append(None)
        else:
            v.append(dico_UAI[v[2]])
        print(c, v)  # Pour voir etape par etape le remplissage des coordonnés
    return dico_lycee