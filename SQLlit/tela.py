from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw
from tkcalendar import DateEntry
from main import *

# ── Paleta ──────────────────────────────────────────────────────
BG        = "#0f1117"   # fundo principal
SURFACE   = "#1a1d27"   # cards / paineis
SURFACE2  = "#22263a"   # inputs / hover
ACCENT    = "#4f8ef7"   # azul primário
ACCENT2   = "#6c63ff"   # roxo secundário
DANGER    = "#ef4444"   # vermelho
SUCCESS   = "#22c55e"   # verde
TEXT      = "#f1f5f9"   # texto principal
TEXT2     = "#94a3b8"   # texto secundário
BORDER    = "#2e3347"   # bordas

# ── Janela ──────────────────────────────────────────────────────
janela = Tk()
janela.title("Sistema de Registro de Alunos")
janela.geometry("1000x680")
janela.configure(bg=BG)
janela.resizable(False, False)

# ── Estilo ttk ──────────────────────────────────────────────────
style = ttk.Style(janela)
style.theme_use("clam")

style.configure("Treeview",
    background=SURFACE, foreground=TEXT,
    fieldbackground=SURFACE, rowheight=32,
    font=("Segoe UI", 10), borderwidth=0)
style.configure("Treeview.Heading",
    background=SURFACE2, foreground=TEXT2,
    font=("Segoe UI", 9, "bold"), relief="flat")
style.map("Treeview",
    background=[("selected", ACCENT)],
    foreground=[("selected", TEXT)])
style.configure("Vertical.TScrollbar",
    background=SURFACE2, troughcolor=SURFACE,
    borderwidth=0, arrowsize=12)
style.configure("TCombobox",
    fieldbackground=SURFACE2, background=SURFACE2,
    foreground=TEXT, selectbackground=ACCENT,
    borderwidth=0, arrowcolor=TEXT2)
style.map("TCombobox",
    fieldbackground=[("readonly", SURFACE2)],
    foreground=[("readonly", TEXT)])
style.configure("DateEntry",
    fieldbackground=SURFACE2, background=SURFACE2,
    foreground=TEXT, borderwidth=0)

# ── Estado global ────────────────────────────────────────────────
imagem_string = "logo.png"
imagem_ref    = None   # mantém referência pra não ser coletado pelo GC

# ── Helpers ──────────────────────────────────────────────────────
def make_round_image(path, size=(120, 120)):
    img  = Image.open(path).resize(size, Image.LANCZOS).convert("RGBA")
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, *size), fill=255)
    img.putalpha(mask)
    return ImageTk.PhotoImage(img)

def label(parent, text, fg=TEXT2, font=("Segoe UI", 9), **kw):
    return Label(parent, text=text, fg=fg, bg=parent["bg"],
                 font=font, **kw)

def entry(parent, width=24):
    e = Entry(parent, width=width, font=("Segoe UI", 10),
              bg=SURFACE2, fg=TEXT, insertbackground=TEXT,
              relief="flat", bd=0, highlightthickness=1,
              highlightbackground=BORDER, highlightcolor=ACCENT)
    return e

def rounded_btn(parent, text, command, color=ACCENT, fg=TEXT,
                width=16, font_size=9):
    btn = Button(parent, text=text, command=command,
                 bg=color, fg=fg, activebackground=color,
                 activeforeground=fg, font=("Segoe UI", font_size, "bold"),
                 width=width, relief="flat", bd=0, cursor="hand2",
                 pady=7)
    btn.bind("<Enter>", lambda e: btn.config(bg=_lighten(color)))
    btn.bind("<Leave>", lambda e: btn.config(bg=color))
    return btn

def _lighten(hex_color):
    r = min(255, int(hex_color[1:3], 16) + 20)
    g = min(255, int(hex_color[3:5], 16) + 20)
    b = min(255, int(hex_color[5:7], 16) + 20)
    return f"#{r:02x}{g:02x}{b:02x}"

def exibir_imagem(caminho):
    global imagem_ref, imagem_string
    imagem_string = caminho
    try:
        imagem_ref = make_round_image(caminho)
    except Exception:
        imagem_ref = make_round_image("logo.png")
        imagem_string = "logo.png"
    l_imagem.config(image=imagem_ref)
    l_imagem.image = imagem_ref

def limpar_campos():
    for w in [e_nome, e_email, e_tel, e_endereco]:
        w.delete(0, END)
    for cb in [c_sexo, c_curso]:
        cb.set("")
    data_nascimento.set_date("2000-01-01")

def validar_id():
    val = e_procurar.get().strip()
    if not val:
        messagebox.showerror("Erro", "Informe o ID do aluno.")
        return None
    try:
        return int(val)
    except ValueError:
        messagebox.showerror("Erro", "ID inválido.")
        return None

# ── Layout principal ─────────────────────────────────────────────
# Sidebar esquerda
sidebar = Frame(janela, bg=SURFACE, width=220)
sidebar.pack(side=LEFT, fill=Y, padx=0, pady=0)
sidebar.pack_propagate(False)

# Área principal
main_area = Frame(janela, bg=BG)
main_area.pack(side=LEFT, fill=BOTH, expand=True)

# Formulário + foto (topo)
form_frame = Frame(main_area, bg=SURFACE, pady=20, padx=20)
form_frame.pack(fill=X, padx=16, pady=(16, 8))

# Tabela (baixo)
table_frame = Frame(main_area, bg=SURFACE)
table_frame.pack(fill=BOTH, expand=True, padx=16, pady=(0, 16))

# ── Sidebar: logo + título ────────────────────────────────────────
try:
    _lg = Image.open("logo.png").resize((54, 54))
    _lg = ImageTk.PhotoImage(_lg)
    Label(sidebar, image=_lg, bg=SURFACE).pack(pady=(28, 6))
    sidebar._lg = _lg
except Exception:
    pass

Label(sidebar, text="EduRegister", fg=TEXT,
      bg=SURFACE, font=("Segoe UI", 13, "bold")).pack()
Label(sidebar, text="Sistema de Alunos", fg=TEXT2,
      bg=SURFACE, font=("Segoe UI", 8)).pack(pady=(0, 24))

Frame(sidebar, bg=BORDER, height=1).pack(fill=X, padx=16, pady=4)

# ── Sidebar: busca ────────────────────────────────────────────────
Label(sidebar, text="BUSCAR ALUNO", fg=TEXT2, bg=SURFACE,
      font=("Segoe UI", 8, "bold")).pack(pady=(20, 4), padx=16, anchor=W)

search_row = Frame(sidebar, bg=SURFACE)
search_row.pack(fill=X, padx=16, pady=4)

e_procurar = Entry(search_row, width=7, font=("Segoe UI", 10),
                   bg=SURFACE2, fg=TEXT, insertbackground=TEXT,
                   relief="flat", bd=0, highlightthickness=1,
                   highlightbackground=BORDER, highlightcolor=ACCENT)
e_procurar.pack(side=LEFT, padx=(0, 6), pady=4, ipady=5, fill=X, expand=True)

rounded_btn(search_row, "→", lambda: procurar(),
            color=ACCENT, width=3).pack(side=LEFT, pady=4)

Frame(sidebar, bg=BORDER, height=1).pack(fill=X, padx=16, pady=16)

# ── Sidebar: botões CRUD ──────────────────────────────────────────
Label(sidebar, text="AÇÕES", fg=TEXT2, bg=SURFACE,
      font=("Segoe UI", 8, "bold")).pack(pady=(0, 8), padx=16, anchor=W)

def _side_btn(text, cmd, color=SURFACE2, fg=TEXT):
    f = Frame(sidebar, bg=SURFACE)
    f.pack(fill=X, padx=16, pady=3)
    b = Button(f, text=text, command=cmd, bg=color, fg=fg,
               activebackground=_lighten(color), activeforeground=fg,
               font=("Segoe UI", 10), width=20, relief="flat",
               bd=0, cursor="hand2", pady=8, anchor=W, padx=12)
    b.pack(fill=X)
    b.bind("<Enter>", lambda e: b.config(bg=_lighten(color)))
    b.bind("<Leave>", lambda e: b.config(bg=color))
    return b

btn_adicionar = _side_btn("＋  Adicionar", lambda: adicionar(), ACCENT)
btn_atualizar = _side_btn("✎  Atualizar",  lambda: atualizar(), ACCENT2)
btn_deletar   = _side_btn("✕  Deletar",    lambda: deletar(),   DANGER)

Frame(sidebar, bg=BORDER, height=1).pack(fill=X, padx=16, pady=16)

# ── Foto do aluno (sidebar inferior) ─────────────────────────────
Label(sidebar, text="FOTO DO ALUNO", fg=TEXT2, bg=SURFACE,
      font=("Segoe UI", 8, "bold")).pack(pady=(0, 8), padx=16, anchor=W)

try:
    imagem_ref = make_round_image("logo.png")
except Exception:
    imagem_ref = None

l_imagem = Label(sidebar, image=imagem_ref, bg=SURFACE)
l_imagem.image = imagem_ref
l_imagem.pack(pady=(0, 8))

foto_row = Frame(sidebar, bg=SURFACE)
foto_row.pack(fill=X, padx=16)

def escolher_imagem():
    caminho = fd.askopenfilename(
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif")])
    if caminho:
        exibir_imagem(caminho)

def remover_imagem():
    exibir_imagem("logo.png")

Button(foto_row, text="Carregar", command=escolher_imagem,
       bg=SURFACE2, fg=TEXT2, activebackground=BORDER, activeforeground=TEXT,
       font=("Segoe UI", 8), relief="flat", bd=0, cursor="hand2",
       pady=5, padx=8).pack(side=LEFT, expand=True, fill=X, padx=(0, 4))

Button(foto_row, text="Remover", command=remover_imagem,
       bg=SURFACE2, fg=DANGER, activebackground=BORDER, activeforeground=DANGER,
       font=("Segoe UI", 8), relief="flat", bd=0, cursor="hand2",
       pady=5, padx=8).pack(side=LEFT, expand=True, fill=X)

# ── Formulário: grid de campos ────────────────────────────────────
Label(form_frame, text="Dados do Aluno", fg=TEXT,
      bg=SURFACE, font=("Segoe UI", 12, "bold")).grid(
      row=0, column=0, columnspan=6, sticky=W, pady=(0, 14))

def campo(parent, row, col, label_text, widget):
    Label(parent, text=label_text, fg=TEXT2, bg=SURFACE,
          font=("Segoe UI", 8, "bold")).grid(
          row=row, column=col, sticky=W, pady=(0, 2), padx=(0, 16))
    widget.grid(row=row+1, column=col, sticky=W, pady=(0, 12),
                padx=(0, 16), ipady=5)

e_nome     = entry(form_frame, 22)
e_email    = entry(form_frame, 22)
e_tel      = entry(form_frame, 14)
e_endereco = entry(form_frame, 18)

c_sexo = ttk.Combobox(form_frame, width=6,
    font=("Segoe UI", 10), justify="center", state="readonly")
c_sexo["values"] = ("M", "F")

c_curso = ttk.Combobox(form_frame, width=16,
    font=("Segoe UI", 10), justify="center", state="readonly")
c_curso["values"] = ("Engenharia", "Medicina", "T.I.", "Designer", "Outros")

data_nascimento = DateEntry(form_frame, width=14,
    font=("Segoe UI", 10), justify="center",
    background=ACCENT, foreground=TEXT,
    borderwidth=0, year=2000,
    headersbackground=ACCENT, headersforeground=TEXT,
    selectbackground=ACCENT, selectforeground=TEXT,
    normalbackground=SURFACE2, normalforeground=TEXT,
    weekendbackground=SURFACE2, weekendforeground=TEXT2,
    othermonthbackground=SURFACE, othermonthforeground=TEXT2)

campo(form_frame, 1, 0, "NOME",              e_nome)
campo(form_frame, 1, 1, "EMAIL",             e_email)
campo(form_frame, 1, 2, "TELEFONE",          e_tel)
campo(form_frame, 3, 0, "ENDEREÇO",          e_endereco)
campo(form_frame, 3, 1, "CURSO",             c_curso)
campo(form_frame, 3, 2, "DATA NASCIMENTO",   data_nascimento)
campo(form_frame, 3, 3, "SEXO",              c_sexo)

# ── Tabela ────────────────────────────────────────────────────────
cols = ["ID", "Nome", "Email", "Telefone", "Sexo", "Nascimento", "Endereço", "Curso"]

Label(table_frame, text="Alunos Cadastrados", fg=TEXT,
      bg=SURFACE, font=("Segoe UI", 11, "bold")).pack(
      anchor=W, padx=16, pady=(12, 6))

tree_container = Frame(table_frame, bg=SURFACE)
tree_container.pack(fill=BOTH, expand=True, padx=16, pady=(0, 16))

tree = ttk.Treeview(tree_container, columns=cols,
                    show="headings", selectmode="browse")

widths = [40, 130, 150, 80, 50, 90, 120, 90]
for col, w in zip(cols, widths):
    tree.heading(col, text=col)
    tree.column(col, width=w, anchor=CENTER if w <= 90 else W)

vsb = ttk.Scrollbar(tree_container, orient=VERTICAL, command=tree.yview)
hsb = ttk.Scrollbar(tree_container, orient=HORIZONTAL, command=tree.xview)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(row=0, column=0, sticky=NSEW)
vsb.grid(row=0, column=1, sticky=NS)
hsb.grid(row=1, column=0, sticky=EW)
tree_container.rowconfigure(0, weight=1)
tree_container.columnconfigure(0, weight=1)

# ── CRUD ──────────────────────────────────────────────────────────
def mostrar_aluno():
    for row in tree.get_children():
        tree.delete(row)
    for item in sistema_de_registro.view_all_students():
        tree.insert("", END, values=item[:-1])

def adicionar():
    nome     = e_nome.get().strip()
    email    = e_email.get().strip()
    tel      = e_tel.get().strip()
    sexo     = c_sexo.get()
    data     = data_nascimento.get()
    endereco = e_endereco.get().strip()
    curso    = c_curso.get()
    img      = imagem_string

    if any(v == "" for v in [nome, email, tel, sexo, data, endereco, curso]):
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    sistema_de_registro.register_estudent(
        [nome, email, tel, sexo, data, endereco, curso, img])
    limpar_campos()
    exibir_imagem("logo.png")
    mostrar_aluno()

def procurar():
    id_aluno = validar_id()
    if id_aluno is None:
        return
    dados = sistema_de_registro.search_student(id_aluno)
    if not dados:
        messagebox.showerror("Erro", f"Aluno ID {id_aluno} não encontrado.")
        return
    limpar_campos()
    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    c_sexo.set(dados[4])
    data_nascimento.set_date(dados[5])
    e_endereco.insert(END, dados[6])
    c_curso.set(dados[7])
    try:
        exibir_imagem(dados[8])
    except FileNotFoundError:
        exibir_imagem("logo.png")

def atualizar():
    id_aluno = validar_id()
    if id_aluno is None:
        return
    nome     = e_nome.get().strip()
    email    = e_email.get().strip()
    tel      = e_tel.get().strip()
    sexo     = c_sexo.get()
    data     = data_nascimento.get()
    endereco = e_endereco.get().strip()
    curso    = c_curso.get()
    img      = imagem_string

    if any(v == "" for v in [nome, email, tel, sexo, data, endereco, curso]):
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    sistema_de_registro.update_students(
        [nome, email, tel, sexo, data, endereco, curso, img, id_aluno])
    limpar_campos()
    exibir_imagem("logo.png")
    mostrar_aluno()

def deletar():
    id_aluno = validar_id()
    if id_aluno is None:
        return
    if not messagebox.askyesno("Confirmar", f"Deletar aluno ID {id_aluno}?"):
        return
    sistema_de_registro.delete_student(id_aluno)
    limpar_campos()
    e_procurar.delete(0, END)
    exibir_imagem("logo.png")
    mostrar_aluno()

mostrar_aluno()
janela.mainloop()