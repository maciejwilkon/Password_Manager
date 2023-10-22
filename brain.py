import generator
import customtkinter as ctk
import home_screen

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


root = home_screen.HomeScreen(generator)
root.mainloop()
