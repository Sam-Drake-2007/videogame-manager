import tkinter as tk
from tkinter import messagebox
from class_jeu import jeu
import properties as p

obj_lst = []


################## Option Créer ##################

def creer_obj():
    
    def verification():
        
        strnom = nom_entry.get()
        if strnom in [obj.strnom for obj in obj_lst]:
            messagebox.showerror("Réponse Invalide", "Cet objet existe déja!")
            nom_entry.delete(0, tk.END)
        else:
            obj_lst.append(jeu(strnom))
            obj_lst_label.config(text=f"Objets: {[obj.strnom for obj in obj_lst]}")
            nom_entry.delete(0, tk.END)
    
    def retour_au_menu():
        fen_creer_obj.destroy()
        
    fen_creer_obj = tk.Tk()
    fen_creer_obj.title("Créer des objets")
    fen_creer_obj.geometry("300x300")
    
    commande_label = tk.Label(fen_creer_obj)
    commande_label.config(text="Entrer le nom de l'objet")
    commande_label.pack()
    
    obj_lst_label = tk.Label(fen_creer_obj)
    obj_lst_label.config(text=f"Objets: {[obj.strnom for obj in obj_lst]}")
    obj_lst_label.pack()
    
    nom_entry = tk.Entry(fen_creer_obj)
    nom_entry.pack()
    
    soumettre_btn = tk.Button(fen_creer_obj)
    soumettre_btn.config(text="Soumettre", command=verification)
    soumettre_btn.pack()
    
    menu_btn = tk.Button(fen_creer_obj)
    menu_btn.config(text="Retour au menu", command=retour_au_menu)
    menu_btn.pack()
    
    fen_creer_obj.mainloop()


################## Option Ouvrir ##################

def choisir_obj():

    def open_properties(object):
        pick_obj_window.destroy()
        property_modification(object)
    
    def retour_au_menu():
        pick_obj_window.destroy()
    
    pick_obj_window = tk.Tk()
    pick_obj_window.title("Choisir un objet")
    pick_obj_window.geometry("300x300")
    
    modify_label = tk.Label(pick_obj_window)
    modify_label.config(text="Indiquer l'objet et la pripriété à modifier")
    modify_label.grid(row=0, column=0)
    
    for i in range(len(obj_lst)):
        obj_label = tk.Button(pick_obj_window)
        obj_label.config(text=obj_lst[i].strnom, command=lambda: open_properties(obj_lst[i]))
        obj_label.grid(row=i+1, column=0)
    
    menu_button = tk.Button(pick_obj_window)
    menu_button.config(text="Retour au menu", command=retour_au_menu)
    menu_button.grid(row=i+2, column=0)   
    
    pick_obj_window.mainloop()


def property_modification(object):
    
    def retour_au_menu():
        property_window.destroy()
        
    property_window = tk.Tk()
    property_window.title(f"Propriétés de '{object.strnom}'")
    property_window.geometry("300x300")
    
    intro_label = tk.Label(property_window)
    intro_label.config(text="Appuyer sur une propriété pour la modifier")
    intro_label.grid(row=0, column=0)
    
    prop_nom_button = tk.Button(property_window)
    prop_nom_button.config(text=f"Nom: {object.strnom}", borderwidth=0, command=lambda: [property_window.destroy(), p.name(object)])
    prop_nom_button.grid(row=1, column=0)

    prop_annee_button = tk.Button(property_window)
    prop_annee_button.config(text=f"Année de sortie: {object.intannee}", borderwidth=0, command=lambda: [property_window.destroy(), p.year(object)])
    prop_annee_button.grid(row=2, column=0)

    prop_genres_button = tk.Button(property_window)
    prop_genres_button.config(text=f"Genres: {object.lstgenre}", borderwidth=0, command=lambda: [property_window.destroy(), p.genres(object)])
    prop_genres_button.grid(row=3, column=0)

    prop_devs_button = tk.Button(property_window)
    prop_devs_button.config(text=f"Developpeurs: {object.lstdeveloppeur}", borderwidth=0, command=lambda: [property_window.destroy(), p.devs(object)])
    prop_devs_button.grid(row=4, column=0)

    prop_langues_button = tk.Button(property_window)
    prop_langues_button.config(text=f"Langues disponibles: {object.lstlangue}", borderwidth=0, command=lambda: [property_window.destroy(), p.languages(object)])
    prop_langues_button.grid(row=5, column=0)

    menu_button = tk.Button(property_window)
    menu_button.config(text="Retour au menu", command=retour_au_menu)
    menu_button.grid(row=6, column=0)  
    
    property_window.mainloop()


################## Option Supprimer ##################

def delete_obj():
    pass