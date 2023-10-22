import customtkinter as ctk
import random


letters_low = list('qwertyuiopasdfghjklzxcvbnm')
letters_cap = [x.upper() for x in letters_low]
numbers = list('1234567890')
special_chars = list("!@#$%^&*()-_=+[]{};:,.<>/?")


class Generator(ctk.CTk):
    def __init__(self, password, user_password):
        super().__init__()
        self.geometry('400x310')
        self.title('Generator')

        self.ll_label = ctk.CTkLabel(self, text='lower letters')
        self.ll_label.grid(row=0, column=0, pady=(10, 0))
        self.ll_entry = ctk.CTkEntry(self, placeholder_text='how many?')
        self.ll_checkbox = ctk.CTkCheckBox(self, text='', command=lambda: self.ll_entry.grid(row=1, column=1))
        self.ll_checkbox.grid(row=1, column=0, padx=(75, 0))

        self.cl_label = ctk.CTkLabel(self, text='capital letters')
        self.cl_label.grid(row=2, column=0, pady=(10, 0))
        self.cl_entry = ctk.CTkEntry(self, placeholder_text='how many?')
        self.cl_checkbox = ctk.CTkCheckBox(self, text='', command=lambda: self.cl_entry.grid(row=3, column=1))
        self.cl_checkbox.grid(row=3, column=0, padx=(75, 0))

        self.n_label = ctk.CTkLabel(self, text='numbers')
        self.n_label.grid(row=4, column=0, pady=(10, 0))
        self.n_entry = ctk.CTkEntry(self, placeholder_text='how many?')
        self.n_checkbox = ctk.CTkCheckBox(self, text='', command=lambda: self.n_entry.grid(row=5, column=1))
        self.n_checkbox.grid(row=5, column=0, padx=(75, 0))

        self.sc_label = ctk.CTkLabel(self, text='special characters')
        self.sc_label.grid(row=6, column=0, pady=(10, 0))
        self.sc_entry = ctk.CTkEntry(self, placeholder_text='how many?')
        self.sc_checkbox = ctk.CTkCheckBox(self, text='', command=lambda: self.sc_entry.grid(row=7, column=1))
        self.sc_checkbox.grid(row=7, column=0, padx=(75, 0))

        self.button = ctk.CTkButton(self, text='submit', hover_color='green',
                                    command=lambda: self.generate_password(password, user_password))
        self.button.grid(row=8, column=1, pady=(10, 0))

    def generate_password(self, password, user_password):
        ll = self.ll_entry.get()
        cl = self.cl_entry.get()
        n = self.n_entry.get()
        sc = self.sc_entry.get()
        if self.ll_checkbox.get() == 0:
            ll = 0
        if self.cl_checkbox.get() == 0:
            cl = 0
        if self.n_checkbox.get() == 0:
            n = 0
        if self.sc_checkbox.get() == 0:
            sc = 0
        try:
            a = random.choices(letters_low, k=int(ll))
            b = random.choices(letters_cap, k=int(cl))
            c = random.choices(numbers, k=int(n))
            d = random.choices(special_chars, k=int(sc))
            password.extend(a)
            password.extend(b)
            password.extend(c)
            password.extend(d)
            random.shuffle(password)
            final_password = "".join(password)
            password.clear()
            info_win = ctk.CTk()
            info_win.geometry("300x80")
            info_label = ctk.CTkLabel(info_win, text=f"Created password is: {final_password}")
            info_label.pack(pady=20, padx=20)
            user_password.insert(index=0, string=final_password)
            info_win.mainloop()

        except ValueError:
            print("Insert numbers only!")
