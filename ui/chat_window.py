import tkinter as tk

class ChatWindow:
    def __init__(self):
        self.window = tk.Tk()

        self.window.iconbitmap("assets/icons/aia.ico")
        self.window.title("Aia")
        self.window.geometry("420x600")
        self.window.configure(bg="#111111")
        self.window.resizable(False, False)
        self.window.attributes("-topmost", True)
        self.on_choice = None
        

        title = tk.Label(
            self.window,
            text="Aia",
            bg="#111111",
            fg="white",
            font=("Segoe UI", 16, "bold")
        )
        title.pack(pady=10)

        self.chat = tk.Text(
            self.window,
            bg="#111111",
            fg="white",
            insertbackground="white",
            wrap="word",
            state="disabled",
            relief="flat",
            font=("Segoe UI", 11),
            height=15
        )

        self.chat.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 5)
        )

        self.choice_frame = tk.Frame(
            self.window,
            bg="#111111"
        )

        self.choice_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.entry = tk.Entry(
            self.window,
            bg="#222222",
            fg="white",
            insertbackground="white",
            font=("Segoe UI", 11)
        )

        self.entry.pack(
            fill="x",
            padx=10,
            pady=(8,5)
        )

        self.button = tk.Button(
            self.window,
            text="Send",
            bg="#222222",
            fg="white",
            activebackground="#444444",
            command=self.send_message
        )

        self.button.pack(
            pady=(0,10)    
        )

        

        self.choice_buttons = []

        for i in range(4):
            button = tk.Button(
                self.choice_frame,
                text="",
                command=lambda index=i: self.choose(index)
            )

            button.pack(
                fill="x",
                pady=2
            )

            self.choice_buttons.append(button)

        self.entry.bind("<Return>", self.send_message)

    
    def add_ai_message(self, text):

        self.type_message("Aia: ", text)

    def show_choices(self, greetings):
        print("Mostrando:", greetings)

        self.greetings = greetings

        for button, greeting in zip(self.choice_buttons, greetings):

            button.config(
                text=greeting["option"],
                state="normal"
            )

    def choose(self, index):
        option = self.greetings[index]
        
        self.add_user_message(option["option"])

        self.add_ai_message(option["response"])

        for button in self.choice_buttons:
            button.config(state="disabled")

    def add_user_message(self, text):

        self.chat.config(state="normal")

        self.chat.insert(
            "end",
            f"You: {text}\n\n"
        )

        self.chat.config(state="disabled")
        self.chat.see("end")

    def send_message(self, event=None):

        text = self.entry.get().strip()

        if not text:
            return
        
        self.add_user_message(text)

        self.entry.delete(0, "end")

    def choose(self, index):
        option = self.greetings[index]

        self.add_user_message(option["option"])
        self.add_ai_message(option["response"])

        if self.on_choice:
            self.on_choice(index)

    def type_message(self, prefix, text):

        self.chat.config(state="normal")

        start = self.chat.index("end-1c")

        self.chat.insert("end", prefix)


        def typing(index=0):

            self.chat.delete(start + f"+{len(prefix)}c", "end-1c")
            self.chat.insert(start + f"+{len(prefix)}c", text[:index + 1])

            self.chat.see("end")

            if index < len(text):
                self.window.after(
                    50,
                    lambda: typing(index + 1)
                )
            else:
                self.chat.insert("end", "\n\n")
                self.chat.config(state="disabled")

        typing()

        
    
    def start(self):
        self.window.mainloop()
