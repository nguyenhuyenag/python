from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import mysql.connector

# --------------- connect database --------------- #
datasource = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="account_db"
)

cursor = datasource.cursor()

root = Tk()
root.title("Ứng dụng Python Form")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(width=TRUE, height=True)


def insert(fetch):
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))


def load():
    tree.delete(*tree.get_children())
    sql = "SELECT * FROM user ORDER BY id ASC"
    cursor.execute(sql)
    fetch = cursor.fetchall()
    insert(fetch)


def clear():
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    ADDRESS.set("")
    USERNAME.set("")


def update():
    if GENDER.get() == "":
        txt_result.config(text="Vui lòng chọn giới tính", fg="red")
    else:
        sql = "SELECT * FROM user"
        cursor.execute(sql)
        data = cursor.fetchall()
        for x in data:
            if int(x[0]) != int(id) and USERNAME.get() == x[1]:
                txt_result.config(text="Tài khoản đã tồn tại", fg="red")
                return

        if GENDER.get() == 0:
            gt = "Nữ"
        elif GENDER.get() == 1:
            gt = "Nam"
        sql = "UPDATE user SET firstname = %s, lastname = %s, gender = %s, address = %s, username = %s WHERE id = %s"
        val = (FIRSTNAME.get(), LASTNAME.get(), gt, ADDRESS.get(), USERNAME.get(), id)
        cursor.execute(sql, val)
        datasource.commit()
        load()
        clear()
        btn_create.config(state=NORMAL)
        btn_update.config(state=DISABLED)
        btn_delete.config(state=NORMAL)
        txt_result.config(text="Cập nhật dữ liệu thành công", fg="green")


def create():
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or ADDRESS.get() == "" or USERNAME.get() == "":
        txt_result.config(text="Bạn chưa điền đủ thông tin!", fg="red")
    else:
        sql = "SELECT * FROM user"
        cursor.execute(sql)
        data = cursor.fetchall()
        for x in data:
            if USERNAME.get() == x[1]:
                txt_result.config(text="Tài khoản đã tồn tại", fg="red")
                return
        if GENDER.get() == 0:
            gt = "Nữ"
        elif GENDER.get() == 1:
            gt = "Nam"
        sql = "INSERT INTO user (firstname, lastname, gender, address, username) VALUES (%s, %s, %s, %s, %s)"
        val = (FIRSTNAME.get(), LASTNAME.get(), gt, ADDRESS.get(), USERNAME.get())
        cursor.execute(sql, val)
        datasource.commit()

        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM user ORDER BY id ASC")
        fetch = cursor.fetchall()
        insert(fetch)
        clear()
        txt_result.config(text="Tạo tài khoản thành công", fg="green")


def onSelected(event):
    global id
    curItem = tree.focus()
    contents = (tree.item(curItem))
    clear()
    if hasattr(contents, 'values'):
        selecteditem = contents['values']
        if len(selecteditem) == 6:
            id = selecteditem[0]
            USERNAME.set(selecteditem[1])
            FIRSTNAME.set(selecteditem[2])
            LASTNAME.set(selecteditem[3])
            if selecteditem[4].upper() == "Nam".upper():
                GENDER.set(1)
            elif selecteditem[4].upper() == "Nữ".upper():
                GENDER.set(0)
            ADDRESS.set(selecteditem[5])
    btn_create.config(state=DISABLED)
    btn_update.config(state=NORMAL)
    btn_delete.config(state=DISABLED)


def delete():
    if not tree.selection():
        txt_result.config(text="Vui lòng chọn dòng cần xóa\n", fg="red")
    else:
        result = tkMessageBox.askquestion('', 'Bạn muốn xóa dòng này?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor.execute("DELETE FROM user WHERE id = %d" % int(selecteditem[0]))
            datasource.commit()
            txt_result.config(text="Xóa dữ liệu thành công", fg="green")


def close():
    result = tkMessageBox.askquestion("Xác nhận", "Bạn muốn đóng chương trình?", icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = IntVar()
ADDRESS = StringVar()
USERNAME = StringVar()
GENDER.set(1)

Top = Frame(root, width=900, height=50, bd=8)
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8)
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8)
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8)
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
Radiobutton(RadioGroup, text="Nam", variable=GENDER, value=1, font=('arial', 16)).pack(side=LEFT)
Radiobutton(RadioGroup, text="Nữ", variable=GENDER, value=0, font=('arial', 16)).pack(side=LEFT)


txt_title = Label(Top, width=900, font=('arial', 24), text="Quản Lý Người Dùng")
txt_title.pack()
txt_firstname = Label(Forms, text="Họ:", font=('arial', 16), bd=15)
txt_firstname.grid(row=0, sticky="e")
txt_lastname = Label(Forms, text="Tên:", font=('arial', 16), bd=15)
txt_lastname.grid(row=1, sticky="e")
txt_gender = Label(Forms, text="Giới tính:", font=('arial', 16), bd=15)
txt_gender.grid(row=2, sticky="e")
txt_address = Label(Forms, text="Địa chỉ:", font=('arial', 16), bd=15)
txt_address.grid(row=3, sticky="e")
txt_username = Label(Forms, text="Tài khoản:", font=('arial', 16), bd=15)
txt_username.grid(row=4, sticky="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

# ==================================ENTRY WIDGET=======================================
firstname = Entry(Forms, textvariable=FIRSTNAME, width=30)
firstname.grid(row=0, column=1)
lastname = Entry(Forms, textvariable=LASTNAME, width=30)
lastname.grid(row=1, column=1)
RadioGroup.grid(row=2, column=1)
address = Entry(Forms, textvariable=ADDRESS, width=30)
address.grid(row=3, column=1)
username = Entry(Forms, textvariable=USERNAME, width=30)
username.grid(row=4, column=1)

# ==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Thêm", command = create)
btn_create.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Cập nhật", command=update, state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Xóa", command=delete)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Thoát", command=close)
btn_exit.pack(side=LEFT)

# ==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)

fields = ["ID", "Tài Khoản", "Họ", "Tên", "Giới Tính", "Địa Chỉ"]

tree = ttk.Treeview(Right, columns=fields, selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading(fields[0], text=fields[0], anchor=W)
tree.heading(fields[1], text=fields[1], anchor=W)
tree.heading(fields[2], text=fields[2], anchor=W)
tree.heading(fields[3], text=fields[3], anchor=W)
tree.heading(fields[4], text=fields[4], anchor=W)
tree.heading(fields[5], text=fields[5], anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=50)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', onSelected)








if __name__ == '__main__':
    load()
    root.mainloop()
