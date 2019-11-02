import tkinter as tk
import tkinter.ttk as ttk
#import sqlite3
import tkinter.messagebox as msg

dbname = "text.db"
#c = sqlite3.connect(dbname)


def read_tree_view(sql):
    i = 0
    for r in c.execute(sql):
        tree.insert("", "end", tags=i, values=r)
        if i & 1:
            tree.tag_configure(i, background="#CCFFFF")
        i += 1


root = tk.Tk()
root.title("text Input business")
root.resizable(width=False, height=False)
#root.geometry("860x610")
#mainwindow.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 600))

frame4 = tk.LabelFrame(root, bd=2, relief="ridge", text=" time ", width=250, height=150, foreground="purple")
frame4.place(x=0, y=10)
label6 = tk.Label(frame4, text="　Input 1　", width=10, height=2, bd=1)
label6.grid(row=1, column=1, padx=14, ipadx=10)
val = tk.StringVar()
box4 = ttk.Combobox(frame4, values=("  ", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30",
                                    "13:00", "13:30", "14:00", "14:30", "15:00"), textvariable=val, state='readonly', width=12, height=2)
box4.current(0)
box4.grid(row=1, column=2, padx=10, ipady=5)
label7 = tk.Label(frame4, text=" Input 2", width=10, height=2)
label7.grid(row=2, column=1, padx=10, pady=7)
val = tk.StringVar()
box5 = ttk.Combobox(frame4, values=("  ", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00",
                                    "13:30", "14:00", "14:30", "15:00", "15:30"), textvariable=val, state='readonly', width=12, height=2)
box5.current(0)
box5.grid(row=2, column=2, padx=10, ipady=3)

tree = ttk.Treeview(root)
tree.place(x=3, y=350)
tree["columns"] = (1, 2, 3, 4)
tree["show"] = "headings"

tree.column(1, width=195)
tree.column(2, width=195)
tree.column(3, width=195)
tree.column(4, width=195)
# tree.column(5, width=45)
# tree.column(6, width=60)
# tree.column(7, width=60)
# tree.column(8, width=60)
# tree.column(9, width=100)
# tree.column(10, width=50)
# tree.column(11, width=210)
# tree.column(12, width=30)

tree.heading(1, text="id")
tree.heading(2, text="2")
tree.heading(3, text="3")
tree.heading(4, text="4")
# tree.heading(5, text="5")
# tree.heading(6, text="6")
# tree.heading(7, text="7")
# tree.heading(8, text="8")
# tree.heading(9, text="9")
# tree.heading(10, text="10")
# tree.heading(11, text="11")
# tree.heading(12, text="12")

# sql = """
# 	SELECT 主.id,主.date,属性.[姓]||属性.[名],主.time1,主.time2,主.rest,食事.meal,送迎.pickup,施設外.outside,主.time3,主.absence,主.addition
# 	FROM main as 主,user as 属性,meal as 食事,pickup as 送迎,outside as 施設外
# 	WHERE 主.user = 属性.id = 食事.id = 送迎.id = 施設外.id
# 	ORDER BY user
# 	"""


# read_tree_view(sql)

root.mainloop()
