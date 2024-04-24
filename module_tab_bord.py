#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[1]:


## Fonction qui permet de recuperer les donnéées pour le primaire et collège
def get_submission_data():
    url = "https://kc.kobotoolbox.org/api/v1/data/1940653?format=json"
    params = {"format": "json"}
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    return df


# In[3]:


# ## Fonction qui permet de recuperer les donnéées pour le prescolaire
def get_submission_data_presc():
    url = "https://kc.kobotoolbox.org/api/v1/data/1929443?format=json"
    params = {"format": "json"}
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    return df


# In[2]:


def get_preparation_data(df):
    ## le vecteur qui contient le ocde avec les noms de cp
    correspondance_CP = {"300":"ABDILAHHI ARREH OMAR",
                "301":"ABDISALAM IBRAHIM ARREYEH","302":"ABDOUKADER MED AHMED","303":"ABDOULKADER ABOUBAKER HANIFA",
                "304":"ABDOULKADER APTION","305":"ABDOURAHMAN DAHER SAMATAR",
                "306":"ADEN AHMED FARAH","307":"AHMED ABDILLAHI ARREH","308":"AHMED ALI ELMI",
                "309":"ALI BEN ALI","310":"ALI DABALEH","311":"ALI DABAR",
                "312":"ALI LADIEH ISMAEL","313":"ARDO WAIS","314":"ARIHA AHMED",
                "315":"BOUHA HAMADOU","316":"CHARMARKE AHMED ELMI","317":"CHOUKRI MAHAMOUD OSMAN",
                "318":"CHOUKRI OMAR OUSMANE","319":"FARAH ALI ILTIREH","320":"HANAN SAID SALEH",
                "321":"HIBO ADEN ABDILAHHI","322":"HOUMED DINI CHEIK DINI","323":"HOUSSEIN ALI MOHAMED",
                "324":"HOUSSEIN IBRAHIM ARREYEH","325":"HOUSSEIN MOHAMED MOUGNI","326":"IBTIHAL ABDOU SAID",
                "327":"IDRISS MOUSKOULTA DAOUD","328":"ISMAN YOUFIS WALIEH","329":"KADAR ABDI IBRAHIM",
                "330":"KADAR MAHAMOUD ABANE","331":"KADRA ISMAN","332":"KAIREH ABDALLAH MOHAMED",
                "333":"KHALED IBRAHIM ALI","334":"MADINA MOUMIN ASSOWEH","335":"MOHAMED ABDALLAH WARSAMA",
                "336":"MOHAMED ABDILLAHI AHMED","337":"MOHAMED ABDILLAHI RAYALEH","338":"MOHAMED AHMED ILTIREH",
                "339":"MOHAMED AHMED OUFANE","340":"MOHAMED ALI DALIEH","341":"MOHAMED DJIBRIL",
                "342":"MOHAMED IBRAHIM MOHAMED","343":"MOHAMED ISMAIL WAIS","344":"MOHAMED MOUSSA DIRIEH",
                "345":"MOHAMED OSMAN","346":"MOHAMED WABERI OSMAN","347":"MOHAMED YOUSSOUF ROBLEH",
                "348":"MOUSSA OMAR DOUKSIEH","349":"MOUSSA OMAR DOUKSIEH","350":"MOUSTAPHA ANDRÉ MARIE CLAUDE",
                "351":"NAWAL SAID AWAD","352":"NOURADINE HOUSSEIN MOHAMED","353":"OMAR ABDI ALI",
                "354":"OMAR SALEM KASSIM","355":"OUBAH MOHAMED GUESSALEH","356":"RACHIDA OSMAN",
                "357":"RAMADAN YONIS DAHER","358":"SAAD MOHAMED ADEN","359":"SAPHA ABDOU ALI",
                "360":"SAREDO HASSAN FARAH","361":"SOULEIMAN HASSAN FOURREH","362":"SOULEIMAN OSMAN WABERI",
                "363":"TAMER MOHAMED SALEH","364":"YAHYA ALI OSMAN","365":"YASMIN OSMAN HASSAN",
                "366":"YOUSSOUF MOHAMED CHEHEM","367":"ZAHRA AHMED","368":"ZAHRA ISMAIL ABDOU",
                "369":"ZAKARIA SAID DJAMA","370":"Idil Djama Toukaleh","371":"Mohamed Farah Iltireh",
                "372":"ILHAM ABDOWAHAB OMAR"
            }
    colon_rep=['identification/region','identification/niveau', 'identification/nom',
           'Teacher_Identification/teacher_firstname']
    ## on recupère certains colonne du df
    data=df[colon_rep]
    ###########On renome les colonnes 
    data=data.rename(columns={'identification/region':"Region","identification/niveau":"Niveau",
                                      "identification/nom":"CP",
                                      "Teacher_Identification/teacher_firstname":"Enseignant"})
    ##dictionnaire de corespondance entre les regions et leur code
    code_region={"1": "Djibouti", "2": "ALI-SABIEH","3":"ARTA","4":"DIKHIL",
                  "5":"OBOCK","6":"TADJOURAH"}
    #### On change le code region par les noms de regions
    for index, row in data.iterrows():
        code_R = row['Region']
        if code_R in code_region:
            data.at[index, 'Region'] =code_region[code_R]
    ### on changes les codes des CP par leur nom
    for index, row in data.iterrows():
        code_cp = row['CP']
        if code_cp in correspondance_CP:
            data.at[index, 'CP'] = correspondance_CP[code_cp]

    # Créer un dictionnaire de correspondance du niveau
    code_niveau = {"1": "Primaire", "2": "Collège"}

    # Remplacer les valeurs numériques par leurs noms correspondants dans la colonne "niveau"
    data['Niveau'] = data['Niveau'].map(code_niveau)
    return data


# In[4]:


def get_preparation_data_pres(df):
    ## le vecteur qui contient le ocde avec les noms de cp
    liste_ensei={"200":'ASMA ISMAIL OMAR',"201":'ARAKSAN KAIREH ROBLEH',"202":'ARAKSAN MOHAMED HASSAN',
             "203":'AMINA HARBI KAYAD',
             "204": 'SOUMEYA OMAR GUEDI',"205":'ZEINAB ALI MOHAMED',"206":'NEIMA AINAN GUESSALEH',"207":'DEKA AHMED ABDILLAHI',
             "208":'NIMA ALI OUFFANEH',"209":'ZAM-ZAM ABDI ISSE',"210":'NEIMA GOULED OUMAR',"211":'SAADA HASSAN YONIS',
             "212":'ROUKYA DJAMA MIHINE',"213":'ASMA MAHDI MOUMIN',"214":'RAHMA ABDILLAHI AHMED',
             "215":'MOUNA ABDOURAHMAN SAID',"216":'MARWA MOHAMED HOUSSEIN',"217":'SAID AHMED',
             "218":'OUBAH AHMED HASSAN',"219":'SAFA ABDI IBRAHIM',"220":'IBRAHIM OSMAN OKIEH',
            "221":'AHMED ADEN MIGANEH',"222":'ARAFAT ABDILLAHI ADJAB',"223":'IFTIN ADEN AWALEH',
           "224":'AYAN ALI HOUSSEIN',"225":'NASTEHO SAID HASSAN',"226":'MOKTAR MOUSSA AHMED',
           "227":'FARHAN SALEH ROBLEH',"228":'NAGAD HOUSSEIN BOCK',"229":'ZEINAB FARAH MOUSSA',
          "230":'MALIKA ABDOULKADER CHEHEM',"231":'IFRAH ABDILLAHI AHMED',"232":'HALIMO SAID AHMED',
         "233":'HASNA MOUMIN ALI',"234":'DEKA SALAH ELMI',"235":'ARAKSAN ROBLEH GABAD',
        "236":'HAWA MOUSTAPHA MAHAMOUD',"237":'ASMA ISMAIL OMAR',"238":'IDIL ISMAIL SOULEIMAN',
       "239":'DEKA ISMAN HERSI',"240":'FATHIA MOHAMED ADOCH',"241":'HODAN MOUSTAPHA MOHAMED',
       "242":'ROUKIA OSMAN AÏNAN',"243":'NASTEHO IBRAHIM FARAH',"244":'BOGOREH DAHER',
       "245": 'NEIMA ABDI FARAH',"246":'FAHIMA OMAR DOUGSIEH',"247":'SAIDA DJAMA RAGUEH',
       "248":'OUBAH GUIRREH BARREH',"249":'KALTOUN FARAH OMAR',"250":'MARIAMA ALI MEDANE',
       "251":'KAFIA BILEH ABDI',"252":'YASSIN IDRISS IBRAHIM',"253":'RACHID DJAMA AHMED',
       "254":'HASNA DJAMA ARDEH',"255":'HAMDA ABDILLAHI BOUHANEH',"256":'SAIDA ABDALLAH WAIS',
       "257":'FATOUMA HASSAN MAÏN',"258":'ASWAN AWALEH HASSAN',"259":'HAWA MOUSSA ELMI',
       "260":'SIAD ROBLEH ADEN',"261":'FARDOUSSA ABDILLAHI MOUMIN',"262":'FATHIA ABDICHAFI MAHAMOUD',
      "263":'NASRA HASSAN YONIS',"264":'ZAKARIA MOHAMED ROBLEH',"265":'OSMAN NOUR IBRAHIM',
      "266":'IDIL ISMAN ROBLEH', "267":'SALEH NOUR OSMAN',"268":'SAID MOUSTAPHA MAHAMOUD',
      "269": 'MOUKTAR AHMED',"270":'HAFSA OSMAN AWALEH',"271":'ZEINABA ISSA KAMIL',
      "272":'IFRAH YOUSSOUF HOUSSEIN',"273":'MOHAMED ABDALLAH HASSAN',"274":'HASSAN ABDOURAHMAN OSMAN',
     "275":'ROUKIA ADEN ALI',"276":'MOHAMED HASSANLEH',"277":'HAMAD KABIR MOHAMED',
    "278":'WAHIB HASSAN MOUSSA',"279":'ABAYAZID ALI YOUSSOUF',"280":'RADWAN ABDI ALI',
   "281":'OUMA ABDALLAH HOUMAD'}
    liste_CP_presc={"600":"IBADO SOULEIMAN GUELLEH","601":"FATOUMA MOUSSA MOUMIN","602":"SAID AHMED IBRAHIM","603":"GAMAL MOHAMED",
                "604":"HABIBA ALI WALIEH","605":"ALI MOHAMED HASSAN MERITO","606":"HALIMA HASSAN ALLALEH",
                "607":"FATOUM ALI HOUMED","608":"NEIMA ABDI ILTIREH","609":"BOURHAN ABOUBAKER KASSIM",
                "610":"HALIMA HASSAN ALLALEH","611":"OMAR ALI GUELLEH","612":"HAWA OMAR OSMAN",
                "613":"ABDOUSALAM DJAMA KAYAD","614":"NABIHA MOHAMOUD","615":"Saada ibrahim olhayeh"
               }
    colon_pres=['precode/nom','precode/region', 'Teacher_Identification/enseig']
    data=df[colon_pres]
    ###########On renome les colonnes 
    data=data.rename(columns={"precode/nom":"CP","precode/region":"Region",
                                            "Teacher_Identification/enseig":"Enseignant",
                                      })
    ##dictionnaire de corespondance entre les regions et leur code
    code_ciro={"1": "ALI-SABIEH", "2": "ARTA","3":"DIKHIL","4":"Djibouti","5":"Djibouti","6":"Djibouti",
                  "7":"Djibouti","8":"Djibouti","9":"Djibouti","10":"OBOCK","11":"TADJOURAH"}
    #### On change le code region par les noms de regions
    for index, row in data.iterrows():
        code_R = row['Region']
        if code_R in code_ciro:
            data.at[index, 'Region'] =code_ciro[code_R]
        ### on changes les codes des CP par leur nom
    for index, row in data.iterrows():
        code_cp = row['CP']
        if code_cp in liste_CP_presc:
            data.at[index, 'CP'] =liste_CP_presc[code_cp]
    ### on changes les codes des enseignant par leur nom
    for index, row in data.iterrows():
        code_ens = row['Enseignant']
        if code_ens in liste_ensei:
            data.at[index, 'Enseignant'] =liste_ensei[code_ens]

    return data


# In[ ]:


### SOUMISSION PARVEAU
def get_soumission_par_niveau(df):
    # Compter le nombre d'occurrences de chaque niveau
    niveau_counts = df['Niveau'].value_counts()

    # Créer le diagramme en barres avec des barres plus fines
    plt.bar(niveau_counts.index, niveau_counts.values, width=0.1, color=['blue', 'green'])
    # Ajouter les valeurs sur les barres
    for i, count in enumerate(niveau_counts.values):
        plt.text(i, count, str(count), ha='center', va='bottom',fontsize=12, fontweight="bold")


    # Ajouter des labels et un titre avec des polices en gras et en couleur
    plt.title('Formulaire soumis par niveau', fontweight="bold", color="black", y=1.04)

    # Personnaliser les étiquettes de l'axe des x
    plt.xticks(niveau_counts.index, niveau_counts.index, color='red', fontweight='bold', fontsize=12)

    # Supprimer les valeurs de l'axe y
    plt.tick_params(axis='y', which='both', left=False, labelleft=False)
    # Ajuster les limites de l'axe y pour augmenter l'espace entre les barres et la ligne en haut du cadre
    plt.ylim(0, max(niveau_counts.values) * 1.1)  # Augmente les limites de 10% par rapport à la valeur maximale


    # Afficher le diagramme
    return plt


# In[ ]:


##SOUMISSION PAR REGION
def get_soumission_par_region(df):
    # Compter le nombre de soumissions par région
    region_counts = df['Region'].value_counts()

    # Liste de couleurs pour chaque région
    couleurs_regions = ['#d62728', '#9467bd', '#ff7f0e', '#17becf', '#bcbd22', '#e377c2']

    # Créer le diagramme en barres avec des couleurs différentes pour chaque région
    plt.bar(region_counts.index, region_counts.values, width=0.1, color=couleurs_regions[:len(region_counts)])

    # Ajouter les valeurs sur les barres
    for i, count in enumerate(region_counts.values):
        plt.text(i, count, str(count), ha='center', va='bottom',fontsize=12, fontweight="bold")

    # Ajouter des labels et un titre
    #plt.xlabel('Région', fontweight="bold", color="black")
    plt.title('Formulaires soumis par région', fontweight="bold", color="black", y=1.04)

    # Personnaliser les étiquettes de l'axe des x
    plt.xticks(region_counts.index, region_counts.index, color='red', fontweight='bold', fontsize=12)

    # Supprimer les valeurs de l'axe y
    plt.tick_params(axis='y', which='both', left=False, labelleft=False)

    # Ajuster les limites de l'axe y pour augmenter l'espace entre les barres et la ligne en haut du cadre
    plt.ylim(0, max(region_counts.values) * 1.1)  # Augmente les limites de 10% par rapport à la valeur maximale

    # Faire pivoter les étiquettes de l'axe x pour une meilleure lisibilité
    plt.xticks(rotation=45, ha='right')

    # Afficher le diagramme
    return plt


# In[ ]:


### elle donne un graphique qui represente le nbr de formulaire soumis par region et par cp
def graphique_soumissions_par_region_et_par_CP(region_selectionnee, df):
    # Filtrer les données pour la région sélectionnée
    df_region_selectionnee = df[df['Region'] == region_selectionnee]

    # Vérifier si le DataFrame pour la région sélectionnée est vide
    if df_region_selectionnee.empty:
        plt.text(0.5, 0.5, f"Pas de formulaire soumis pour {region_selectionnee} pour l'instant", ha='center', va='center', fontsize=12)
        plt.axis('off')  # Masquer les axes
    else:
        # Compter le nombre de soumissions par enquêteur pour la région sélectionnée
        enqueteur_counts = df_region_selectionnee['CP'].value_counts()

        # Créer une liste de couleurs en alternance
        couleurs = ['lightcoral', 'mediumpurple'] * ((len(enqueteur_counts) + 1) // 2)

        # Créer le diagramme en barres avec les couleurs en alternance
        plt.bar(enqueteur_counts.index, enqueteur_counts.values, width=0.1, color=couleurs[:len(enqueteur_counts)])

        # Ajouter les valeurs sur les barres
        for i, count in enumerate(enqueteur_counts.values):
            plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12, fontweight="bold")

        # Ajouter des labels et un titre
       # plt.title(f'Formulaires soumis pour la région {region_selectionnee} par CP', fontweight="bold", color="black", y=1.04)

        # Supprimer les valeurs de l'axe y
        plt.tick_params(axis='y', which='both', left=False, labelleft=False)

        # Ajuster les limites de l'axe y pour augmenter l'espace entre les barres et la ligne en haut du cadre
        plt.ylim(0, max(enqueteur_counts.values) * 1.1)  # Augmente les limites de 10% par rapport à la valeur maximale

        # Faire pivoter les étiquettes de l'axe x pour une meilleure lisibilité
        plt.xticks(rotation=45, ha='right')

    # Afficher le diagramme
    return plt


# In[ ]:


def get_enquetes_par_CP(nom_enqueteur, df):
    # Filtrer les données pour le CP sélectionné
    df_enqueteur = df[df['CP'] == nom_enqueteur]

    # Vérifier si le DataFrame pour le CP sélectionné est vide
    if df_enqueteur.empty:
        # Afficher un message si le DataFrame est vide
        print(f"Pas de formulaire soumis pour Mr. {nom_enqueteur} pour l'instant")
        return None
    else:
        # Extraire les enseignants évalués par cet enquêteur de la colonne "Enseignant"
        enquetes = df_enqueteur['Enseignant'].unique()

        # Créer une table contenant les enseignants évalués par cet enquêteur
        table_enquetes = df[df['Enseignant'].isin(enquetes)]

        return table_enquetes


# In[ ]:





# In[ ]:


def graphique_soumissions_par_region_et_par_niveau(region_selectionnee, df_prim_col):
    # Filtrer les données pour la région sélectionnée
    df_region_selectionnee = df_prim_col[df_prim_col['Region'] == region_selectionnee]

    # Vérifier si le DataFrame pour la région sélectionnée est vide
    if df_region_selectionnee.empty:
        plt.text(0.5, 0.5, f"Pas de formulaire soumis pour {region_selectionnee} pour l'instant", ha='center', va='center', fontsize=12)
        plt.axis('off')  # Masquer les axes
    else:
        # Compter le nombre de soumissions par enquêteur pour la région sélectionnée
        enqueteur_counts = df_region_selectionnee['Niveau'].value_counts()

        # Créer une liste de couleurs en alternance
        couleurs = ['lightcoral', 'mediumpurple'] * ((len(enqueteur_counts) + 1) // 2)

        # Créer le diagramme en barres avec les couleurs en alternance
        plt.bar(enqueteur_counts.index, enqueteur_counts.values, width=0.1, color=couleurs[:len(enqueteur_counts)])

        # Ajouter les valeurs sur les barres
        for i, count in enumerate(enqueteur_counts.values):
            plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12, fontweight="bold")

        # Ajouter des labels et un titre
       # plt.title(f'Formulaires soumis pour la région {region_selectionnee} par niveau', fontweight="bold", color="black", y=1.04)

        # Supprimer les valeurs de l'axe y
        plt.tick_params(axis='y', which='both', left=False, labelleft=False)

        # Ajuster les limites de l'axe y pour augmenter l'espace entre les barres et la ligne en haut du cadre
        plt.ylim(0, max(enqueteur_counts.values) * 1.1)  # Augmente les limites de 10% par rapport à la valeur maximale

        # Faire pivoter les étiquettes de l'axe x pour une meilleure lisibilité
        plt.xticks(rotation=45, ha='right')

    # Afficher le diagramme
    return plt


# In[ ]:


def graphique_soumissions_par_niveau_reg(niveau_selectionnee, df):
    # Filtrer les données pour la région sélectionnée
    df_niveau_selectionnee = df[df['Niveau'] == niveau_selectionnee]

    # Vérifier si le DataFrame pour la région sélectionnée est vide
    if df_niveau_selectionnee.empty:
        plt.text(0.5, 0.5, "Pas de formulaire soumis pour l'instant", ha='center', va='center', fontsize=12)
        plt.axis('off')  # Masquer les axes
    else:
        # Compter le nombre de soumissions par region pour le niveau sélectionnée
        enqueteur_counts = df_niveau_selectionnee['Region'].value_counts()

        # Créer une liste de couleurs en alternance
        couleurs = ['lightcoral', 'mediumpurple'] * ((len(enqueteur_counts) + 1) // 2)

        # Créer le diagramme en barres avec les couleurs en alternance
        plt.bar(enqueteur_counts.index, enqueteur_counts.values, width=0.1, color=couleurs[:len(enqueteur_counts)])

        # Ajouter les valeurs sur les barres
        for i, count in enumerate(enqueteur_counts.values):
            plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12, fontweight="bold")

        # Ajouter des labels et un titre
       # plt.title(f'Formulaires soumis pour le {niveau_selectionnee}\n par région', fontweight="bold", color="black", y=1.04)

        # Supprimer les valeurs de l'axe y
        plt.tick_params(axis='y', which='both', left=False, labelleft=False)

        # Ajuster les limites de l'axe y pour augmenter l'espace entre les barres et la ligne en haut du cadre
        plt.ylim(0, max(enqueteur_counts.values) * 1.1)  # Augmente les limites de 10% par rapport à la valeur maximale

        # Faire pivoter les étiquettes de l'axe x pour une meilleure lisibilité
        plt.xticks(rotation=45, ha='right')

    # Afficher le diagramme
    return plt


# In[ ]:


liste_Ens=["ASMA ISMAIL OMAR","ARAKSAN KAIREH ROBLEH","ARAKSAN MOHAMED HASSAN","AMINA HARBI KAYAD",                                  
           "SOUMEYA OMAR GUEDI",
            "ZEINAB ALI MOHAMED",         
            "NEIMA AINAN GUESSALEH",                           
            "DEKA AHMED ABDILLAHI",                               
            "NIMA ALI OUFFANEH", 
            "ZAM-ZAM ABDI ISSE",
            "NEIMA GOULED OUMAR",
            "SAADA HASSAN YONIS",
            "ROUKYA DJAMA MIHINE",
            "ASMA MAHDI MOUMIN",   
            "RAHMA ABDILLAHI AHMED",                      
            "MOUNA ABDOURAHMAN SAID", 
            "MARWA MOHAMED HOUSSEIN",
            "SAID AHMED", 
            "OUBAH AHMED HASSAN",
            "SAFA ABDI IBRAHIM",
            "IBRAHIM OSMAN OKIEH",      
            "AHMED ADEN MIGANEH",    
            "ARAFAT ABDILLAHI ADJAB",        
            "IFTIN ADEN AWALEH",   
            "AYAN ALI HOUSSEIN",  
            "NASTEHO SAID HASSAN",   
            "MOKTAR MOUSSA AHMED",       
            "FARHAN SALEH ROBLEH",      
            "NAGAD HOUSSEIN BOCK",    
            "ZEINAB FARAH MOUSSA",  
            "MALIKA ABDOULKADER CHEHEM",   
            "IFRAH ABDILLAHI AHMED",
            "HALIMO SAID AHMED",
            "HASNA MOUMIN ALI",
            "DEKA SALAH ELMI",
            "ARAKSAN ROBLEH GABAD",
            "HAWA MOUSTAPHA MAHAMOUD",
            "ASMA ISMAIL OMAR",
            "IDIL ISMAIL SOULEIMAN",
            "DEKA ISMAN  HERSI",       
            "FATHIA MOHAMED ADOCH",
            "HODAN MOUSTAPHA MOHAMED",
            "ROUKIA OSMAN AÏNAN",                             
            "NASTEHO IBRAHIM FARAH",
            "BOGOREH DAHER",
            "NEIMA ABDI FARAH",
            "FAHIMA OMAR DOUGSIEH",                
            "SAIDA DJAMA RAGUEH",                    
            "OUBAH GUIRREH BARREH",                   
            "KALTOUN FARAH OMAR",
            "MARIAMA ALI MEDANE",
            "KAFIA BILEH ABDI",
            "YASSIN IDRISS IBRAHIM",                    
            "RACHID DJAMA AHMED",                  
            "HASNA DJAMA ARDEH",                       
            "HAMDA  ABDILLAHI BOUHANEH"
            "SAIDA ABDALLAH WAIS",
            "FATOUMA HASSAN MAÏN",      
            "ASWAN AWALEH HASSAN",
            "HAWA MOUSSA ELMI",                                 
            "SIAD ROBLEH ADEN",
            "FARDOUSSA ABDILLAHI MOUMIN",  
            "FATHIA ABDICHAFI MAHAMOUD",  
            "NASRA HASSAN YONIS", 
            "ZAKARIA MOHAMED ROBLEH",  
            "OSMAN NOUR IBRAHIM",     
            "IDIL ISMAN ROBLEH",
            "SALEH NOUR OSMAN",                            
            "SAID  MOUSTAPHA MAHAMOUD",             
            "MOUKTAR AHMED",                                
            "HAFSA OSMAN AWALEH",
            "ZEINABA ISSA KAMIL",  
            "IFRAH YOUSSOUF HOUSSEIN",
            "MOHAMED ABDALLAH HASSAN", 
            "HASSAN ABDOURAHMAN OSMAN",
            "ROUKIA ADEN ALI",                 
            "MOHAMED HASSANLEH",
            "HAMAD KABIR MOHAMED",       
            "WAHIB HASSAN MOUSSA",         
            "ABAYAZID ALI YOUSSOUF",         
            "RADWAN ABDI ALI",
            "OUMA ABDALLAH HOUMAD"]


# In[5]:


liste_CP_presc=["IBADO SOULEIMAN GUELLEH","FATOUMA MOUSSA MOUMIN","SAID AHMED IBRAHIM","GAMAL MOHAMED",
                "HABIBA ALI WALIEH","6ALI MOHAMED HASSAN MERITO","HALIMA HASSAN ALLALEH",
                "FATOUM ALI HOUMED","NEIMA ABDI ILTIREH","BOURHAN ABOUBAKER KASSIM",
                "HALIMA HASSAN ALLALEH","OMAR ALI GUELLEH","HAWA OMAR OSMAN",
                "ABDOUSALAM DJAMA KAYAD","NABIHA MOHAMOUD","Saada ibrahim olhayeh"]

