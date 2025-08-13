
  #  Sistema de Registro de Alunos
Este é um projeto educacional desenvolvido 100% em Python, com o objetivo de simular um sistema real de cadastro e gerenciamento de alunos, trabalhando com conceitos fundamentais da programação.

A ideia é construir, do zero, um sistema funcional com interface de texto (CLI), capaz de armazenar, exibir, buscar e remover dados de alunos, com persistência em arquivo local.

## O que é e como funciona

Este é um sistema com interface de texto (CLI) que permite:

- **Cadastrar alunos** com nome, matrícula, idade e curso.
- **Listar todos os alunos** registrados.
- **Buscar um aluno específico** por nome ou matrícula.
- **Remover alunos** do cadastro, com confirmação prévia.
- **Salvar os dados** automaticamente em arquivos locais no formato `.txt` ou `.csv`.

Ele foi construído com uma linguagem simples, ideal para quem está começando a programar.

---

## Tecnologias e conceitos aplicados

- **Python 3** – Linguagem principal utilizada.  
- **Programação Orientada a Objetos (POO)** – Para organizar o código em classes e métodos.  
- **Manipulação de arquivos** (`.txt / .csv`) – Leitura, escrita e persistência dos registros.  
- **Menus interativos** usando `input()` e loops `while`.  
- **Estruturas de decisão** com `if` e `else`.  
- **Tratamento de exceções** com `try/except` para evitar erros durante a execução.  
- **Modularização do código** em arquivos `.py` separados.  
- **Formatação com f-strings** para imprimir e salvar dados de forma elegante.

---

## Funcionalidades implementadas

- Cadastro de aluno com **nome**, **matrícula (numérica)**, **idade** e **curso**.  
- **Validação de entrada**, garantindo que matrícula seja numérica e campos obrigatórios não estejam vazios.  
- **Listagem e busca** de alunos cadastrados.  
- **Remoção de registros**, com confirmação para evitar exclusões acidentais.  
- **Salvamento automático** dos dados em CSV ou TXT após alterações.  
- **Tratamento de erros** para evitar que entradas inválidas travem o programa.

---

## Objetivos de aprendizado

Com este projeto, você consolida habilidades essenciais como:

- Desenvolvimento de **lógica de programação**.  
- Aplicação de **POO** para organizar e estruturar o código.  
- Controle de **fluxo com menus** e entrada do usuário.  
- **Leitura e gravação de arquivos** com persistência de dados.  
- **Modularização** do projeto.  
- Implementação de **tratamento de erros** e validação de dados.  
- Uso de **boas práticas de código**.

---
## Estrutura de pastas (sugestão)

Projeto-registro-de-alunos/
main.py  (Lógica principal e menus interativos)
aluno.py (Classe Aluno e métodos relacionados)
arquivo.py (Funções para salvar, ler e manipular arquivos)
banco_de_dados.txt (Cadastro persistido em formato texto ou CSV)
README.md (Documentação do projeto)
.gitignore (Arquivos ignorados pelo Git)

---

## Como usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/RodrigoAssis7/Projeto-registro-de-alunos.git
Entre na pasta do projeto: `cd Projeto-registro-de-alunos`

Execute o sistema: `python main.py`

Use o menu de texto, escolhendo entre as opções de cadastrar, buscar, listar ou remover alunos.

2. **Observação**:
O banco de dados e as fotos ficam salvos localmente na pasta do projeto.

3. **Video explicativo**: Para esclarecer eventuais dúvidas, disponibilizei um vídeo de demonstração feito por mim, apresentando o funcionamento do sistema.

segue o link:
