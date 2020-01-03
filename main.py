from tkinter import *
from tkinter.filedialog import askopenfilename


def open_directory():
    file_selected = askopenfilename()
    text_url.delete(0, END)
    text_url.insert(0, file_selected)
    print(file_selected)

window = Tk()

window.geometry("700x500")
window.title("Emotion in video")

title_label = Label(window, text="Label")
title_label.grid(row=0, columnspan=4)

video_url_label = Label(window, text="video url: ")
video_url_label.grid(row=1)

button = Button(window, text='press',command=open_directory)
button.grid(row=1, column=2)

text_url = Entry(window, width=80)
text_url.grid(row=1, column=1)

window.mainloop()