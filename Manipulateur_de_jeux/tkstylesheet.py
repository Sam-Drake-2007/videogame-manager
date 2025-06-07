"""Ce module est utilisé pour appliquer du style constant à chaque élément de tkinter. 
J'ai essayer de créer quelque chose de similair au cascading style sheets (CSS) souvent utilisé avec HTML et JavaScript. 
En modificant les constantes de style, tout le document va changer en accordance avec le changement. 
Ceci est aussi utile pour économiser des lignes de code car on a pas besoin de configurer chaque élément."""

import tkinter as tk

# Constantes de style
COULEUR_FOND = "#2E3440"        
COULEUR_BOUTON = "#3B4252"       
COULEUR_BOUTON_ACTIF = "#434C5E"  
COULEUR_TEXTE = "#E5E9F0"        
COULEUR_ACCENT = "#88C0D0"       
COULEUR_ENTREE = "#4C566A"     
POLICE = ("Segoe UI", 12,)

def create_label(parent, text="", **kwargs): # kwargs permet à la fonction d'accepter d'autres paramètres si necessaire (par exemple dans le label du logo)
    """Fonction pour créer une label avec un style constant."""
    return tk.Label(
        parent,
        text=text,
        bg=COULEUR_FOND,
        fg=COULEUR_TEXTE,
        font=POLICE,
        **kwargs
    )

def create_button(parent, text="", command=None, **kwargs):
    """Fonction pour créer un bouton avec un style constant."""
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=POLICE,
        bg=COULEUR_BOUTON,
        fg=COULEUR_TEXTE,
        activebackground=COULEUR_BOUTON_ACTIF,
        activeforeground=COULEUR_TEXTE,
        relief="flat",
        bd=0,
        padx=15,
        pady=5,
        **kwargs
    )

def create_entry(parent, **kwargs):
    """Fonction pour créer un entry avec un style constant."""
    return tk.Entry(
        parent,
        bg=COULEUR_ENTREE,
        fg=COULEUR_TEXTE,
        font=POLICE,
        insertbackground=COULEUR_TEXTE,
        relief="flat",
        bd=2,
        **kwargs
    )

def style_window(fenetre, largeur=400, hauteur=480):
    """Fonction pour applique du style aux fenêtres. Elle permet aussi au fenêtres de se générer dans le centre de la fenêtre."""
    fenetre.configure(bg=COULEUR_FOND)
    fenetre.geometry(f"{largeur}x{hauteur}+{int(fenetre.winfo_screenwidth()/2 - largeur/2)}+{int(fenetre.winfo_screenheight()/2 - hauteur/2)}") # Calculation pour déterminer ou placer la fenêtre pour être dans le milieu de l'écran
    fenetre.resizable(False, False) # Empêcher l'utilisateur de modifier la taille de la fenêtre