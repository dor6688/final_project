from tkinter import *
from tkinter.filedialog import askopenfilename
#from extract_audio_from_video import *
from image_to_color import *
from color.color_detection import *


def open_directory():
    file_selected = askopenfilename()
    text_url_entry.delete(0, END)
    text_url_entry.insert(0, file_selected)
    print("selected - " + file_selected)


def extract_audio():
    x=4
    #extract_audio_from_clip(text_url_entry.get(),r"C:\Users\dorlev.BGU-USERS\PycharmProjects\final_project\audios\tmp1.wav")


def get_colors():
    rgb_name(get_colors_names(text_url_entry.get()))


########## GUI ###########
window = Tk()

window.geometry("700x500")
window.title("Emotion in video")

title_label = Label(window, text="Title Here")
title_label.grid(row=0, columnspan=4)

video_url_label = Label(window, text="video url: ")
video_url_label.grid(row=1)

select_video_button = Button(window, text='press',command=open_directory)
select_video_button.grid(row=1, column=2)

text_url_entry = Entry(window, width=80)
text_url_entry.grid(row=1, column=1)

extract_audio_button = Button(window, text='Predict', command=extract_audio)
extract_audio_button.grid(row=2)

color_button = Button(window, text='Color', command=get_colors)
color_button.grid(row=2, column=1)

window.mainloop()