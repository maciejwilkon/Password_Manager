import customtkinter as ctk
import data_saving


class HomeScreen(ctk.CTk):
    def __init__(self, generator):
        super().__init__()
        self.geometry('400x200')
        self.title('Password manager')

        self.username = ctk.CTkEntry(self, width=300, placeholder_text='username/email')
        self.username.grid(row=0, column=0, columnspan=2, pady=(50, 0), padx=(50, 0))

        self.user_password = ctk.CTkEntry(self, width=300, placeholder_text='Enter password')
        self.user_password.grid(row=1, column=0, columnspan=2, pady=(10, 0), padx=(50, 0))

        self.generator_button = ctk.CTkButton(self, text='Generate password', hover_color='green',
                                              command=lambda: self.generating(generator))
        self.generator_button.grid(row=2, column=0, pady=(10, 0), padx=(50, 0))

        self.delete_button = ctk.CTkButton(self, text='Delete data', hover_color='red',
                                           command=lambda: data_saving.deleting_input_dialog())
        self.delete_button.grid(row=2, column=1, pady=(10, 0), padx=(5, 0))

        self.data_button = ctk.CTkButton(self, text='Display data', hover_color='orange',
                                         command=lambda: data_saving.searching_input_dialog())
        self.data_button.grid(row=3, column=1, pady=(10, 0), padx=(5, 0))

        self.save_button = ctk.CTkButton(self, text='Save', hover_color='green',
                                         command=lambda:
                                         data_saving.save_data(self.username.get(), self.user_password.get()))
        self.save_button.grid(row=3, column=0, pady=(10, 0), padx=(50, 0))

    def generating(self, generator):
        password = []
        gene = generator.Generator(password, self.user_password)
        gene.mainloop()
