import tkinter as tk
import window_commands as wc
from time import sleep

################## Propriété 'nom' ##################

def name(object):
    
    def verification():
        nom = name_edit_entry.get()
        object.strnom = nom
        response_label.config(text=f"Nom actuel: {object.strnom}")
        name_edit_window.title(f"Edit name of {object.strnom}")

    def retour_au_menu():
        name_edit_window.destroy()
        wc.property_modification(object)
        
    name_edit_window = tk.Tk()
    name_edit_window.title(f"Edit name of {object.strnom}")
    name_edit_window.geometry("300x300")

    name_edit_label = tk.Label(name_edit_window)
    name_edit_label.config(text="Nom de l'objet")
    name_edit_label.pack()
    
    name_edit_entry = tk.Entry(name_edit_window)
    name_edit_entry.pack()
    
    name_edit_button = tk.Button(name_edit_window)
    name_edit_button.config(text="Soumettre", command=verification)
    name_edit_button.pack()
    
    response_label = tk.Label(name_edit_window)
    response_label.config(text=f"Nom actuel: {object.strnom}")
    response_label.pack()

    menu_button = tk.Button(name_edit_window)
    menu_button.config(text="Retour au menu", command=retour_au_menu)
    menu_button.pack()
    
    name_edit_window.mainloop()


################## Propriété 'année' ##################

def year(object):

    def verification():
        annee = create_entry.get()
        object.intannee = annee
        response_label.config(text=f"Année de sortie actuelle: {object.intannee}")

    def retour_au_menu():
        year_edit_window.destroy()
        wc.property_modification(object)
        
    year_edit_window = tk.Tk()
    year_edit_window.title(f"Edit year of {object.strnom}")
    year_edit_window.geometry("300x300")

    create_label = tk.Label(year_edit_window)
    create_label.config(text="Année: ")
    create_label.pack()
    
    create_entry = tk.Entry(year_edit_window)
    create_entry.pack()
    
    create_button = tk.Button(year_edit_window)
    create_button.config(text="Soumettre", command=verification)
    create_button.pack()
    
    response_label = tk.Label(year_edit_window)
    response_label.config(text=f"Année de sortie actuelle: {object.intannee}")
    response_label.pack()

    menu_button = tk.Button(year_edit_window)
    menu_button.config(text="Retour au menu", command=retour_au_menu)
    menu_button.pack()
    
    year_edit_window.mainloop()


################## Propriété 'genres' ##################

def genres(object):

    def ajouter():
        genre = entry.get()
        if genre in object.lstgenre:
            response_label.config(text=f"Genre déja dans la liste")
        else:
            object.ajout_objet_genre(genre)
            response_label.config(text=f"Genre ajouté dans la liste")
            current_properties_label.config(text=f"Genres actuels: {object.lstgenre}")
    
    def supprimer():
        genre = entry.get()
        if genre in object.lstgenre:
            response_label.config(text=f"Genre supprimé")
            object.supp_objet_genre(genre)
            current_properties_label.config(text=f"Genres actuels: {object.lstgenre}")
            
        else:
            response_label.config(text=f"Genre pas dans la liste, peut pas être supprimé")
    
    def retour_au_menu():
        genres_edit_window.destroy()
        wc.property_modification(object)

    genres_edit_window = tk.Tk()
    genres_edit_window.title(f"Edit genres of {object.strnom}")
    genres_edit_window.geometry("300x300")

    entry = tk.Entry(genres_edit_window)
    entry.pack()
    
    ajouter_button = tk.Button(genres_edit_window)
    ajouter_button.config(text="Ajouter", command=ajouter)
    ajouter_button.pack()
    
    supprimer_button = tk.Button(genres_edit_window)
    supprimer_button.config(text="Supprimer", command=supprimer)
    supprimer_button.pack()
    
    current_properties_label = tk.Label(genres_edit_window)
    current_properties_label.config(text=f"Genres actuels: {object.lstgenre}")
    current_properties_label.pack()

    
    response_label = tk.Label(genres_edit_window)
    response_label.pack()

    menu_button = tk.Button(genres_edit_window)
    menu_button.config(text="Retour au menu", command=retour_au_menu)
    menu_button.pack()
    
    genres_edit_window.mainloop()


################## Propriété 'developpeurs' ##################

def devs(object):

    def ajouter():
        dev = entry.get()
        if dev in object.lstdeveloppeur:
            response_label.config(text=f"Dev déja dans la liste")
        else:
            object.ajout_objet_dev(dev)
            response_label.config(text=f"Dev ajouté dans la liste")
            current_properties_label.config(text=f"Devs actuels: {object.lstdeveloppeur}")
    
    def supprimer():
        dev = entry.get()
        if dev in object.lstdeveloppeur:
            response_label.config(text=f"dev supprimé")
            object.supp_objet_dev(dev)
            current_properties_label.config(text=f"devs actuels: {object.lstdeveloppeur}")
            
        else:
            response_label.config(text=f"dev pas dans la liste, peut pas être supprimé")
    
    def retour_au_menu():
        genres_edit_window.destroy()
        wc.property_modification(object)

    genres_edit_window = tk.Tk()
    genres_edit_window.title(f"Edit devs of {object.strnom}")
    genres_edit_window.geometry("300x300")

    entry = tk.Entry(genres_edit_window)
    entry.pack()
    
    ajouter_button = tk.Button(genres_edit_window)
    ajouter_button.config(text="Ajouter", command=ajouter)
    ajouter_button.pack()
    
    supprimer_button = tk.Button(genres_edit_window)
    supprimer_button.config(text="Supprimer", command=supprimer)
    supprimer_button.pack()
    
    current_properties_label = tk.Label(genres_edit_window)
    current_properties_label.config(text=f"devs actuels: {object.lstdeveloppeur}")
    current_properties_label.pack()

    
    response_label = tk.Label(genres_edit_window)
    response_label.pack()

    menu_button = tk.Button(genres_edit_window)
    menu_button.config(text="Retour au menu", command=retour_au_menu)
    menu_button.pack()
    
    genres_edit_window.mainloop()

################## Propriété 'langues' ##################

def languages(object):

    def ajouter():
        langue = entry.get()
        if langue in object.lstlangue:
            response_label.config(text=f"langue déja dans la liste")
        else:
            object.ajout_objet_langue(langue)
            response_label.config(text=f"langue ajouté dans la liste")
            current_properties_label.config(text=f"langues actuels: {object.lstlangue}")
    
    def supprimer():
        langue = entry.get()
        if langue in object.lstlangue:
            response_label.config(text=f"langue supprimé")
            object.supp_objet_langue(langue)
            current_properties_label.config(text=f"langues actuels: {object.lstlangue}")
            
        else:
            response_label.config(text=f"langue pas dans la liste, peut pas être supprimé")
    
    def retour_au_menu():
        genres_edit_window.destroy()
        wc.property_modification(object)

    genres_edit_window = tk.Tk()
    genres_edit_window.title(f"Edit langues of {object.strnom}")
    genres_edit_window.geometry("300x300")

    entry = tk.Entry(genres_edit_window)
    entry.pack()
    
    ajouter_button = tk.Button(genres_edit_window)
    ajouter_button.config(text="Ajouter", command=ajouter)
    ajouter_button.pack()
    
    supprimer_button = tk.Button(genres_edit_window)
    supprimer_button.config(text="Supprimer", command=supprimer)
    supprimer_button.pack()
    
    current_properties_label = tk.Label(genres_edit_window)
    current_properties_label.config(text=f"langues actuels: {object.lstlangue}")
    current_properties_label.pack()

    
    response_label = tk.Label(genres_edit_window)
    response_label.pack()

    menu_button = tk.Button(genres_edit_window)
    menu_button.config(text="Retour au menu", command=retour_au_menu)
    menu_button.pack()
    
    genres_edit_window.mainloop()