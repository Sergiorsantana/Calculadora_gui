import tkinter as tk
from tkinter import messagebox

# Função para calcular
def calcular():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        operacao = operador.get()

        if operacao == '+':
            resultado = a + b
        elif operacao == '-':
            resultado = a - b
        elif operacao == '*':
            resultado = a * b
        elif operacao == '/':
            resultado = a / b if b != 0 else 'Erro: Divisão por zero'
        else:
            resultado = 'Operação inválida'

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Campos de entrada
tk.Label(janela, text="Número 1:").grid(row=0, column=0)
entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=1)

tk.Label(janela, text="Número 2:").grid(row=1, column=0)
entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=1)

# Operação
tk.Label(janela, text="Operação:").grid(row=2, column=0)
operador = tk.StringVar()
operador.set("+")  # Define a opção padrão

opcoes = ["+", "-", "*", "/"]
menu_operacao = tk.OptionMenu(janela, operador, *opcoes)
menu_operacao.grid(row=2, column=1)

# Botão calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2)

# Exibir resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2)

# Iniciar a interface gráfica
janela.mainloop()
