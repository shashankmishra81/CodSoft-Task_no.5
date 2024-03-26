import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.master, text="Name:").grid(row=0, column=0)
        tk.Label(self.master, text="Phone:").grid(row=1, column=0)
        tk.Label(self.master, text="Email:").grid(row=2, column=0)

        # Entry Boxes
        tk.Entry(self.master, textvariable=self.name_var).grid(row=0, column=1)
        tk.Entry(self.master, textvariable=self.phone_var).grid(row=1, column=1)
        tk.Entry(self.master, textvariable=self.email_var).grid(row=2, column=1)

        # Buttons
        tk.Button(self.master, text="Add Contact", command=self.add_contact).grid(row=3, column=0, columnspan=2)
        tk.Button(self.master, text="Clear", command=self.refresh_list).grid(row=4, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()

        if not name or not phone or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        messagebox.showinfo("Success", f"Contact added: \nName: {name} \nPhone: {phone} \nEmail: {email}")
    def refresh_list(self):
        self.contact_listbox.delete(0,tk.END)
        for contact in self.contacts():
            self.contact_listbox.insert(tk.END, f"{contact[0]}-{contact[1]}")
def main():
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
if __name__ == "__main__":
    main()
