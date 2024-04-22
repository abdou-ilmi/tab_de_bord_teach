#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:53:02 2024

@author: ilham
"""
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from module_tab_bord import get_submission_data
from module_tab_bord import get_submission_data_presc
from module_tab_bord import get_preparation_data
from module_tab_bord import get_soumission_par_niveau
from module_tab_bord import get_soumission_par_region
from module_tab_bord import get_enquetes_par_CP
from module_tab_bord import graphique_soumissions_par_region_et_par_CP
from module_tab_bord import graphique_soumissions_par_region_et_par_niveau
from module_tab_bord import graphique_soumissions_par_niveau_reg
from module_tab_bord import liste_CP_presc
from module_tab_bord import get_preparation_data_pres
## le vecteur qui contient le ocde avec les noms de cp
liste_CP=["ABDISALAM IBRAHIM ARREYEH","ABDOUKADER MED AHMED","ABDOULKADER ABOUBAKER HANIFA",
                "ABDOULKADER APTION","ABDOURAHMAN DAHER SAMATAR",
                "ADEN AHMED FARAH","AHMED ABDILLAHI ARREH","AHMED ALI ELMI",
                "ALI BEN ALI","ALI DABALEH","ALI DABAR",
                "ALI LADIEH ISMAEL","ARDO WAIS","ARIHA AHMED",
                "BOUHA HAMADOU","CHARMARKE AHMED ELMI","CHOUKRI MAHAMOUD OSMAN",
                "CHOUKRI OMAR OUSMANE","FARAH ALI ILTIREH","HANAN SAID SALEH",
                "HIBO ADEN ABDILAHHI","HOUMED DINI CHEIK DINI","HOUSSEIN ALI MOHAMED",
                "HOUSSEIN IBRAHIM ARREYEH","HOUSSEIN MOHAMED MOUGNI","IBTIHAL ABDOU SAID",
                "IDRISS MOUSKOULTA DAOUD","ISMAN YOUFIS WALIEH","KADAR ABDI IBRAHIM",
                "KADAR MAHAMOUD ABANE","KADRA ISMAN","KAIREH ABDALLAH MOHAMED",
                "KHALED IBRAHIM ALI","MADINA MOUMIN ASSOWEH","MOHAMED ABDALLAH WARSAMA",
                "MOHAMED ABDILLAHI AHMED","MOHAMED ABDILLAHI RAYALEH","MOHAMED AHMED ILTIREH",
                "MOHAMED AHMED OUFANE","MOHAMED ALI DALIEH","MOHAMED DJIBRIL",
                "MOHAMED IBRAHIM MOHAMED","MOHAMED ISMAIL WAIS","MOHAMED MOUSSA DIRIEH",
                "MOHAMED OSMAN","MOHAMED WABERI OSMAN","MOHAMED YOUSSOUF ROBLEH",
                "MOUSSA OMAR DOUKSIEH","MOUSSA OMAR DOUKSIEH","MOUSTAPHA ANDRÉ MARIE CLAUDE",
                "NAWAL SAID AWAD","NOURADINE HOUSSEIN MOHAMED","OMAR ABDI ALI",
                "OMAR SALEM KASSIM","OUBAH MOHAMED GUESSALEH","RACHIDA OSMAN",
                "RAMADAN YONIS DAHER","SAAD MOHAMED ADEN","SAPHA ABDOU ALI",
                "SAREDO HASSAN FARAH","SOULEIMAN HASSAN FOURREH","SOULEIMAN OSMAN WABERI",
                "TAMER MOHAMED SALEH","YAHYA ALI OSMAN","YASMIN OSMAN HASSAN",
                "YOUSSOUF MOHAMED CHEHEM","ZAHRA AHMED","ZAHRA ISMAIL ABDOU",
                "ZAKARIA SAID DJAMA","Idil Djama Toukaleh","Mohamed Farah Iltireh",
                "ILHAM ABDOWAHAB OMAR"]
# Fonction pour récupérer les données des soumissions par agent
def get_formulaire_par_CP(nom_enqueteur, df):
    # Filtrer les données pour le CP sélectionné
    df_enqueteur = df[df['CP'] == nom_enqueteur]

    # Vérifier si le DataFrame pour le CP sélectionné est vide
    if df_enqueteur.empty:
        # Afficher un message si le DataFrame est vide
        st.write(f"Pas de formulaire soumis pour Mr. {nom_enqueteur} pour l'instant")
        return None
    else:
        # Extraire les enseignants évalués par cet enquêteur de la colonne "Enseignant"
        enquetes = df_enqueteur['Enseignant'].unique()

        # Créer une table contenant les enseignants évalués par cet enquêteur
        table_enquetes = df[df['Enseignant'].isin(enquetes)]

        return table_enquetes
## Fonction qui permet de recuperer les donnéées pour le primaire et collège
# def get_submission_data():
#     url = "https://kc.kobotoolbox.org/api/v1/data/1940653?format=json"
#     params = {"format": "json"}
#     response = requests.get(url, params=params)
#     data = response.json()
#     df = pd.DataFrame(data)
#     return df
# ## Fonction qui permet de recuperer les donnéées pour le prescolaire
# def get_submission_data_presc():
#     url = "https://kc.kobotoolbox.org/api/v1/data/1929443?format=json"
#     params = {"format": "json"}
#     response = requests.get(url, params=params)
#     data = response.json()
#     df = pd.DataFrame(data)
#     return df
# Appel de la fonction pour récupérer les données dès le début du script
data = get_submission_data()
data_pres = get_submission_data_presc()
df_presc=get_preparation_data_pres(data_pres)
df_prim_col=get_preparation_data(data)
df_col=df_prim_col[df_prim_col['Niveau'] =="Collège"]
df_prim=df_prim_col[df_prim_col['Niveau'] =="Primaire"]
vect_region= ["Djibouti", "ALI-SABIEH", "ARTA", "DIKHIL", "OBOCK", "TADJOURAH"]
vect_niveau=["Collège","Primaire"]
# Nombre total de formulaires prévus
total_formulaires =586 # Remplacez par le nombre total de formulaires prévus
total_formulaires_pres=82

# Nombre de formulaires soumis jusqu'à présent (hypothétique, remplacez par la logique réelle)
nombre_formulaires_soumis = len(df_prim_col) # Par exemple

# Calculer le pourcentage de formulaires soumis par rapport au total prévu
pourcentage_soumissions = (nombre_formulaires_soumis / total_formulaires)


#################prescolaire
# Nombre de formulaires soumis jusqu'à présent (hypothétique, remplacez par la logique réelle)
nombre_formulaires_soumis_pres = len(df_presc) # Par exemple

# Calculer le pourcentage de formulaires soumis par rapport au total prévu
pourcentage_soumissions_pres = (nombre_formulaires_soumis_pres/ total_formulaires_pres)


def main():

    

     
    # Chemin vers les images
    #chemin_image1 = "/home/ilham/Documents/tab_de_bord_teach/image_ece.PNG"
    #chemin_image2 = "/home/ilham/Documents/tab_de_bord_teach/image_edu.png"
    #col1, _, col2 = st.columns([1, 1, 1])
    # Utiliser les colonnes pour ajuster l'espace entre les images
    col1, _, col2, _, col3 = st.columns([1, 2, 1, 2, 1])
    # Utiliser les colonnes pour afficher les images côte à côte
    #col1, col2 = st.columns(2)
    
    # Afficher l'image 1 dans la première colonne
    with col1:
        st.image("/home/ilham/Documents/tab_de_bord_teach/image_ece.PNG", width=100, caption='', use_column_width=False)
      # Afficher un espace vide entre les colonnes
    col2.empty()   
         
    # Afficher l'image 2 dans la deuxième colonne
    with col3:
        st.image("/home/ilham/Documents/tab_de_bord_teach/image_edu.png", width=100, caption='', use_column_width=False,
                  output_format='auto')
#################################
    # col1, _, col2, _, col3 = st.columns([1, 1.5, 1, 1.5, 1])
    #  # Utiliser les colonnes pour afficher les images côte à côte
    #  #col1, col2 = st.columns(2)
     
    #  # Afficher l'image 1 dans la première colonne
    # with col1:
    #      st.write("Enseignants au collège:199")
    #   # Afficher un espace vide entre les colonnes
    # #col2.empty() 
    # with col2:
    #      st.write("Enseignants en préscolaire:387") 
    #  # Afficher l'image 2 dans la deuxième colonne
    # with col3:
    #      st.write("Enseignants en primaire:387")
    st.markdown("<h1 style='text-align: center; color: blue;'>Deuxième évaluation TEACHECE</h1>", unsafe_allow_html=True)
######################
    #col1, _, col2, _, col3 = st.columns([1, 1.2, 1, 1.2, 1])
    col1, col2,col3 = st.columns([1, 1, 1])
    # Afficher le nombre d'enseignants au collège dans la première colonne
    with col1:
        st.markdown("<span style='font-size:24px; color:blue;'>Enseignants en préscolaire:</span> <span style='font-size:24px;'>82</span>", unsafe_allow_html=True)
    
    # Afficher le nombre d'enseignants en préscolaire dans la deuxième colonne
    with col2:
        st.markdown("<span style='font-size:24px; color:green;'>Enseignants en primaire:</span> <span style='font-size:24px;'>387</span>", unsafe_allow_html=True)
    
    # Afficher le nombre d'enseignants en primaire dans la troisième colonne
    with col3:
        st.markdown("<span style='font-size:24px; color:red;'>Enseignants au collège:</span> <span style='font-size:24px;'>199</span>", unsafe_allow_html=True)

###################

    #st.markdown("<h1 style='text-align: center; color: blue;'>Deuxième évaluation TEACHECE</h1>", unsafe_allow_html=True)

#st.markdown("<h3 style='text-align: center; color: orange;'>Cette API analyse les conversations des membres Quosh & United Boss sur WathsApp</h3>", unsafe_allow_html=True)
    st.info("suivie de l'evolution des soumissions des formulaires de l'évaluation")
#st.markdown('''
#Cette API analyse les conversations des membres Quosh & United Boss sur WathsApp
#* **libraries utilisés:** Streamlit, Pandas,numpy,matplotlib,seaborn
#* **Data Source:** Kaggle
#''')

 # Options de navigation pour les pages
    selected_page = st.sidebar.selectbox("Sélectionner un formulaire", 
                                      ["Teach primaire et college", "Teach préscolaire"])
    # Affichage de la page sélectionnée
    if selected_page == "Teach primaire et college":
        page_une()
    elif selected_page == "Teach préscolaire":
        page_deux()
def page_une():
   # st.header("Teach primaire et college")
    # Fonction pour récupérer les données des soumissions par agent
    vect_section_une=["Données globale", "Par région","Par niveau",
                      "Par CP & région","Par CP"]  
    # Options de navigation pour les sections de la page
    selected_section = st.sidebar.radio("Sélectionner une section",vect_section_une)
                                        

    # Affichage de la section sélectionnée
    if selected_section ==vect_section_une[0]:
        section_une_a()
    elif selected_section ==vect_section_une[1]:
        section_une_b()
    elif selected_section ==vect_section_une[2]:
         section_une_c() 
    elif selected_section ==vect_section_une[3]:
         section_une_d()
    elif selected_section ==vect_section_une[4]:
         section_une_e() 
def section_une_a():
  
    col1, col2, col3 = st.columns([1, 3, 1])
    
    # Créer un espace vide à gauche et à droite du graphique
    left_placeholder = col2.empty()
    right_placeholder = col2.empty()
    
    # Afficher le graphique entre les espaces vides
    with left_placeholder:
        # Espace vide à gauche du graphique
        st.write(" ")  # Espace vide pour ajuster la position
    
    # Afficher le nombre de formulaires soumis au milieu du graphique
    with col2:
        st.write(f"<div style='border: 1px solid black; padding: 10px; background-color: lightblue;'><span style='font-size: 20px; color: blue;'>Soumission pour le primaire & collège: {nombre_formulaires_soumis}</span></div>", unsafe_allow_html=True)
       # Ajouter un espace
        st.write("<br>", unsafe_allow_html=True)
    # Afficher la barre de progression au milieu du graphique
    with col2:
        # Créer un espace vide
        
        # Afficher la barre de progression en pourcentage
        st.write(f"<div style='width: 100px;'>{pourcentage_soumissions*100:.2f} %</div>", unsafe_allow_html=True)
       # st.write(f" {pourcentage_soumissions:.2f} %",width=100)
        progress_bar = st.progress(pourcentage_soumissions)
        # Afficher la valeur de progression sur la barre de progression
       # progress_bar.text(f"{pourcentage_soumissions:.2f}%")
        
    # Afficher le graphique entre les espaces vides
    with right_placeholder:
        # Espace vide à droite du graphique
        st.write(" ")  # Espace vide pour ajuster la position
    
    # Afficher le graphique dans la deuxième colonne
    with col2:
        st.pyplot(get_soumission_par_niveau(df_prim_col), width=800, height=600)
    
           # progress_bar.text(f"{pourcentage_soumissions:.2f}%")

def section_une_b():
    st.subheader("")
    # Sélectionner la région
    selected_region = st.selectbox("Choisir une région", vect_region)
    
    if selected_region:
        # Filtrer les données en fonction de la région sélectionnée
        #df_region = df_prim_col[df_prim_col['Region'] == selected_region]
        
        # Afficher le graphique en fonction de la région sélectionnée
        st.pyplot(graphique_soumissions_par_region_et_par_niveau(selected_region, df_prim_col))
   
def section_une_c():
    st.subheader("")
    # Sélectionner la région
    selected_niveau = st.sidebar.selectbox("Choisir un niveau", vect_niveau)
    
    if selected_niveau:
        # Filtrer les données en fonction de la région sélectionnée
        #df_region = df_prim_col[df_prim_col['Region'] == selected_region]
        
        # Afficher le graphique en fonction de la région sélectionnée
        st.pyplot(graphique_soumissions_par_niveau_reg(selected_niveau, df_prim_col))
def section_une_d():
    st.subheader("Formulaire soumis par les CP par niveau")
    selected_region = st.sidebar.selectbox("Choisir une région", vect_region)
    Niveau=["collège","primaire"]
    if selected_region:
        selected_niv = st.selectbox("Choisir un niveau:",Niveau )
        if selected_niv==Niveau[0]:
        # Afficher le graphique en fonction de la région sélectionnée
            st.pyplot(graphique_soumissions_par_region_et_par_CP(selected_region,df_col))
        elif selected_niv==Niveau[1]:
       # Afficher le graphique en fonction de la région sélectionnée
           st.pyplot(graphique_soumissions_par_region_et_par_CP(selected_region,df_prim))
def section_une_e():
    st.subheader("Formualire soumis par conseiller")
    selected_CP= st.sidebar.selectbox("Choisir une CP",liste_CP)
    
    if selected_CP:
        # Afficher le graphique en fonction de la région sélectionnée
        st.write(get_formulaire_par_CP(selected_CP, df_prim_col))         
def page_deux():
    st.header("")

    vect_section_deux=["Par région", "Par CP & région","Par CP"]  
    # Options de navigation pour les sections de la page
    selected_section = st.sidebar.radio("Sélectionner une section",vect_section_deux)
                                        

    # Affichage de la section sélectionnée
    if selected_section ==vect_section_deux[0]:
        section_deux_a()
    elif selected_section ==vect_section_deux[1]:
        section_deux_b()
    elif selected_section ==vect_section_deux[2]:
         section_deux_c() 

def section_deux_a():
  
    col1, col2, col3 = st.columns([1, 3, 1])
    
    # Créer un espace vide à gauche et à droite du graphique
    left_placeholder = col2.empty()
    right_placeholder = col2.empty()
    
    # Afficher le graphique entre les espaces vides
    with left_placeholder:
        # Espace vide à gauche du graphique
        st.write(" ")  # Espace vide pour ajuster la position
    
    # Afficher le nombre de formulaires soumis au milieu du graphique
    with col2:
        st.write(f"<div style='border: 1px solid black; padding: 10px; background-color: lightblue;'><span style='font-size: 20px; color: blue;'>Soumission pour le préscolaire : {nombre_formulaires_soumis_pres}</span></div>", unsafe_allow_html=True)
       # Ajouter un espace
        st.write("<br>", unsafe_allow_html=True)
    # Afficher la barre de progression au milieu du graphique
    with col2:
        # Créer un espace vide
        
        # Afficher la barre de progression en pourcentage
        st.write(f"<div style='width: 100px;'>{pourcentage_soumissions_pres*100:.2f} %</div>", unsafe_allow_html=True)
       # st.write(f" {pourcentage_soumissions:.2f} %",width=100)
        progress_bar = st.progress(pourcentage_soumissions_pres)
        # Afficher la valeur de progression sur la barre de progression
       # progress_bar.text(f"{pourcentage_soumissions:.2f}%")
        
    # Afficher le graphique entre les espaces vides
    with right_placeholder:
        # Espace vide à droite du graphique
        st.write(" ")  # Espace vide pour ajuster la position
    
    # Afficher le graphique dans la deuxième colonne
    with col2:
        st.pyplot(get_soumission_par_region(df_presc), width=800, height=600)
    
           # progress_bar.text(f"{pourcentage_soumissions:.2f}%")


def section_deux_b():
    st.subheader("")
    selected_region = st.sidebar.selectbox("Choisir une région", vect_region)
    Niveau=["collège","primaire"]
    if selected_region:

       # Afficher le graphique en fonction de la région sélectionnée
           st.pyplot(graphique_soumissions_par_region_et_par_CP(selected_region,df_presc))
def section_deux_c():
    st.subheader("Formualire soumis par conseiller")
    selected_CP_pres= st.sidebar.selectbox("Choisir une CP",liste_CP_presc)
    
    if selected_CP_pres:
        # Afficher le graphique en fonction de la région sélectionnée
        st.write(get_formulaire_par_CP(selected_CP_pres, df_presc))  
        
if __name__ == "__main__":
        main()