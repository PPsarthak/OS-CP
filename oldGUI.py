#OLD CONTENT


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
