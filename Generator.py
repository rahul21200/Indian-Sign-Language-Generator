def rr_main():
    import speech_recognition as sr
    import cv2
    import os
    import time
    import imageio as io
    import matplotlib.pyplot as plt
    import os
    import skvideo.io
    import numpy as np
    from matplotlib.animation import FuncAnimation
    import tkinter as tk
    import imageio
    from tkinter import messagebox

    # Function to display images

    def display(img, title="Original"):
        plt.imshow(img, cmap='gray'), plt.title(title)
        plt.axis('off')
        plt.show(block=False)
        plt.pause(2)
        plt.close

    # path = (r'C:\Users\USER\OneDrive\Desktop\Proj\Indian Sign Language Generation\Reverse sign images\\')
    dir_name = os.path.dirname(__file__)
    filename = os.path.join(
        dir_name, 'Reverse sign images//')

    path = filename
    voice = sr.Recognizer()
    text = []
    with sr.Microphone() as source:
        # top=tk.Tk()
        messagebox.showinfo('Info', 'Speak Now')
        #print("Speak Now")
        audio = voice.listen(source)
        try:
            messagebox.showinfo('Info', 'Recognizing...')
            # print("Recognizing....")
            text = voice.recognize_google(audio)
            messagebox.showinfo('Info', 'You said: '+str(text))
            print("You Said: ", text)
        except:
            # print("Your voice is not clear")
            messagebox.showerror("error", "Your voice is not clear")

    text.lower()
    # text = "".join(text)
    print(type(text))
    try:
        for l in text:
            if l != ' ':
                img = imageio.imread(path+str(l)+'.jpg')
                display(img, l)
    except:
        for l in text:
            if l != ' ':
                img = imageio.imread(path+str(l)+'.jpg')
                display(img, l)
        messagebox.showerror("error", "There was an error reading the input")

# rr_main()
