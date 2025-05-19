import tkinter as tk
from src.gui.app_controller import AppController


def main():
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()


