import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.com = sqlite3.connect('estudante.db')
        self.c = self.com.cursor()
        self.creat_table()
        
    def creat_table(self):
        self.c.execute()