import tkinter as tk
from src.gui.screens.welcome_screen import WelcomeScreen
from src.gui.screens.login_screen import LoginScreen
from src.gui.screens.main_screen import MainScreen

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("Wave 'Em Around")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")

        self.current_screen = None
        self.selected_song_path = None

        self.show_welcome_screen()

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()

    def show_welcome_screen(self):
        self.clear_screen()
        self.current_screen = WelcomeScreen(self.root, self)

    def show_login_screen(self):
        self.clear_screen()
        self.current_screen = LoginScreen(self.root, self)

    def show_main_screen(self):
        self.clear_screen()
        self.current_screen = MainScreen(self.root, self)


