import tkinter as tk
from src.potent_gui import AudioGestureApp

def main():
    root = tk.Tk()
    app = AudioGestureApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
     