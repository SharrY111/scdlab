import socket
import threading
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Server:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Server - Face Recognition System")
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", True)

        # ... (Same code as before for UI setup)

        # Server socket setup
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 12345))  # Change port if needed
        self.server_socket.listen(5)

        # Accept connections in a separate thread
        threading.Thread(target=self.accept_connections).start()

    def accept_connections(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break

                # Handle the received data (implement your logic here)
                user_input = data.decode("utf-8")
                self.handle_user_input(user_input)

            except ConnectionResetError:
                break

    def handle_user_input(self, user_input):
        # Implement your logic to handle user input here
        print(f"Received user input: {user_input}")

if __name__ == '__main__':
    root = Tk()
    obj = Server(root)
    root.mainloop()
