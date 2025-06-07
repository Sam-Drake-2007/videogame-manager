"""Les propriétés qui peuvent êtres modifiés après avoir sélectionné une des options dans les fenêtres secondaires."""

import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import tkstylesheet as tks
import fenetres_secondaires as wc

def on_closing(entry_widget):
    messagebox.showinfo("Info", "Utilisez les boutons pour fermer la fernêtre!")
    entry_widget.focus_set()


################## Propriété 'nom' ##################

def name(obj):
    
    def verification():
        strnom = nom_entry.get().strip().lower()
        if strnom in [obj.strnom for obj in wc.return_obj_lst()]:
            messagebox.showerror("Réponse Invalide", "Ce jeu existe déja!")
        elif not strnom:
            messagebox.showwarning("Réponse Vide", "Veuillez entrer un nom.")
        else:
            obj.strnom = strnom
            response_label.config(text=f"Nom actuel: '{obj.strnom}'")
            fen_nom_prop.title(f"Modifier le nom du jeu '{obj.strnom}'")
        nom_entry.delete(0, tk.END)
        nom_entry.focus_set()
        
    fen_nom_prop = tk.Toplevel()
    fen_nom_prop.title(f"Modifier le nom du jeu '{obj.strnom}'")
    tks.style_window(fen_nom_prop, 400, 260)
    fen_nom_prop.columnconfigure(0, weight=1)
    
    instruction_label = tks.create_label(fen_nom_prop, text="Entrer le nouveau nom du jeu")
    instruction_label.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="ew")
    
    response_label = tks.create_label(fen_nom_prop, text=f"Nom actuel: '{obj.strnom}'")
    response_label.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="ew")
    
    nom_entry = tks.create_entry(fen_nom_prop)
    nom_entry.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew")
    nom_entry.focus_set()
    
    nom_edit_btn = tks.create_button(fen_nom_prop, text="Soumettre", command=verification)
    nom_edit_btn.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")

    separator = ttk.Separator(fen_nom_prop, orient="horizontal")
    separator.grid(row=4, column=0, padx=20, pady=(0, 10), sticky="ew")
    
    menu_button = tks.create_button(fen_nom_prop, text="Retour au menu", command=lambda: [fen_nom_prop.destroy(), wc.modification_props(obj)])
    menu_button.grid(row=5, column=0, pady=(0, 20), padx=20, sticky="ew")
    
    fen_nom_prop.protocol("WM_DELETE_WINDOW", lambda: on_closing(nom_entry))
    

################## Propriété 'année' ##################

def year(obj):

    def verification():
        strannee = annee_label.get().strip()
        try:
            intannee = int(strannee)
            if intannee >= 1958 and intannee <= 2025: # Le premier jeu vidéo à été créé en 1958
                obj.intannee = intannee
                annee_sortie_label.config(text=f"Année de sortie actuelle: '{obj.intannee}'")
            else:
                messagebox.showerror("Année Invalide", "Entrer une année entre 1958 et 2025!")
        except:
            messagebox.showerror("Année Invalide", "Entrer une année en chiffres!")
        annee_label.delete(0, tk.END)
        annee_label.focus_set()
        
    fen_annee = tk.Toplevel()
    fen_annee.title(f"Modifier l'année de sortie du jeu '{obj.strnom}'")
    tks.style_window(fen_annee, 400, 260)
    fen_annee.columnconfigure(0, weight=1)
    
    instruc_label = tks.create_label(fen_annee, text="Entrer l'année de sortie")
    instruc_label.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="ew")

    annee_sortie_label = tks.create_label(fen_annee, text=f"Année de sortie actuelle: {obj.intannee}")
    annee_sortie_label.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="ew")
    
    annee_label = tks.create_entry(fen_annee)
    annee_label.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew")
    annee_label.focus_set()
    
    soumettre_btn = tks.create_button(fen_annee, text="Soumettre", command=verification)
    soumettre_btn.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")

    separator = ttk.Separator(fen_annee, orient="horizontal")
    separator.grid(row=4, column=0, padx=20, pady=(0, 10), sticky="ew")
    
    menu_btn = tks.create_button(fen_annee, text="Retour au menu", command=lambda: [fen_annee.destroy(), wc.modification_props(obj)])
    menu_btn.grid(row=5, column=0, pady=(0, 20), padx=20, sticky="ew")
    
    fen_annee.protocol("WM_DELETE_WINDOW", lambda: on_closing(annee_label))
    

################## Propriété 'genres' ##################

def genres(obj):

    def ajouter():
        strgenre = genre_entry.get().strip().lower()
        if strgenre in obj.lstgenre:
            messagebox.showerror("Genre Invalide", "Genre déja dans la liste.")
        elif not strgenre:
            messagebox.showwarning("Réponse Vide", "Veuillez entrer un genre.")
        else:
            obj.ajout_objet_genre(strgenre)
            genres_label.config(text=f"Genres actuels: {obj.lstgenre}")
            fen_genre.update_idletasks()
            fen_genre.minsize(fen_genre.winfo_reqwidth(), fen_genre.winfo_reqheight())
        genre_entry.delete(0, tk.END)
        genre_entry.focus_set()
    
    def supprimer():
        strgenre = genre_entry.get().strip().lower()
        if len (strgenre) > 0 and strgenre in obj.lstgenre:
            obj.supp_objet_genre(strgenre)
            genres_label.config(text=f"Genres actuels: {obj.lstgenre}")
            fen_genre.update_idletasks()
            fen_genre.minsize(fen_genre.winfo_reqwidth(), fen_genre.winfo_reqheight())   
        elif not strgenre:
            messagebox.showwarning("Réponse vide", "Veuillez entrer un genre.")
        else:
            messagebox.showerror("Genre Invalide", "Genre pas dans la liste.")  
        genre_entry.delete(0, tk.END)
        genre_entry.focus_set()

    fen_genre = tk.Toplevel()
    fen_genre.title(f"Modifier les genres du jeu '{obj.strnom}'")
    tks.style_window(fen_genre, 400, 300)
    fen_genre.columnconfigure(0, weight=1)

    instruction_label = tks.create_label(fen_genre, text="Entrer un genre à ajouter ou supprimer")
    instruction_label.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="ew")

    genres_label = tks.create_label(fen_genre, text=f"Genres actuels: {obj.lstgenre}", wraplength=320)
    genres_label.grid(row=1, column=0, pady=(0, 15), padx=20, sticky="ew")
    
    genre_entry = tks.create_entry(fen_genre)
    genre_entry.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew")
    genre_entry.focus_set()
    
    ajouter_btn = tks.create_button(fen_genre, text="Ajouter", command=ajouter)
    ajouter_btn.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")
    
    supprimer_btn = tks.create_button(fen_genre, text="Supprimer", command=supprimer)
    supprimer_btn.grid(row=4, column=0, pady=(0, 10), padx=20, sticky="ew")

    separator = ttk.Separator(fen_genre, orient="horizontal")
    separator.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

    menu_btn = tks.create_button(fen_genre, text="Retour au menu", command=lambda: [fen_genre.destroy(), wc.modification_props(obj)])
    menu_btn.grid(row=6, column=0, pady=(0, 20), padx=20, sticky="ew")

    fen_genre.protocol("WM_DELETE_WINDOW", lambda: on_closing(genre_entry))
    fen_genre.update_idletasks()
    fen_genre.minsize(fen_genre.winfo_reqwidth(), fen_genre.winfo_reqheight())
    

################## Propriété 'developpeurs' ##################

def devs(obj):

    def ajouter():
        strdev = devs_entry.get().strip().lower()
        if strdev in obj.lstdeveloppeur:
            messagebox.showerror("Développeur Invalide", "Développeur déjà dans la liste.")
        elif not strdev:
            messagebox.showwarning("Réponse Vide", "Veuillez entrer un nom.")
        else:
            obj.ajout_objet_dev(strdev)
            devs_label.config(text=f"Développeurs actuels: {obj.lstdeveloppeur}")
            fen_devs.update_idletasks()
            fen_devs.minsize(fen_devs.winfo_reqwidth(), fen_devs.winfo_reqheight())
        devs_entry.delete(0, tk.END)
        devs_entry.focus_set()

    def supprimer():
        dev = devs_entry.get().strip().lower()
        if len(dev) > 0 and dev in obj.lstdeveloppeur:
            obj.supp_objet_dev(dev)
            devs_label.config(text=f"Développeurs actuels: {obj.lstdeveloppeur}")
            fen_devs.update_idletasks()
            fen_devs.minsize(fen_devs.winfo_reqwidth(), fen_devs.winfo_reqheight())   
        elif not dev:
            messagebox.showwarning("Réponse Vide", "Veuillez entrer un développeur.")
        else:
            messagebox.showerror("Développeur Invalide", "Développeur pas dans la liste.")
        devs_entry.delete(0, tk.END)
        devs_entry.focus_set()

    fen_devs = tk.Toplevel()
    fen_devs.title(f"Modifier les developpeurs du jeu '{obj.strnom}'")
    tks.style_window(fen_devs, 400, 300)
    fen_devs.columnconfigure(0, weight=1)

    instruction_label = tks.create_label(fen_devs, text="Entrer un développeur à ajouter ou supprimer")
    instruction_label.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="ew")

    devs_label = tks.create_label(fen_devs, text=f"Développeurs actuels: {obj.lstdeveloppeur}", wraplength=320)
    devs_label.grid(row=1, column=0, pady=(0, 15), padx=20, sticky="ew")
    
    devs_entry = tks.create_entry(fen_devs)
    devs_entry.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew")
    devs_entry.focus_set()
    
    ajouter_btn = tks.create_button(fen_devs, text="Ajouter", command=ajouter)
    ajouter_btn.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")
    
    supprimer_btn = tks.create_button(fen_devs, text="Supprimer", command=supprimer)
    supprimer_btn.grid(row=4, column=0, pady=(0, 10), padx=20, sticky="ew")

    separator = ttk.Separator(fen_devs, orient="horizontal")
    separator.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

    menu_btn = tks.create_button(fen_devs, text="Retour au menu", command=lambda: [fen_devs.destroy(), wc.modification_props(obj)])
    menu_btn.grid(row=6, column=0, pady=(0, 20), padx=20, sticky="ew")

    fen_devs.protocol("WM_DELETE_WINDOW", lambda: on_closing(devs_entry))
    fen_devs.update_idletasks()
    fen_devs.minsize(fen_devs.winfo_reqwidth(), fen_devs.winfo_reqheight())
    
    
################## Propriété 'langues' ##################

def languages(obj):

    def ajouter():
        strlangue = langues_entry.get().strip().lower()
        if strlangue in obj.lstlangue:
            messagebox.showerror("Langue Invalide", "Langue déjà dans la liste.")
        elif not strlangue:
            messagebox.showwarning("Réponse Vide", "Veuillez entrer une langue.")
        else:
            obj.ajout_objet_langue(strlangue)
            langues_label.config(text=f"Langues actuelles: {obj.lstlangue}")
            fen_langues.update_idletasks()
            fen_langues.minsize(fen_langues.winfo_reqwidth(), fen_langues.winfo_reqheight())
        langues_entry.delete(0, tk.END)
        langues_entry.focus_set()

    def supprimer():
        strlangue = langues_entry.get().strip().lower()
        if len(strlangue) > 0 and strlangue in obj.lstlangue:
            obj.supp_objet_langue(strlangue)
            langues_label.config(text=f"Langues actuelles: {obj.lstlangue}")
            fen_langues.update_idletasks()
            fen_langues.minsize(fen_langues.winfo_reqwidth(), fen_langues.winfo_reqheight())   
        elif not strlangue:
            messagebox.showwarning("Réponse Vide", "Veuillez entrer une langue.")
        else:
            messagebox.showerror("Langue Invalide", "Langue pas dans la liste")
        langues_entry.delete(0, tk.END)
        langues_entry.focus_set()

    fen_langues = tk.Toplevel()
    fen_langues.title(f"Modifier les langues disponibles du jeu '{obj.strnom}'")
    tks.style_window(fen_langues, 400, 300)
    fen_langues.columnconfigure(0, weight=1)

    instruction_label = tks.create_label(fen_langues, text="Entrer une langue à ajouter ou supprimer")
    instruction_label.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="ew")

    langues_label = tks.create_label(fen_langues, text=f"Langues actuelles: {obj.lstlangue}", wraplength=320)
    langues_label.grid(row=1, column=0, pady=(0, 15), padx=20, sticky="ew")
    
    langues_entry = tks.create_entry(fen_langues)
    langues_entry.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew")
    langues_entry.focus_set()
    
    ajouter_btn = tks.create_button(fen_langues, text="Ajouter", command=ajouter)
    ajouter_btn.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")
    
    supprimer_btn = tks.create_button(fen_langues, text="Supprimer", command=supprimer)
    supprimer_btn.grid(row=4, column=0, pady=(0, 10), padx=20, sticky="ew")

    separator = ttk.Separator(fen_langues, orient="horizontal")
    separator.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

    menu_btn = tks.create_button(fen_langues, text="Retour au menu", command=lambda: [fen_langues.destroy(), wc.modification_props(obj)])
    menu_btn.grid(row=6, column=0, pady=(0, 20), padx=20, sticky="ew")

    fen_langues.protocol("WM_DELETE_WINDOW", lambda: on_closing(langues_entry))
    fen_langues.update_idletasks()
    fen_langues.minsize(fen_langues.winfo_reqwidth(), fen_langues.winfo_reqheight())