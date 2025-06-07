"""Samuel Drake. Ce program permet à l'utilisateur de manipuler une liste d'objets sous forme de jeux vidéos. 
Chaque jeu est composé de 5 propriétés: Nom, année, genre(s), developpeur(s), langue(s) disponible(s)."""

import tkinter as tk
from tkinter import messagebox
import tkstylesheet as tks
import fenetres_secondaires as wc
    
def on_closing(): # Fonction pour prévenir la fermeture de la fenêtre avec le X
    messagebox.showinfo("Info", "Utilisez les boutons pour fermer la fernêtre!")
        
def main_menu():
    
    def window_commands(fonction_destination):
        if len(wc.return_obj_lst()) == 0: # Empêcher à l'utilisateur de modifier les propriétés des objets s'il y a aucun objet
            messagebox.showerror("Choix Invalide", "Créer un jeu avant d'utiliser cette fonction")
        else:
            main_menu.destroy()
            fonction_destination()
    
    main_menu = tk.Toplevel()
    main_menu.title("Menu Principal")
    tks.style_window(main_menu, 400, 500)
    main_menu.columnconfigure(0, weight=1)

    logo_photo = tk.PhotoImage(file="logo.gif")
    logo_label = tks.create_label(main_menu, image=logo_photo)
    main_menu.logo_photo = logo_photo # Garder une référence de l'image pour pas qu'elle continue d'apparaitre
    logo_label.grid(row=0, column=0, padx=20, pady=(10,0))
    
    introduction_label = tks.create_label(main_menu, text="Bienvenu au manipulateur de jeux!\nVeuillez selectionner une option:")
    introduction_label.grid(row=1, column=0, padx=20, pady=(0,20), sticky="ew")

    creer_obj_btn = tks.create_button(main_menu, text="Créer/Supprimer des jeux", command=lambda: [wc.creer_obj(), main_menu.destroy()])
    creer_obj_btn.grid(row=2, column=0, padx=20, pady=(0,10), sticky="ew")

    ouvrir_prop_obj_btn = tks.create_button(main_menu, text="Ouvrir/Modifier les propriétés de jeux", command=lambda: window_commands(wc.choisir_obj))
    ouvrir_prop_obj_btn.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    quitter_btn = tks.create_button(main_menu, text="Quitter", command=exit)
    quitter_btn.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
    
    main_menu.protocol("WM_DELETE_WINDOW", on_closing) # Lorsque l'utilisateur appui sur le x rouge, ceci exécute la fonction on_closing
    
root = tk.Tk()
root.withdraw() # Cacher la fenêtre root
main_menu()
root.mainloop()