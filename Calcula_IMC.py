import tkinter as tk



def imc():
    peso = eval(entry1.get())
    altura = eval(entry2.get())
    resultado = peso / (altura**2)
    imc = 'Valores Inválidos \nPor favor, insira o peso em kG e a altura em metros'
    if resultado > 30:
        imc = 'Obesidade'
    elif 30 > resultado >= 25:
        imc = 'Sobrepeso'
    elif 25 > resultado >= 18.5:
        imc = 'Normal'
    elif 18.5 > resultado >= 0:
        imc = 'Baixo Peso'
    label_resultado.config(text=f"Seu IMC é: {imc}\n{resultado}")


# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de Soma")
janela.geometry("200x200")
janela.configure(border=10,relief="ridge")

# Estilizando a janela
janela['background'] = '#856ff8'

# Adicionando padding a Janela
janela.configure(padx=10, pady=10)


# Criação dos campos de entrada
label1 = tk.Label(janela, text="Peso:")
label1.pack()
label1.configure(width=25)
entry1 = tk.Entry(janela)
entry1.pack()
entry1.configure(width=30)

label2 = tk.Label(janela, text="Altura:")
label2.pack()
label2.configure(width=25)
entry2 = tk.Entry(janela)
entry2.pack()
entry2.configure(width=30)

# Criação do botão de soma
botao_somar = tk.Button(janela, text="Calcular IMC", command=imc, bg='#ffffff', activebackground='#856ff8')
botao_somar.pack()
botao_somar.configure(width=25)


# Criação do rótulo para exibir o resultado
label_resultado = tk.Label(janela)
label_resultado.pack()
label_resultado.configure(width=25)


# Execução da janela
janela.mainloop()
