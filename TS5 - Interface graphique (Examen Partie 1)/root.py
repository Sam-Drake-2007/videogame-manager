import tkinter as tk
import window_commands as wc

root = tk.Tk()
root.title("Menu")
root.geometry("300x500")
#main_window.overrideredirect(True)

logo_photo = tk.PhotoImage(file="logo.gif")
logo_label = tk.Label(image=logo_photo)
logo_label.pack()

creer_obj_btn = tk.Button(root)
creer_obj_btn.config(text="Créer des objets", command=wc.creer_obj)
creer_obj_btn.pack()

ouvrir_prop_obj_btn = tk.Button(root)
ouvrir_prop_obj_btn.config(text="Ouvrir/modifier les propriétés d'un objet", command=wc.choisir_obj)
ouvrir_prop_obj_btn.pack()

supp_obj_btn = tk.Button(root)
supp_obj_btn.config(text="Supprimer un objet")
supp_obj_btn.pack()

quitter_btn = tk.Button(root)
quitter_btn.config(text="Quitter", command=exit)
quitter_btn.pack()

flex_label = tk.Label(root)
flex_label.pack()

root.mainloop()