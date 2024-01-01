from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Socket:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", True)

        # Image labels
        # First header image
        img = Image.open(r"Images_GUI\n_ban5.png")
        img = img.resize((1366, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(r"Images_GUI\n_bg6.jpg")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Image labels
        # First header image
        img = Image.open(r"Images_GUI\n_ban5.png")
        img = img.resize((1366, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(r"Images_GUI\n_bg6.jpg")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)
        # Image labels
        # First header image
        img = Image.open(r"Images_GUI\n_ban5.png")
        img = img.resize((1366, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(r"Images_GUI\n_bg6.jpg")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

       
        # Second image
        img1 = Image.open(r"Images_GUI\faqs.jpg")
        img1 = img1.resize((500, 360))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        
        # title section1
        title_lb1 = Label(bg_img, text="FAQ's ", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=830, y=60, width=500,
                        height=50)

        # Set image as label
        f_lb2 = Label(self.root, image=self.photoimg1)
        f_lb2.place(x=830, y=250, width=500, height=360)

        # title section
        title_lb1 = Label(bg_img, text="HOW CAN I HELP YOU? ", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)


        # Main frame
        main_frame = Frame(self.root, bd=4, bg='white', width=730)
        main_frame.place(x=180, y=180)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('times new roman', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.place(x=180, y=620)

        label_1 = Label(btn_frame, text="Type Something", font=('times new roman', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send, font=('times new roman', 16, 'bold'), width=8,
                           bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data", command=self.clear_data, font=('times new roman', 16, 'bold'),
                            width=8, bg='red', fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_2 = Label(btn_frame, text=self.msg, font=('times new roman', 14, 'bold'), fg='red', bg='white')
        self.label_2.grid(row=1, column=1, padx=5, sticky=W)

    # ============Send Function======
    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')

    def clear_data(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        user_input = self.entry.get()
        send = '\t\t\t' + 'You: ' + user_input
        self.text.insert(END, '\n' + send)
        self.text.yview(END)

        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_2.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_2.config(text=self.msg, fg='red')

            # Bot responses based on user input
                       # Bot responses based on user input
            if user_input.lower() == 'hello':
                self.text.insert(END, "\n\n" + "Bot: Hi")
            elif user_input.lower() == 'hi':
                self.text.insert(END, "\n\n" + "Bot: Hello")
            elif user_input.lower() == 'how are you?':
                self.text.insert(END, "\n\n" + "Bot: Fine and you?")
            elif user_input.lower() == 'who made you?':
                self.text.insert(END, "\n\n" + "Bot: Sharjeel and Qaiser, students of Software Engineering from Foundation University")
            elif user_input.lower() == 'what is your purpose?':
                self.text.insert(END, "\n\n" + "Bot: I am designed to assist with queries related to the Face Recognition Attendance System.")
            elif user_input.lower() == 'can you explain the face recognition process?':
                self.text.insert(END, "\n\n" + "Bot: The system analyzes facial features to recognize and verify individuals based on unique characteristics.")
            elif user_input.lower() == 'where can the face recognition system be used?':
                self.text.insert(END, "\n\n" + "Bot: It can be used in various sectors, including security, healthcare, transportation, and law enforcement.")
            elif user_input.lower() == 'is it safe to use the face recognition system?':
                self.text.insert(END, "\n\n" + "Bot: Yes, it prioritizes security and follows privacy rules, ensuring the safety of facial data.")
            elif user_input.lower() == 'what are the potential benefits of the system?':
                self.text.insert(END, "\n\n" + "Bot: Benefits include accurate attendance tracking, enhanced security, and a user-friendly experience.")
            elif user_input.lower() == 'how quickly does the system identify a person?':
                self.text.insert(END, "\n\n" + "Bot: The identification process is typically fast, happening in a matter of seconds.")
            elif user_input.lower() == 'what happens if there are changes in a person\'s appearance?':
                self.text.insert(END, "\n\n" + "Bot: The system is designed to adapt to changes, recognizing individuals even with minor alterations.")
            elif user_input.lower() == 'can it be used for customer authentication in online services?':
                self.text.insert(END, "\n\n" + "Bot: Yes, it can be integrated into online platforms for secure customer authentication.")
            elif user_input.lower() == 'how user-friendly is the system for non-technical users?':
                self.text.insert(END, "\n\n" + "Bot: It's designed to be intuitive, with training and support materials for non-technical users.")
            elif user_input.lower() == 'does it store actual images of faces?':
                self.text.insert(END, "\n\n" + "Bot: No, the system converts facial features into a mathematical code, prioritizing privacy.")
            elif user_input.lower() == 'what if someone tries to trick the system with a photo or video?':
                self.text.insert(END, "\n\n" + "Bot: The system detects and prevents spoofing attempts, distinguishing between real faces and static images.")
            elif user_input.lower() == 'how can it be integrated into existing security systems?':
                self.text.insert(END, "\n\n" + "Bot: It easily fits with different security systems, adding an extra layer of smart security.")
            elif user_input.lower() == 'are there help and updates available?':
                self.text.insert(END, "\n\n" + "Bot: Yes, there's support, updates, and training available for optimal use of the Face Recognition System.")
            elif user_input.lower() == 'can it grow with my business?':
                self.text.insert(END, "\n\n" + "Bot: Absolutely! It's a flexible tool that can be adjusted to fit any business size.")
            elif user_input.lower() == 'is there a limit to the number of faces the system can recognize?':
                self.text.insert(END, "\n\n" + "Bot: The system is scalable and can handle a large database of faces.")
            elif user_input.lower() == 'how accurate is the system?':
                self.text.insert(END, "\n\n" + "Bot: It's highly accurate, with improvements over time through updates.")
            elif user_input.lower() == 'how can I contact support?':
                self.text.insert(END, "\n\n" + "Bot: You can contact support by emailing support@facerecognition.com or calling our helpline at +123456789.")
            elif user_input.lower() == 'what are the system requirements for installation?':
                self.text.insert(END, "\n\n" + "Bot: The system requires a standard computer with a webcam. Detailed system requirements can be found on our official website.")    
            else:
                self.text.insert(END, "\n\n" + "Bot: Sorry, I did not get it")

if __name__ == '__main__':
    root = Tk()
    obj = Socket(root)
    root.mainloop()
