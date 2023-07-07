import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import datetime

CONFIG_FILE = "config.txt"

class MorningCheckInApp:
    def __init__(self, master):
        self.master = master
        master.title("Morning Check-in App")

        self.smtp_server = ""
        self.smtp_port = ""
        self.email_address = ""
        self.email_password = ""

        self.load_smtp_details()

        self.prompts = [
            "What is the most important task to accomplish today?",
            "How can I proactively prevent distractions?",
            "How will I recognize if I succeed?",
            "What would be my well-deserved reward?"
        ]

        self.create_interface()

    def create_interface(self):
        self.entries = []

        def focus_next_entry(event):
            event.widget.tk_focusNext().focus()
            return "break"

        for i, prompt in enumerate(self.prompts):
            prompt_label = tk.Label(self.master, text=prompt)
            prompt_label.grid(row=i*2, column=1, padx=5, pady=5)

            entry = tk.Text(self.master, height=4, width=50)
            entry.grid(row=i*2+1, column=1, padx=10, pady=10)
            entry.bind("<Tab>", focus_next_entry)
            self.entries.append(entry)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_responses)
        self.submit_button.grid(row=len(self.prompts)*2+1, column=1, padx=10, pady=10)

        self.smtp_button = tk.Button(self.master, text="SMTP Details", command=self.input_smtp_details)
        self.smtp_button.grid(row=len(self.prompts)*2+1, column=0, padx=10, pady=10)

        self.email_button = tk.Button(self.master, text="Email Details", command=self.input_email_details)
        self.email_button.grid(row=len(self.prompts)*2+1, column=2, padx=10, pady=10)

    def load_smtp_details(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                config = file.readlines()
                if len(config) >= 4:
                    self.smtp_server = config[0].strip()
                    self.smtp_port = int(config[1].strip())
                    self.email_address = config[2].strip()
                    self.email_password = config[3].strip()

    def save_smtp_details(self):
        if all([self.smtp_server, self.smtp_port, self.email_address, self.email_password]):
            config = [
                self.smtp_server,
                str(self.smtp_port),
                self.email_address,
                self.email_password
            ]

            with open(CONFIG_FILE, "w") as file:
                file.write("\n".join(config))

    def input_email_details(self):
        self.create_email_details_window()

    def create_email_details_window(self):
        self.email_details_window = tk.Toplevel(self.master)
        self.email_details_window.title("Email Details")

        email_label = tk.Label(self.email_details_window, text="Email Address:")
        email_label.grid(row=0, column=0)
        self.email_address_entry = tk.Entry(self.email_details_window)
        self.email_address_entry.grid(row=0, column=1)
        self.email_address_entry.insert(0, self.email_address or "")

        password_label = tk.Label(self.email_details_window, text="Email Password:")
        password_label.grid(row=1, column=0)
        self.email_password_entry = tk.Entry(self.email_details_window, show="*")
        self.email_password_entry.grid(row=1, column=1)
        self.email_password_entry.insert(0, self.email_password or "")

        save_button = tk.Button(
            self.email_details_window,
            text="Save Email Details",
            command=self.save_input_email_details
        )
        save_button.grid(row=2, column=0, columnspan=2)

    def input_smtp_details(self):
        self.create_smtp_details_window()

    def create_smtp_details_window(self):
        self.smtp_details_window = tk.Toplevel(self.master)
        self.smtp_details_window.title("SMTP Details")

        server_label = tk.Label(self.smtp_details_window, text="SMTP Server:")
        server_label.grid(row=0, column=0)
        self.smtp_server_entry = tk.Entry(self.smtp_details_window)
        self.smtp_server_entry.grid(row=0, column=1)
        self.smtp_server_entry.insert(0, self.smtp_server or "")

        port_label = tk.Label(self.smtp_details_window, text="SMTP Port:")
        port_label.grid(row=1, column=0)
        self.smtp_port_entry = tk.Entry(self.smtp_details_window)
        self.smtp_port_entry.grid(row=1, column=1)
        self.smtp_port_entry.insert(0, self.smtp_port or "")

        save_button = tk.Button(
            self.smtp_details_window,
            text="Save SMTP Details",
            command=self.save_input_smtp_details
        )
        save_button.grid(row=2, column=0, columnspan=2)

    def save_input_email_details(self):
        self.email_address = self.email_address_entry.get()
        self.email_password = self.email_password_entry.get()
        self.save_smtp_details()
        self.email_details_window.destroy()

    def save_input_smtp_details(self):
        self.smtp_server = self.smtp_server_entry.get()
        self.smtp_port = self.smtp_port_entry.get()
        self.save_smtp_details()
        self.smtp_details_window.destroy()

    def submit_responses(self):
        if all(entry.get("1.0", "end").strip() for entry in self.entries):
            response_text = ""
            for i, entry in enumerate(self.entries):
                prompt = f"{i+1}. {self.prompts[i]}"
                response = entry.get("1.0", "end").strip()
                response_text += f"{prompt}\n{response}\n\n"
            self.send_email(response_text)
            messagebox.showinfo("Success", "Your responses have been emailed!")
        else:
            messagebox.showerror("Error", "Please fill out all the responses before submitting.")

    def send_email(self, response_text):
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = self.email_address

        current_date = datetime.date.today().strftime('%Y-%m-%d')
        msg['Subject'] = f"Morning Check-in Responses for {current_date}"

        body = response_text
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(msg['From'], self.email_password)
        text = msg.as_string()
        server.sendmail(msg['From'], msg['To'], text)
        server.quit()

root = tk.Tk()
app = MorningCheckInApp(root)
root.mainloop()
