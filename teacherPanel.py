import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from database import Database

class TeacherPanel:
    def __init__(self, parent, db):
        self.db = db
        self.frame = ttk.Frame(parent)

        ttk.Label(self.frame, text="Teacher Panel", font=("Arial", 16)).pack(pady=10)

        login_frame = ttk.Frame(self.frame)
        login_frame.pack(pady=10)

        ttk.Label(login_frame, text="Username:").pack()
        self.username_entry = ttk.Entry(login_frame)
        self.username_entry.pack()

        ttk.Label(login_frame, text="Password:").pack()
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.pack()

        self.login_button = ttk.Button(login_frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.username_entry.bind("<Return>", lambda event: self.password_entry.focus())
        self.password_entry.bind("<Return>", self.login)

    def login(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.db.cursor.execute("SELECT * FROM teachers WHERE username = ? AND password = ?", (username, password))
        teacher = self.db.cursor.fetchone()

        if teacher:
            messagebox.showinfo("Login Successful", f"Welcome, {teacher[1]}!")
            self.teacher_id = teacher[0]
            self.teacher_actions_window()
        else:
            messagebox.showerror("Login Failed", "No such username or password!")

    def teacher_actions_window(self):
        teacher_window = tk.Toplevel(self.frame)
        teacher_window.title("Teacher Actions")
        teacher_window.geometry("1280x720")

        ttk.Label(teacher_window, text="Courses").pack(pady=10)

        tree = ttk.Treeview(teacher_window, columns=("ID", "Course Name"), show="headings")
        tree.heading("ID", text="Course ID")
        tree.heading("Course Name", text="Course Name")

        self.db.cursor.execute("SELECT id, name FROM courses WHERE teacher_id = ?", (self.teacher_id,))
        courses = self.db.cursor.fetchall()

        for course in courses:
            tree.insert("", "end", values=(course[0], course[1]))

        tree.pack(pady=10)