import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.com = sqlite3.connect('estudante.db')
        self.c = self.com.cursor()
        self.create_table() 
        
    def create_table(self): 
        self.c.execute(''' CREATE TABLE IF NOT EXISTS estudantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                tel TEXT NOT NULL,
                sexo TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                endereco TEXT NOT NULL,
                curso TEXT NOT NULL,
                picture TEXT NOT NULL) ''')
        
        def register_estudent(self, estudantes):
            self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (estudantes))
        self.com.commit()

        #mostrando mensagem de suscesso
        messagebox.showinfo('sucesso', 'Registro com sucesso!')
        
        def view_all_students(self):
            self.c.execut("SELECT * FROM estudantes")
            dados = self.c.fetchall()
            for i in dados:
                print(f'ID : {i[0]} | Nome : {i[1]} | Email: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Data de nascimento: {i[5]} | Endereco: {i[6]} | Curso: {i[7]} | Picture: {i[8]}')