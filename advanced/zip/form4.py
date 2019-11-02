from tkinter import *
from tkinter import ttk
import sqlite3
import os.path


class Product:
    db_name = 'database.db'

    def __init__(self, wind):
        self.wind = wind
        self.wind.title('IT Products')

        frame = LabelFrame(self.wind, text='Add new record')
        frame.grid(row=0, column=1)

        Label(frame, text='Name: ').grid(row=1, column=1)
        self.name = Entry(frame)
        self.name.grid(row=1, column=2)

        Label(frame, text='Surname: ').grid(row=2, column=1)
        self.price = Entry(frame)
        self.price.grid(row=2, column=2)

        ttk.Button(frame, text='Add record',
                   command=self.adding).grid(row=3, column=2)
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0)

        self.tree = ttk.Treeview(height=10, columns=("lname", "sex", "sdate", "dob"))
        self.tree.grid(row=100, column=0, columnspan=100)
        self.tree.heading('#0', text='First Name', anchor=W)
        self.tree.heading("lname", text='Last Name', anchor=W)
        self.tree.heading("sex", text='Gender', anchor=W)
        self.tree.heading("sdate", text='Start Date', anchor=W)
        self.tree.heading("dob", text='Birth Date', anchor=W)

        ttk.Button(text='Delete record', command=self.deleting).grid( row=10, column=5)
        ttk.Button(text='Edit record').grid(row=10, column=1)

        self.viewing_records()

    def run_query(self, query, parameters=()):

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # query = 'SELECT * FROM customers '
        # db_rows = self.run_query(query)
        # for row in db_rows:
        #     # self.tree.insert('', 2, text=str(), values=(row[1], row[2], row[3]))
        #     self.tree.insert('', 2, text=row[1], values=(row[1], row[2], row[3]))

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def adding(self):

        if self.validation():
            query='INSERT INTO customersVALUES (NULL, ?, ?)'
            parameters=(self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text']='Record {} added'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text']='Name field or price is empty'
            self.viewing_records()


    def deleting(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            #self.message[text]='Please select record'
            return
        self. message['text']=''
        name=self.tree.item(self.tree.selection())['text']
        query='DELETE FROM customers WHERE name = ?'
        self.run_query(query, (name,))
        self.message['text']='Record {} deleted'.format(name)
        self.viewing_records()





if __name__ == '__main__':
    wind=Tk()
    application=Product(wind)
    wind.mainloop()
