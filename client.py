import socket
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Client:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Client - Face Recognition System")
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", True)

        # ... (Same code as before for UI setup)

        # Client socket setup
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))  # Connect to the server (change the address/port if needed)

    # ============Send Function======
    def send(self):
        user_input = self.entry.get()
        self.client_socket.send(user_input.encode("utf-8"))
        self.entry.set('')

if __name__ == '__main__':
    root = Tk()
    obj = Client(root)
    root.mainloop()
