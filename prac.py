import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
import random
import time
import datetime
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        #=====================title=====================================
        title = tk.Label(self.root, text="Student Management System", font=("times new roman", 40, "bold"), bg="yellow", fg="red", bd=10, relief=tk.GROOVE)
        title.pack(side=tk.TOP, fill=tk.X)

        #=====================variable=====================
        self.roll_no_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.branch_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.search_by = tk.StringVar()
        self.search_txt = tk.StringVar()

        #=====================manage frame=====================
        Manage_Frame = tk.Frame(self.root, bd=4, relief=tk.RAISED, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title = tk.Label(Manage_Frame, text="Manage Student", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = tk.Label(Manage_Frame, text="Roll No.", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_roll = tk.Entry(Manage_Frame, textvariable=self.roll_no_var, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")
        lbl_name = tk.Label(Manage_Frame, text="Name", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = tk.Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        lbl_course = tk.Label(Manage_Frame, text="Course", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_course.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_course = tk.Entry(Manage_Frame, textvariable=self.course_var, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_course.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        lbl_branch = tk.Label(Manage_Frame, text="Branch", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_branch.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_branch = tk.Entry(Manage_Frame, textvariable=self.branch_var, font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_branch.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        lbl_gender = tk.Label(Manage_Frame, text="Gender", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"), state="readonly")
        combo_gender['values'] = ("Male", "Female")
        combo_gender.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        lbl_dob = tk.Label(Manage_Frame, text="D.O.B", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        