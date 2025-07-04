import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
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
      self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)",
                           (estudantes))
      self.conn.commit()

      #mostrando mensagem de suscesso
      messagebox.showinfo('sucesso', 'Registro com sucesso!')
        
    def view_all_students(self):
      self.c.execute("SELECT * FROM estudantes")
      dados = self.c.fetchall()

      for i in dados:
           print(f'ID : {i[0]} | Nome : {i[1]} | Email: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Data de nascimento: {i[5]} | Endereco: {i[6]} | Curso: {i[7]} | Picture: {i[8]}')

    def search_student(self, id):
     self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
     dados = self.c.fetchone()

     print(f'ID : {dados[0]} | Nome : {dados[1]} | Email: {dados[2]} | Tel: {dados[3]} | Sexo: {dados[4]} | Data de nascimento: {dados[5]} | Endereco: {dados[6]} | Curso: {dados[7]} | Picture: {dados[8]}')


    def update_students(self, nova_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?,  curso=?, picture=? WHERE id=? "
        self.c.execute(query,nova_valores)
        self.conn.commit()

        #mostrando mensagem de suscesso
        messagebox.showinfo('sucesso', f'Estudante com ID:{nova_valores[8]} Foi atualizado!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

          #mostrando mensagem de suscesso
        messagebox.showinfo('sucesso', f'Estudante com ID:{id} Foi Deletado!')
    
#Criando uma instancia do sistema de registro
sistema_de_registro = SistemaDeRegistro()

#informacoes
#estudante = ('elena', 'elena@gmail.com', '4321', 'M', '18/05/2007', 'angola', 'enfermagem', "imagem2.png")

#sistema_de_registro.register_estudent(estudante)

# Ver estudantes
#todos_alunos = sistema_de_registro.view_all_students()

# procurar aluno
#aluno = sistema_de_registro.search_student(2)

# Atualizar aluno
#estudante = ('elena', 'elena@gmail.com', '555', 'F', '18/05/2007', 'angola', 'enfermagem', "imagem2.png", 2)
#aluno = sistema_de_registro.update_students(estudante)

sistema_de_registro.delete_student(1)

# ver estudante
todos_alunos = sistema_de_registro.view_all_students()