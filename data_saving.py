import json
import os
import customtkinter as ctk


def check_for_file(file_name):
    return os.path.exists(file_name)


def data_saved_info():
    sc = ctk.CTk()
    sc.geometry('200x100')
    sc.title("Data Feedback")
    info_label = ctk.CTkLabel(sc, text="Data successfully saved!")
    info_label.pack(pady=20, padx=20)
    sc.mainloop()


def save_data(username, password):
    if check_for_file("database.json"):
        with open("database.json") as fp:
            data = json.load(fp)
        data.append({"username": username, "password": password})
        with open("database.json", "w") as json_file:
            json.dump(data, json_file, indent=4, separators=(",", ": "))
        data.clear()
        data_saved_info()
    else:
        data = [{"username": username, "password": password}]
        with open("database.json", "w") as json_file:
            json.dump(data, json_file, indent=4, separators=(",", ": "))
        data.clear()
        data_saved_info()


def searching_input_dialog():
    dialog_win = ctk.CTk()
    dialog_win.title("Data Search")
    dialog_win.geometry("200x100")
    input_entry = ctk.CTkEntry(dialog_win, placeholder_text="Type username")
    input_entry.pack(pady=20, padx=20)
    search_button = ctk.CTkButton(dialog_win, text="Search", command=lambda: read_data(input_entry.get()))
    search_button.pack(padx=20)
    dialog_win.mainloop()


def read_data(username):
    database_display = ctk.CTkToplevel()
    data_textbox = ctk.CTkTextbox(database_display, 300, 300)
    if check_for_file("database.json"):
        if username == 'all':
            texts = ""
            with open("database.json") as fp:
                data = json.load(fp)
                for i in data:
                    string = f"username: {i['username']} --> password: {i['password']}"
                    texts += string + "\n"
            data_textbox.insert("0.0", texts)
            data_textbox.pack()
        else:
            with open("database.json") as fp:
                data = json.load(fp)
                for i in data:
                    if i['username'] == username:
                        texts = f"username: {i['username']} --> password: {i['password']}"
                        data_textbox.configure(width=300, height=100)
                        data_textbox.insert("0.0", texts)
                        data_textbox.pack()
                        break
                    else:
                        pass

                def find_user(my_list, user):
                    for item in my_list:
                        if 'username' in item and item['username'] == user:
                            return True
                    return False
                result = find_user(data, username)
                if result is False:
                    data_textbox.configure(width=150, height=50)
                    data_textbox.insert("0.0", "No such user found.")
                    data_textbox.pack()
        database_display.mainloop()

    else:
        data_textbox.configure(width=300, height=100)
        data_textbox.insert("0.0", "No database found. Save your first data to create one.")
        data_textbox.pack()
        database_display.mainloop()


def deleting_input_dialog():
    dialog_win = ctk.CTk()
    dialog_win.title("Data Delete")
    dialog_win.geometry("200x100")
    input_entry = ctk.CTkEntry(dialog_win, placeholder_text="Type username")
    input_entry.pack(pady=20, padx=20)
    search_button = ctk.CTkButton(dialog_win, text="Delete", command=lambda: delete_user(input_entry.get()))
    search_button.pack(padx=20)
    dialog_win.mainloop()


def delete_user(username):
    database_display = ctk.CTkToplevel()
    data_textbox = ctk.CTkTextbox(database_display, 300, 300)
    with open("database.json", "r+") as fp:
        data = json.load(fp)
        user_found = False
        for i in data:
            if i.get('username') == username:
                data.remove(i)
                data_textbox.configure(width=300, height=100)
                data_textbox.insert("0.0", f"Data for user {username} deleted successfully!")
                data_textbox.pack()
                user_found = True
                break
        with open("database.json", "w") as file:
            json.dump(data, file, indent=2)

        if not user_found:
            data_textbox.configure(width=150, height=50)
            data_textbox.insert("0.0", "No such user found.")
            data_textbox.pack()
    database_display.mainloop()
