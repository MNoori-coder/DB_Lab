from tkinter import *
import DAL
import tkinter.messagebox

window = Tk()
window.title("My library")
window.resizable(width=False, height=False)
window.configure(bg='gray')

# -------------------------------- Labels --------------------------------
l1 = Label(window, text='Title', bg='gray')
l1.grid(row=0, column=0, padx=5, pady=5)

l2 = Label(window, text='Author', bg='gray')
l2.grid(row=0, column=2, padx=5, pady=5)

l3 = Label(window, text='Year', bg='gray')
l3.grid(row=1, column=0, padx=5, pady=5)

l4 = Label(window, text='ISBN', bg='gray')
l4.grid(row=1, column=2, padx=5, pady=5)

# -------------------------------- Entries --------------------------------
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1, padx=5, pady=5)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3, padx=5, pady=5)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1, padx=5, pady=5)

ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3, padx=5, pady=5)


# -------------------------------- Scrollbar --------------------------------
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# -------------------------------- ListView --------------------------------
list1 = Listbox(window, width=35, height=10)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, padx=5, pady=5)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

is_select = False

def get_selected_row(event):
    global selected_book
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]     # (index, )
        selected_book = list1.get(index)
        global is_select
        is_select = True
        # Title
        e1.delete(0, END)
        e1.insert(END, selected_book[1])
        # Author
        e2.delete(0, END)
        e2.insert(END, selected_book[2])
        # Year
        e3.delete(0, END)
        e3.insert(END, selected_book[3])
        # ISBN
        e4.delete(0, END)
        e4.insert(END, selected_book[4])


list1.bind("<<ListboxSelect>>", get_selected_row)

# -------------------------------- Buttons --------------------------------
b1 = Button(window, text='View All', width=12, command=lambda: view_command(), bg='yellow')
b1.grid(row=2, column=3, padx=5, pady=5)


b2 = Button(window, text='Search', width=12,
            command=lambda: search_command(), bg='pink')
b2.grid(row=3, column=3, padx=5, pady=5)

b3 = Button(window, text='Insert', width=12, command=lambda: insert_command(), bg='green')
b3.grid(row=4, column=3, padx=5, pady=5)

b4 = Button(window, text='Update Selected', width=12,
            command=lambda: update_command(), bg='blue')
b4.grid(row=5, column=3, padx=5, pady=5)

b5 = Button(window, text='Delete Selected', width=12,
            command=lambda: delete_command(), bg='red')
b5.grid(row=6, column=3, padx=5, pady=5)

b6 = Button(window, text='Quit', width=12, command=window.destroy, bg='orange')
b6.grid(row=7, column=3, padx=5, pady=5)


# -------------------------------- BLL --------------------------------

def errorMsg(msg):
    tkinter.messagebox.showerror('Error!', msg)

def clear_list():
    list1.delete(0, END)


def fill_list(books):
    for book in books:
        list1.insert(END, book)


def view_command():
    global is_select
    is_select = False
    clear_list()
    books = DAL.view()
    # Title
    e1.delete(0, END)
    # Author
    e2.delete(0, END)
    # Year
    e3.delete(0, END)
    # ISBN
    e4.delete(0, END)
    fill_list(books)


view_command()


def search_command():
    if (title_text.get() == '') and (author_text.get() == '') and (year_text.get() == '') and (ISBN_text.get() == ''):
        errorMsg('Please enter at least one value!')
        return 0
    global is_select
    is_select = False
    clear_list()
    books = DAL.search(title_text.get(), author_text.get(),
                       year_text.get(), ISBN_text.get())
    fill_list(books)


def insert_command():
    if (title_text.get() == '') or (author_text.get() == '') or (year_text.get() == '') or (ISBN_text.get() == ''):
        errorMsg('Please fill all inputs!')
        return 0
    global is_select
    is_select = False
    DAL.insert(title_text.get(), author_text.get(),
               year_text.get(), ISBN_text.get())
    view_command()


def delete_command():
    global is_select
    if is_select:
        DAL.delete(selected_book[0])   # (id, title, author, year, ISBN)
        is_select = False
    else:
        errorMsg('No book has been selected!')
        return 0
    view_command()


def update_command():
    global is_select
    if is_select:
        if (title_text.get() == '') or (author_text.get() == '') or (year_text.get() == '') or (ISBN_text.get() == ''):
            errorMsg('Please fill all inputs!')
            return 0
        DAL.update(selected_book[0], title_text.get(), author_text.get(),
                year_text.get(), ISBN_text.get())
        is_select = False
    else:
        errorMsg('No book has been selected!')
        return 0
    view_command()


window.mainloop()
