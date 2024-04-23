import cv2
from tkinter import *
from PIL import Image, ImageTk


def open_camera():
    cap = cv2.VideoCapture(0) # 0 is the default camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the image to PIL format
        frame = Image.fromarray(frame)

        # Convert the image to a Tkinter-compatible photo image
        frame = ImageTk.PhotoImage(frame)

        # Display the image in the GUI
        label.config(image=frame)
        label.image = frame

        root.update()

    cap.release()

root = Tk()
root.title("Camera Feed")

button1 = Button(root, text="Open Camera", command=open_camera)
button1.pack()

label = Label(root)
label.pack()

root.mainloop()
