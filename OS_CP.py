from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os
import shutil

# Creating the backend functions
def open_file():
    file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])

    os.startfile(os.path.abspath(file))


def copy_file():
    file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")])
    dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")

    try:
        shutil.copy(file_to_copy, dir_to_copy_to)
        mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
    except:
        mb.showerror(title='Error!', message='We were unable to copy your file to the desired location. Please try again')


def delete_file():
    file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])

    os.remove(os.path.abspath(file))

    mb.showinfo(title='File deleted', message='Your desired file has been deleted')


def rename_file():
    file = fd.askopenfilename(title='Choose a file to rename', filetypes=[("All files", "*.*")])

    if not file:
        return  # User canceled

    rename_wn = Toplevel(root)
    rename_wn.title("Rename the file to")
    rename_wn.geometry("300x100")
    rename_wn.resizable(0, 0)

    Label(rename_wn, text='What should be the new name of the file?', font=("Times New Roman", 10)).place(x=0, y=0)

    new_name = Entry(rename_wn, width=40, font=("Times New Roman", 10))
    new_name.place(x=0, y=30)

    def rename():
        new_file_name = os.path.join(os.path.dirname(file), new_name.get() + os.path.splitext(file)[1])

        try:
            os.rename(file, new_file_name)
            mb.showinfo(title="File Renamed", message='Your desired file has been renamed')
            rename_wn.destroy()
        except:
            mb.showerror(title='Error', message='Failed to rename the file. Please try again')

    rename_button = Button(rename_wn, text="Rename", font=("Times New Roman", 10), command=rename)
    rename_button.place(x=130, y=70)


def open_folder():
    folder = fd.askdirectory(title="Select Folder to open")
    os.startfile(folder)


def delete_folder():
    folder_to_delete = fd.askdirectory(title='Choose a folder to delete')
    os.rmdir(folder_to_delete)
    mb.showinfo("Folder Deleted", "Your desired folder has been deleted")


def move_folder():
    folder_to_move = fd.askdirectory(title='Select the folder you want to move')
    mb.showinfo(message='You just selected the folder to move, now please select the desired destination where you want to move the folder to')
    destination = fd.askdirectory(title='Where to move the folder to')

    try:
        shutil.move(folder_to_move, destination)
        mb.showinfo("Folder moved", 'Your desired folder has been moved to the location you wanted')
    except:
        mb.showerror('Error', 'We could not move your folder. Please make sure that the destination exists')


def list_files_in_folder():
    folder = fd.askdirectory(title='Select the folder whose files you want to list')

    if not folder:
        return  # User canceled

    files = os.listdir(folder)

    list_files_wn = Toplevel(root)
    list_files_wn.title('Files in your selected folder')
    list_files_wn.geometry('300x400')
    list_files_wn.resizable(0, 0)

    listbox = Listbox(list_files_wn, selectbackground='SteelBlue', font=("Georgia", 10), height=15, width=40)

    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox.config(yscrollcommand=scrollbar.set)
    listbox.pack(padx=10, pady=10, fill=BOTH, expand=True)
    
    count = 0
    for file in files:
        listbox.insert(END, file)
        count += 1

    listbox.insert(END, "")
    listbox.insert(END, "Num of files = {}".format(count))
    list_files_wn.mainloop()  # Start the list_files_wn main loop
    


# Defining the variables
title = 'ET-C3 Group 2 File Manager'
background = 'Grey'

button_font = ("Times New Roman", 13)
button_background = 'White'

# Initializing the window
root = Tk()
root.title(title)
root.geometry('320x400')
root.resizable(0, 0)
root.config(bg=background)

# Creating and placing the components in the window
Label(root, text=title, font=("Comic Sans MS", 15), bg=background, wraplength=350).place(x=20, y=0)

Button(root, text='Open a file', width=20, font=button_font, bg=button_background, command=open_file).place(x=60, y=50)

Button(root, text='Copy a file', width=20, font=button_font, bg=button_background, command=copy_file).place(x=60, y=90)

Button(root, text='Rename a file', width=20, font=button_font, bg=button_background, command=rename_file).place(x=60, y=130)

Button(root, text='Delete a file', width=20, font=button_font, bg=button_background, command=delete_file).place(x=60, y=170)

Button(root, text='Open a folder', width=20, font=button_font, bg=button_background, command=open_folder).place(x=60, y=210)

Button(root, text='Delete a folder', width=20, font=button_font, bg=button_background, command=delete_folder).place(x=60, y=250)

Button(root, text='Move a folder', width=20, font=button_font, bg=button_background, command=move_folder).place(x=60, y=290)

Button(root, text='List all files in a folder', width=20, font=button_font, bg=button_background,
       command=list_files_in_folder).place(x=60, y=330)

# Finalizing the window
root.update()
root.mainloop()
