from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os
import shutil
import zipfile

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

def extract_zip_to_folder():
    zip_path = fd.askopenfilename(title='Choose a ZIP file to extract', filetypes=[("ZIP files", "*.zip")])
    extract_folder = fd.askdirectory(title="Choose the folder to extract to")

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        mb.showinfo(title='Extraction Complete', message='ZIP file extracted successfully.')
    except Exception as e:
        mb.showerror(title='Error', message=f'Error extracting ZIP file: {e}')


def open_in_terminal():
    folder = fd.askdirectory(title="Select Folder to open in terminal")
    if folder:
        os.system(f"start cmd /K cd /d {folder}")

def search_file():
    folder = fd.askdirectory(title="Select Folder to Search")
    if not folder:
        return  # User canceled

    search_dialog = Toplevel(root)
    search_dialog.title("Search for a File")
    search_dialog.geometry("300x100")
    search_dialog.resizable(0, 0)

    Label(search_dialog, text="Enter the name of the file:", font=("Arial", 12)).pack(pady=10)

    search_entry = Entry(search_dialog, font=("Arial", 10), width=30)
    search_entry.pack()

    def perform_search():
        file_name = search_entry.get()
        if file_name:
            results = [file for file in os.listdir(folder) if file_name in file]
            if results:
                results_wn = Toplevel(search_dialog)
                results_wn.title("Search Results")
                results_wn.geometry("400x300")
                results_wn.resizable(0, 0)

                listbox = Listbox(results_wn, selectbackground='SteelBlue', font=("Arial", 10), height=15, width=50)

                scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
                scrollbar.pack(side=RIGHT, fill=Y)

                listbox.config(yscrollcommand=scrollbar.set)
                listbox.pack(padx=10, pady=10, fill=BOTH, expand=True)

                for result in results:
                    listbox.insert(END, result)

            else:
                mb.showinfo("Search Results", "No matching files found.")
        else:
            mb.showinfo("Search Results", "Please enter a valid file name.")

    search_button = Button(search_dialog, text="Search", font=("Arial", 10), command=perform_search)
    search_button.pack(pady=5)


def show_properties():
    path = fd.askopenfilename(title="Select File/Folder to show properties", filetypes=[("All files", "*.*")])
    # path = fd.askdirectory(title="Select File/Folder to show properties")
    if path:
        properties_wn = Toplevel(root)
        properties_wn.title("Properties")
        properties_wn.geometry("300x200")
        properties_wn.resizable(0, 0)

        Label(properties_wn, text="Properties of selected file/folder:", font=("Arial", 12)).pack(pady=10)

        properties_text = Text(properties_wn, wrap=WORD, font=("Arial", 10))
        properties_text.pack(fill=BOTH, expand=True, padx=10, pady=5)

        properties = ""
        if os.path.exists(path):
            properties += f"Path: {path}\n"
            properties += f"Size: {os.path.getsize(path)} bytes\n"
            properties += f"Last Modified: {os.path.getmtime(path)}\n"
            properties += f"Is Directory: {os.path.isdir(path)}\n"
        else:
            properties = "Selected file/folder does not exist."

        properties_text.insert(END, properties)
        properties_text.config(state=DISABLED)


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

# button_font = ("Times New Roman", 13)
button_font = ("Bell Gothic Std Light", 13)
button_background = 'White'

# Initializing the window
root = Tk()
root.title(title)
root.geometry('320x530')
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

Button(root, text='Extract a ZIP to a Folder', width=20, font=button_font, bg=button_background, command=extract_zip_to_folder).place(x=60, y=370)

Button(root, text='Open in Terminal', width=20, font=button_font, bg=button_background, command=open_in_terminal).place(x=60, y=410)

# Adding the "Show Properties" button
Button(root, text='Show Properties', width=20, font=button_font, bg=button_background, command=show_properties).place(x=60, y=450)

Button(root, text='Search for a File', width=20, font=button_font, bg=button_background, command=search_file).place(x=60, y=490)

# Finalizing the window
root.update()
root.mainloop()
