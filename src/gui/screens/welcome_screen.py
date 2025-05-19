import tkinter as tk

class WelcomeScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, bg="#f0f0f0")
        self.controller = controller
        self.pack(expand=True)

        tk.Label(self, text="Wave 'Em Around", font=("Helvetica", 32, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Label(self, text="Welcome", font=("Helvetica", 24), bg="#f0f0f0").pack()
        tk.Label(self, text="To the Future of Audio Design", font=("Helvetica", 16), bg="#f0f0f0").pack(pady=10)

        tk.Button(self, text="Next", command=self.controller.show_login_screen).pack(pady=20)


