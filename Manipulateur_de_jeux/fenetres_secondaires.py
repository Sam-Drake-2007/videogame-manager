"""Ceci sont les fenêtres secondaires qui s'ouvrent lorsqu'on appui sur un des boutons du menu principal."""

import tkinter as tk
from tkinter import messagebox
import tkstylesheet as tks
import tkinter.ttk as ttk
from class_jeu import Jeu
import properties as p


obj_lst = []
def return_obj_lst(): # Transférer la liste à d'autres modules
    return obj_lst

def on_closing(entry_widget):
    messagebox.showinfo("Info", "Utilisez les boutons pour fermer la fernêtre!")
    entry_widget.focus_set()


################## Option Créer/Supprimer ##################

def creer_obj():
    
    def update_obj_lst_label():
        obj_lst_label.config(text=f"Jeux: {[obj.strnom for obj in obj_lst]}")
        fen_creer_obj.update_idletasks() # Ceci et la ligne qui suit sont pour changer les dimentions de la fenêtre pour que tout les widgets y rentrent. Les dimentions dans la ligne 58 sont juste par défaut.
        fen_creer_obj.minsize(fen_creer_obj.winfo_reqwidth(), fen_creer_obj.winfo_reqheight())
        
    def verification_creer():
        strnom = nom_entry.get().strip().lower()
        if strnom in [obj.strnom for obj in obj_lst]:
            messagebox.showerror("Réponse Invalide", "Ce jeu existe déja!")
        elif not strnom:
            messagebox.showwarning("Réponse Vide", "Veuillez entrer un nom.")
        else:
            obj_lst.append(Jeu(strnom))
            update_obj_lst_label()
        nom_entry.delete(0, tk.END) # Effacer le texte du entry et mettre focus dessu
        nom_entry.focus_set()
            
    def verification_supp():
        strnom = nom_entry.get().strip().lower()
        if len (strnom) > 0 and strnom not in [obj.strnom for obj in obj_lst]:
            messagebox.showerror("Réponse Invalide", "Ce jeu n'existe pas!")
        elif not strnom:
            messagebox.showwarning("Réponse Vide", "Veuillez entrer un nom.")
        else:
            obj_lst.pop([obj.strnom for obj in obj_lst].index(strnom))
            update_obj_lst_label()
        nom_entry.delete(0, tk.END)
        nom_entry.focus_set()
    
    def retour_au_menu():
        fen_creer_obj.destroy()
        from root import main_menu # Importer le menu principal ici pour éviter les 'circular imports'
        main_menu()
        
    fen_creer_obj = tk.Toplevel()
    fen_creer_obj.title("Créer des jeux")
    tks.style_window(fen_creer_obj, 400, 320)
    fen_creer_obj.columnconfigure(0, weight=1)
    fen_creer_obj.rowconfigure(1, weight=1)
    
    commande_label = tks.create_label(fen_creer_obj, text="Entrer le nom du jeu")
    commande_label.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="ew")

    obj_lst_label = tks.create_label(fen_creer_obj, text=f"Jeux: {[obj.strnom for obj in obj_lst]}", wraplength=320)
    obj_lst_label.grid(row=1, column=0, pady=(0, 15), padx=20, sticky="ew")
        
    nom_entry = tks.create_entry(fen_creer_obj)
    nom_entry.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew")
    nom_entry.focus_set()
        
    soumettre_btn = tks.create_button(fen_creer_obj, text="Créer", command=verification_creer)
    soumettre_btn.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")
    
    supp_btn = tks.create_button(fen_creer_obj, text="Supprimer", command=verification_supp)
    supp_btn.grid(row=4, column=0, sticky="ew", padx=20, pady=(0, 10))
    
    separator = ttk.Separator(fen_creer_obj, orient='horizontal')
    separator.grid(row=5, column=0, sticky="ew", padx=20, pady=(0, 10))

    menu_btn = tks.create_button(fen_creer_obj, text="Retour au menu", command=retour_au_menu)
    menu_btn.grid(row=6, column=0, pady=(0, 20), padx=20, sticky="ew")
    
    fen_creer_obj.protocol("WM_DELETE_WINDOW", lambda: on_closing(nom_entry))
    fen_creer_obj.after(10, update_obj_lst_label) # Reload les objets de la liste après 10 ms pour éviter que la fenêtre se ferme
    

################## Option Ouvrir/Modifier ##################

def choisir_obj():

    def ouvrir_propriétés(obj):
        fen_ouvrir_obj.destroy()
        modification_props(obj)
    
    def retour_au_menu():
        fen_ouvrir_obj.destroy()
        from root import main_menu
        main_menu()
    
    fen_ouvrir_obj = tk.Toplevel()
    fen_ouvrir_obj.title("Choisir un jeu")
    tks.style_window(fen_ouvrir_obj, 400, 200)
    fen_ouvrir_obj.columnconfigure(0, weight=1)
    
    commande_label = tks.create_label(fen_ouvrir_obj, text="Choisir le jeu que vous voulez modifier")
    commande_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
    
    for i in range(len(obj_lst)):
        obj_btn = tks.create_button(fen_ouvrir_obj, text=obj_lst[i].strnom, command=lambda obj=obj_lst[i]: ouvrir_propriétés(obj)) # Fonction lambda pour passer des paramètres à la commande du bouton
        obj_btn.grid(row=i+1, column=0, padx=20, pady=5, sticky="ew")
    
    separator = ttk.Separator(fen_ouvrir_obj, orient='horizontal')
    separator.grid(row=len(obj_lst)+1, column=0, padx=20, pady=(5, 10), sticky="ew")
    
    menu_btn = tks.create_button(fen_ouvrir_obj, text="Retour au menu", command=retour_au_menu)
    menu_btn.grid(row=len(obj_lst)+2, column=0, padx=20, pady=(0, 20), sticky="ew")
    
    fen_ouvrir_obj.protocol("WM_DELETE_WINDOW", on_closing)
    fen_ouvrir_obj.update_idletasks()
    fen_ouvrir_obj.minsize(fen_ouvrir_obj.winfo_reqwidth(), fen_ouvrir_obj.winfo_reqheight())
        

def modification_props(obj):
        
    fen_prop = tk.Toplevel()
    fen_prop.title(f"Propriétés de '{obj.strnom}'")
    tks.style_window(fen_prop, 400, 400)
    fen_prop.columnconfigure(0, weight=1)
    
    intro_label = tks.create_label(fen_prop, text="Appuyer sur une propriété pour la modifier")
    intro_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
    
    prop_nom_btn = tks.create_button(fen_prop, text=f"Nom: '{obj.strnom}'", borderwidth=0, command=lambda: [fen_prop.destroy(), p.name(obj)])
    prop_nom_btn.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

    prop_annee_btn = tks.create_button(fen_prop, text=f"Année de sortie: '{obj.intannee}'", borderwidth=0, command=lambda: [fen_prop.destroy(), p.year(obj)])
    prop_annee_btn.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

    prop_genres_btn = tks.create_button(fen_prop, text=f"Genres: {obj.lstgenre}", borderwidth=0, command=lambda: [fen_prop.destroy(), p.genres(obj)], wraplength=300)
    prop_genres_btn.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

    prop_devs_btn = tks.create_button(fen_prop, text=f"Developpeurs: {obj.lstdeveloppeur}", borderwidth=0, command=lambda: [fen_prop.destroy(), p.devs(obj)], wraplength=300)
    prop_devs_btn.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

    prop_langues_btn = tks.create_button(fen_prop, text=f"Langues disponibles: {obj.lstlangue}", borderwidth=0, command=lambda: [fen_prop.destroy(), p.languages(obj)], wraplength=300)
    prop_langues_btn.grid(row=5, column=0, padx=20, pady=5, sticky="ew")

    separator = ttk.Separator(fen_prop, orient='horizontal')
    separator.grid(row=6, column=0, padx=20, pady=(10, 10), sticky="ew")

    menu_btn = tks.create_button(fen_prop, text="Retour au menu", command=lambda: [fen_prop.destroy(), choisir_obj()])
    menu_btn.grid(row=7, column=0, padx=20, pady=(5, 20), sticky="ew")
    
    fen_prop.protocol("WM_DELETE_WINDOW", on_closing)
    fen_prop.update_idletasks()
    fen_prop.minsize(fen_prop.winfo_reqwidth(), fen_prop.winfo_reqheight())