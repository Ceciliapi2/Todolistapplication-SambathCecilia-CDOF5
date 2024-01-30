import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

tache_instances = []
taches_data = []

class Tache:
    def __init__(self, tache, date):
        self.tache = tache
        self.date = date

def ajout_tache():
    tache = tache_entry.get()
    date = date_entry.get()
    new_tache = Tache(tache, date)
    tache_instances.append(new_tache)
    tache_instances.append([tache, date])
    taches_tree.insert("", tk.END, values=(tache, date))
    tache_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    
def supprimer_tache():
    selected_item = taches_tree.selection()
    if selected_item:
        tache = taches_tree.item(selected_item)["values"][0]
        for tache in taches_data:
            if tache["tache"] == tache:
                taches_data.remove(tache)
                break
        taches_tree.delete(selected_item)
    else:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une commande à supprimer")

def double_click_taches(event):
    selected_item = taches_tree.focus()
    if selected_item:
        values = taches_tree.item(selected_item, "values")
        if values:
            tache_entry.delete(0, tk.END)
            tache_entry.insert(tk.END, values[0])
        


if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Liste des taches")

    scrollbar = tk.Scrollbar(root, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    canvas = tk.Canvas(root, yscrollcommand=scrollbar.set, height=500)
    canvas.pack(side="left", fill="both", expand=True)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    titre_label = tk.Label(frame, text="Taches", font=("Arial", 16))
    titre_label.pack(pady=5)
   
    columns_taches = ("tache", "date")
   
    tree_frame = tk.Frame(frame)
    tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)

    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical")
    scrollbar.pack(side='right', fill='y')

    style = ttk.Style()
    style.configure('Treeview', rowheight=25)

    taches_tree = ttk.Treeview(tree_frame, columns=columns_taches, show="headings", style='Custom.Treeview')
   
    scrollbar.config(command=taches_tree.yview)

    for col in columns_taches:
        taches_tree.heading(col, text=col)
        taches_tree.column(col, width=150)
   
    taches_tree.pack(fill=tk.BOTH, expand=True, pady=10)
    taches_tree.bind("<Double-1>", double_click_taches)

    input_frame_taches = tk.Frame(frame)
    input_frame_taches.pack()

    tache_label = tk.Label(input_frame_taches, text="Tache :")
    tache_label.pack(side=tk.LEFT, padx=5)
    tache_entry = tk.Entry(input_frame_taches)
    tache_entry.pack(side=tk.LEFT, padx=5)
    
    date_label = tk.Label(input_frame_taches, text="Date :")
    date_label.pack(side=tk.LEFT, padx=5)
    date_entry = tk.Entry(input_frame_taches)
    date_entry.pack(side=tk.LEFT, padx=5)

    button_frame_taches = tk.Frame(frame)
    button_frame_taches.pack(pady=10)
   
    add_button_taches = tk.Button(button_frame_taches, text="Ajouter une tache", command=ajout_tache)
    add_button_taches.pack(side=tk.LEFT, padx=5)
    
    delete_button_taches = tk.Button(button_frame_taches, text="Supprimer tache", command=supprimer_tache)
    delete_button_taches.pack(side=tk.LEFT, padx=5)
    

    root.mainloop()