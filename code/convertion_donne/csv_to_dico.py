
def csv_to_dico(data_parcousup, data_UAI):
    '''
    Fonction qui renvoie 2 dictionnaires remplit utilisant les base de donné du data parcousup
    et du gouvernement utile au SIG
    '''
    # On crée les dictionnaires utiles
    dico_lycee = {}
    dico_id = {}
    dico_etu = {i: {"Numéro": [], "Nom": [], "Prénom": [], "Sexe": [], "Profil du candidat": [], "Série": []} for i in
                data_parcousup["Libellé établissement"]}

    # On remplit le dico etudiant contenant les informations de tous les étudiants pour un lycée
    for i in range(len(data_parcousup["Numéro"])):
        for k in ["Numéro","Nom","Prénom","Sexe","Profil du candidat","Série"]:
            dico_etu[data_parcousup["Libellé établissement"][i]][k].append(data_parcousup[k][i])

    # Remplissage du dico_lycee {lycée:[departement , commune , UAI,{dico_etudiant}]}
    for lycee in range(len(data_parcousup["Libellé établissement"])):
        # On verifie que le lycé n'est pas encore renseigné dans le dico
        if data_parcousup["Libellé établissement"][lycee] not in dico_lycee:
            # On exclu les lycée hors ile de france
            if data_parcousup["Département établissement"][lycee] in [75, 77, 78, 91, 92, 93, 94, 95]:
                dico_lycee[data_parcousup["Libellé établissement"][lycee]] = [data_parcousup["Département établissement"][lycee],
                                                                      data_parcousup["Commune établissement"][lycee],
                                                                      data_parcousup["UAI établissement"][lycee],
                                                                      # On établit une jointure entre le dico etu et lycee
                                                                      dico_etu[data_parcousup["Libellé établissement"][lycee]]]

    # dico_id {UAI :(latitude, longitude)}
    for id in range(len(data_UAI["Code Ã©tablissement"])):
        dico_id[data_UAI["Code Ã©tablissement"][id]] = (data_UAI["Latitude"][id], data_UAI["Longitude"][id])

    return dico_lycee, dico_id