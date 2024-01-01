from tkinter import Label, Tk, Button
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
import pyttsx3
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

thread_lock = threading.Lock()

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

class Train:
    def __init__(self, root):
        speak_va("Training Panel")
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Panel")

        # Header image
        img = Image.open(r"C:\Users\Win 10\Desktop\z\Face-Recognition-based-Attendance-System-main\Images_GUI\n_ban5.png")
        img = img.resize((1366, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(r"C:\Users\Win 10\Desktop\z\Face-Recognition-based-Attendance-System-main\Images_GUI\n_bg6.jpg")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="Welcome to Training Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Training button
        std_img_btn = Image.open(r"C:\Users\Win 10\Desktop\z\Face-Recognition-based-Attendance-System-main\Images_GUI\t_btn1.png")
        std_img_btn = std_img_btn.resize((180, 180))
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.start_threads, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.start_threads, text="Start Training", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

    def train_classifier(self):
        with thread_lock:
            data_dir = "data_img"
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

            faces = []
            ids = []

            for image in path:
                img = Image.open(image).convert('L')  # convert to gray scale
                image_np = np.array(img, 'uint8')
                image_id = int(os.path.split(image)[1].split('.')[1])

                faces.append(image_np)
                ids.append(image_id)

                cv2.imshow("Training", image_np)
                cv2.waitKey(1) == 13

            ids = np.array(ids)

            # Train Classifier
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("clf.xml")

            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training Dataset Completed!", parent=self.root)

    def respond_user(self):
        with thread_lock:
            # Code for responding to the user goes here
            pass

    def start_threads(self):
        thread_user = threading.Thread(target=self.respond_user)
        thread_train = threading.Thread(target=self.train_classifier)

        thread_user.start()
        thread_train.start()

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
