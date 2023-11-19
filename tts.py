from tkinter import *
from tkinter import ttk
from gtts import gTTS
import os
import platform

window = Tk()
window.geometry("650x400")
window.title("Text To Speach")
window.config(bg="darkblue")


c2 = StringVar()


def clear():
    entry_file.delete(0, END)
    entry_input.delete(0, END)
    lang_select.set("Choose a Language")
    status_lable.place_forget()
    button_listen.place_forget()


def listen():
    os.system("vlc " + entry_file.get() + ".wav")


def browse():
    if platform.system() == "Linux":
        os.system("nautilus .")
    elif platform.system() == "Windows":
        os.system("start .")


def text_to_speech(text):
    if entry_input.get() == "" or entry_file.get() == "":
        status_lable.config(text="Please Check the fields")
        entry_input.config(highlightbackground="red", highlightcolor="red")
        entry_file.config(highlightbackground="red", highlightcolor="red")

    elif c2.get() == "":
        status_lable.config(text="Please Select a language")

    else:
        try:
            entry_input.config(highlightbackground="green", highlightcolor="green")
            entry_file.config(highlightbackground="green", highlightcolor="green")
            # Create a gTTS object

            tts = gTTS(text=entry_input.get(), lang=c2.get(), slow=False)

            # Save the speech to a file
            tts.save(entry_file.get() + ".wav")
            status_lable.place(x=1, y=255)
            status_lable.config(text="Done, Your file saved on the project directory")
            button_browse.place(x=1, y=300)
            button_listen.place(x=150, y=300)

        except:
            status_lable.config(
                text="Please Check your internet or the language selection"
            )


menubar = Menu(window)
window.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
help_menu = Menu(menubar)

# add a menu item to the menu

file_menu.add_command(label="Browse", command=lambda: browse())

file_menu.add_command(label="Clear data", command=lambda: clear())

file_menu.add_command(label="Exit", command=window.destroy)


# add the File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)


window_title = Label(
    window, text="Text To Speach", font=("Arial", 14, "bold"), bg="darkblue", fg="white"
)
window_title.place(x=140, y=1)

label_file = Label(
    window,
    text="Enter File name: ",
    bg="darkblue",
    fg="white",
    font=("verdana", "10", "bold"),
)
label_file.place(x=140, y=50)

entry_file = Entry(
    window, width=25, font=("verdana", "10", "bold"), highlightthickness=2
)
entry_file.place(x=100, y=70)

label_lang = Label(
    window,
    text="Select Speach LANGUAGE: ",
    bg="darkblue",
    fg="white",
    font=("verdana", "10", "bold"),
)
label_lang.place(x=140, y=100)

lang_select = ttk.Combobox(
    window, width=24, state="readonly", textvariable=c2, font=("verdana", "10", "bold")
)
lang_select.set("Choose a Language")
lang_select.place(x=100, y=120)
lang_select["values"] = (
    "ar",
    "en",
)

label_input = Label(
    window,
    text="Enter Your TEXT: ",
    bg="darkblue",
    fg="white",
    font=("verdana", "10", "bold"),
)
label_input.place(x=140, y=150)

entry_input = Entry(
    window, width=25, font=("verdana", "10", "bold"), highlightthickness=2
)
entry_input.place(x=100, y=170, height=43)


button_ = Button(
    window,
    text="Convert",
    cursor="hand2",
    border=5,
    command=lambda: text_to_speech(entry_input.get()),
    font=("verdana", "10", "bold"),
)
button_.place(x=150, y=215)

button_clear = Button(
    window,
    text="Clear",
    cursor="hand2",
    border=5,
    command=lambda: clear(),
    font=("verdana", "10", "bold"),
    height=1,
)
button_clear.place(x=1, y=1)

button_browse = Button(
    window,
    text="Browse",
    cursor="hand2",
    border=5,
    command=lambda: browse(),
    font=("verdana", "10", "bold"),
    height=1,
)
button_browse.place_forget()

button_listen = Button(
    window,
    text="Listen",
    cursor="hand2",
    border=5,
    command=lambda: listen(),
    font=("verdana", "10", "bold"),
)
button_listen.place_forget()

status_lable = Label(
    window, text="", font=("verdana", "10", "bold"), fg="red", bg="darkblue"
)

sc_img = PhotoImage(file="icon.png")



input_btn_r = Label(window, image=sc_img, width=200, height=200,bg="darkblue")
input_btn_r.place(x=400, y=70)

status_lable.place(x=1, y=255)

dev_name = Label(
    window,
    text="Adam Wael",
    font=("Arial", 14, "bold"),
    bg="darkblue",
    fg="white",
)
dev_name.place(x=400, y=10)
dev_age = Label(
    window,
    text="Age: 15",
    font=("Arial", 14, "bold"),
    bg="darkblue",
    fg="white",
)
dev_age.place(x=400, y=30)

window.mainloop()
