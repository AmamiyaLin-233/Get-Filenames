import os
import tkinter

def btn1_click():
    filename = []
    for f in os.listdir():
        if os.path.isfile(f):
            filename.append(f)

    strfilename = "\n".join(filename)
    textbox.delete("1.0", tkinter.END)
    textbox.insert("1.0", strfilename)

def btn2_click():
    filename = textbox.get("1.0", tkinter.END)

    with open('files_output.txt', 'w') as f:
        f.write(filename)

def btn3_click():
    textbox.delete("1.0", tkinter.END)

'''GUI'''

main_window = tkinter.Tk()
main_window.title("Get Filenames")
main_window.geometry("590x440")

frame = tkinter.Frame(main_window)
frame.grid(row=0, column=0, padx=0, pady=0, sticky="w")

button1 = tkinter.Button(frame, text="  Get  ", command=btn1_click)
button1.grid(row=0, column=1, padx=10, pady=10, )

button2 = tkinter.Button(frame, text=" Save ", command=btn2_click)
button2.grid(row=0, column=2, padx=10, pady=10)

button3 = tkinter.Button(frame, text=" Clear ", command=btn3_click)
button3.grid(row=0, column=3, padx=10, pady=10)

label1 = tkinter.Label(main_window, text="Filename list is below: ")
label1.grid(row=1, column=0, padx=10, pady=0, sticky="w")

textbox = tkinter.Text(main_window)
textbox.grid(row=2, column=0, padx=10, pady=0)

label2 = tkinter.Label(main_window, text="Copyright © 2026 AmamiyaLin All Rights Reserved")
label2.config(fg="gray")
label2.grid(row=3, column=0, padx=10, pady=20, sticky="w")

main_window.mainloop()
