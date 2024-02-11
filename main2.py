# importar as Bibliotecas -----------------------------------------------------------------------------------
from tkinter import *
import os
import tkinter
from tkinter import messagebox
#-----------------------------------------------------------------------------------------------------------
# cores a usar neste Projecto ------------------------------------------------------------------------------
Co0='#00c2ff' # bg Botões 
#-----------------------------------------------------------------------------------------------------------
# criar a Função sair --------------------------------------------------------------------------------------
def sair_sistema():
    resposta = messagebox.askquestion("Sair", "Tem certeza que deseja sair?Sim/Nao")
    if resposta == 'yes':
        janela.quit()
#-----------------------------------------------------------------------------------------------------------
# função para abrir a linha de comandos Do windows ---------------------------------------------------------
def abrir_cmd():
    os.system("start cmd")
#-----------------------------------------------------------------------------------------------------------
# função para abrir bloco de Notas -------------------------------------------------------------------------    
def abrir_Bloco():
    os.system("start notepad")
#-----------------------------------------------------------------------------------------------------------
# messagem Sobre -------------------------------------------------------------------------------------------
def sobre ():
    messagebox.showinfo('Informação',
    'Este programa nasceu para dar suporte ao windows 7'+
    ' e a quem Programa em Python com windows 7 \n'+
    ' Autor: dev Joel 2024 Portugal ©')    
#----------------------------------------------------------------------------------------------------------
# função para mostar O selector de cores -------------------------------------------------------------------
def mostrar_seletor_cores():
    # Definindo as cores
    cor0 = "#444466"  # Preto
    cor1 = "#feffff"  # Branco
    cor2 = "#004338"

    # Criando a janela principal
    janela = Tk()
    janela.geometry("530x205")
    janela.configure(bg=cor1)
    janela.iconbitmap('icon1.ico')  # Ícone da janela
    janela.title('Selector de cores')

    # Configurando os elementos da janela
    tela = Label(janela, bg=cor0, width=40, height=10, bd=1)  # Área de exibição da cor
    tela.grid(row=0, column=0)

    frame_direita = Frame(janela, bg=cor1)  # Frame para controles deslizantes
    frame_direita.grid(row=0, column=1, padx=5)

    frame_baixo = Frame(janela, bg=cor1)  # Frame para o código hexadecimal e botão 'Copiar'
    frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)

    # Função para atualizar a cor quando os controles deslizantes são movidos
    def escala(valor):
        r = s_red.get()
        g = s_green.get()
        b = s_blue.get()
        
        # Convertendo para código hexadecimal
        hexadecimal = "#%02x%02x%02x" % (r, g, b)
        
        # Alterando a cor de fundo da área de exibição
        tela['bg'] = hexadecimal
        
        # Atualizando a entrada com o código hexadecimal
        e_cor.delete(0, END)
        e_cor.insert(0, hexadecimal)

    # Função para copiar o código hexadecimal para a área de transferência
    def onClick():
        tkinter.messagebox.showinfo('Cor', "A cor foi copiada")  # Exibindo uma caixa de diálogo informativa
        
        # Copiando o código hexadecimal para a área de transferência
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(e_cor.get())
        clip.destroy()

    # Configurando os controles deslizantes para vermelho, verde e azul
    l_red = Label(frame_direita,text='Red', width=7, bg=cor1, fg='red', anchor='nw', font=("Time New Roman", 12, "bold"))
    l_red.grid(row=0, column=0)
    s_red = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg="red", orient=HORIZONTAL)
    s_red.grid(row=0, column=1)

    l_green = Label(frame_direita,text='Green', width=7, bg=cor1, fg='green', anchor='nw', font=("Time New Roman", 12, "bold"))
    l_green.grid(row=1, column=0)
    s_green = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg="green", orient=HORIZONTAL)
    s_green.grid(row=1, column=1)

    l_blue = Label(frame_direita,text='Blue', width=7, bg=cor1, fg='blue', anchor='nw', font=("Time New Roman", 12, "bold"))
    l_blue.grid(row=2, column=0)
    s_blue = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg="blue", orient=HORIZONTAL)
    s_blue.grid(row=2, column=1)

    # Configurando a seção para o código hexadecimal e o botão 'Copiar'
    l_rgb = Label(frame_baixo,text='CÓDIGO HEX :',  bg=cor1, font=("Ivy", 10, "bold"))
    l_rgb.grid(row=0, column=0, padx=5)

    e_cor = Entry(frame_baixo, width=12, font=("Ivy", 10, "bold"), justify=CENTER)  # Entrada para o código hexadecimal
    e_cor.grid(row=0, column=1, padx=5)

    b_copiar = Button(frame_baixo,command=onClick, text='Copiar a cor',  bg=cor1, font=("Ivy", 8, "bold"), relief=RAISED, overrelief=RIDGE)  # Botão 'Copiar'
    b_copiar.grid(row=0, column=2, padx=5)

    l_app_nome = Label(frame_baixo,text='Seletor de Cores',  bg=cor1, font=("Ivy", 15, "bold"))  # Nome do aplicativo
    l_app_nome.grid(row=0, column=3, padx=40)

    janela.mainloop()  # Iniciando o loop principal da interface gráfica
#------------------------------------------------------------------------------------------------------------
# configurar a Janela ---------------------------------------------------------------------------------------
janela = Tk()
janela.title('Programar Python cmd')
janela.geometry('300x390+100+100')
janela.resizable(0,0)
janela.config(bg='white')
janela.iconbitmap('C:\\Users\\HP\\Desktop\\Projectos\\Sistema\\icon1.ico')
#------------------------------------------------------------------------------------------------------------
# Botão para abrir o CMD do Windows --------------------------------------------------------------------------------------
Bcmd = Button(janela, text='CMD windows', font=('arial 20'), relief=RAISED, overrelief=RIDGE, width=17, command=abrir_cmd, bg=Co0)
Bcmd.place(x=10, y=20)
#--------------------------------------------------------------------------------------------------------------------------
# Botão para abrir o Bloco de Notas do Windows -----------------------------------------------------------------------------------
Bnotepad = Button(janela, text='Bloco de Notas', font=('arial 20'), relief=RAISED, overrelief=RIDGE, width=17, command=abrir_Bloco, bg=Co0)
Bnotepad.place(x=10, y=90)
#----------------------------------------------------------------------------------------------------------------------------------

# Botão para abrir o selector de cores ---------------------------------------------------------------------------------------------
Bcolor = Button(janela, text='Selector de cores', font=('arial 20'), relief=RAISED, overrelief=RIDGE, width=17, command=mostrar_seletor_cores,bg=Co0)
Bcolor.place(x=10, y=160)
#-----------------------------------------------------------------------------------------------------------------------------------

# Botão para Sobre o sistema ------------------------------------------------------------------------------------------------------- 
BSobre = Button(janela, text='Sobre O Sistema', font=('arial 20'), relief=RAISED, overrelief=RIDGE, width=17, command=sobre,bg=Co0)
BSobre.place(x=10, y=230)
#-----------------------------------------------------------------------------------------------------------------------------------
# Botão para Sair do sistema -------------------------------------------------------------------------------------------------------
BSair = Button(janela, text='Sair do Sistema', font=('arial 20'), relief=RAISED, overrelief=RIDGE, width=17, command=sair_sistema,bg=Co0)
BSair.place(x=10, y=300)
#-----------------------------------------------------------------------------------------------------------------------------------
# iniciar a Janela -----------------------------------------------------------------------------------------------------------------
janela.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------