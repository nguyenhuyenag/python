import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk

datasource = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="student_db"
)


def buildForm(root):
    fields = ("ID", "NAME", "COLLEGE", "PHONE", "ADDRESS")
    entries = {}
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        #ent.insert(0, "0")
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries[field] = ent
    return entries


if __name__ == '__main__':

    root = tk.Tk()
    
    ents = buildForm(root)

    b1 = tk.Button(root, text='Get', command=(lambda e=ents: final_balance(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)

    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()
