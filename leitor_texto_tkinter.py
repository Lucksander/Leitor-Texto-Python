# Importa a biblioteca tkinter
# Esta biblioteca é usada para criar interfaces gráficas em Python, e aqui será utilizada para abrir uma janela de seleção de arquivos.
import tkinter as tk

# Importa a função para abrir janela de seleção de arquivos
from tkinter import filedialog

# Cria a janela principal
janela = tk.Tk()

# Esconde a janela principal
janela.withdraw()

# Abre o explorador de arquivos
caminho_arquivo = filedialog.askopenfilename(
    title="Selecione um arquivo TXT",
    filetypes=[("Arquivos de Texto", "*.txt")]
)

# Verifica se o usuário escolheu um arquivo
if caminho_arquivo:

    try:
        # Abre o arquivo selecionado
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

            # Lê o conteúdo
            conteudo = arquivo.read()

            # Exibe o conteúdo na tela
            print("\n--- Conteúdo do Arquivo ---\n")
            print(conteudo)

    except Exception as erro:
        print("Erro ao ler o arquivo:", erro)

else:
    print("Nenhum arquivo foi selecionado.")