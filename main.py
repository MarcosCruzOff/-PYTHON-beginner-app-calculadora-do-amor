# Importando tkinter
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk


# cores

cor0 = "#2e2d2b"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"  # letra
cor5 = "#e06636"  # - profit
cor6 = "#038cfc"  # azul
cor7 = "#3fbfb9"  # verde

# Criando app -----------------------------------------------------

app = Tk ()
app.title ("Calculadora do amor")
icon = PhotoImage(file="imagens/icon.png")
app.iconphoto(True, icon)
app.geometry('410x400')
app.configure(background=cor1)
app.resizable(width=FALSE, height=FALSE)

style = Style(app)
style.theme_use("clam")

# Frames -----------------------------------------------------

frameCima = Frame(app, width=418, height=200, bg=cor1,  relief="flat",)
frameCima.grid(row=0, column=0)

frameMeio = Frame(app, width=418, height=200, bg=cor1,  relief="solid",)
frameMeio.grid(row=1, column=0)

# Logo -----------------------------------------------------
app_ = Label(
        frameCima,
        text="Calculadora do amor",
        width=400, 
        padx=5, 
        relief=FLAT, 
        anchor=NW, 
        font=('jetBrains Mono', 20),
        bg=cor7,
        fg=cor1)

app_.place(x=0, y=0)

app_img = Image.open('imagens/coracao.png')
app_img = app_img.resize((140, 140))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900,compound=LEFT, padx=5, relief=FLAT, anchor=NW,bg=cor1, fg=cor4 )
app_logo.place(x=10, y=50)

# ------------ Resultado ------------------------------------

l_resultado = Label(frameCima, text="",padx=10, width=35, height=1,anchor=NW, font=('Verdana 10 '), bg=cor1, fg=cor0)
l_resultado.place(x=170, y=70)

l_resultado_1 = Label(frameCima, text="",padx=10, width=17, height=1,anchor=CENTER, font=('Verdana 12 bold'), bg=cor1, fg=cor5)
l_resultado_1.place(x=170, y=100)

l_resultado_2 = Label(frameCima, text="",padx=10, width=5, height=1,anchor=CENTER, font=('Verdana 25 bold'), bg=cor1, fg=cor0)
l_resultado_2.place(x=210, y=140)

l_nome = Label(frameMeio, text="Seu nome", height=1,anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_nome.place(x=6, y=15)

e_seu_nome = Entry(frameMeio, width=15, font=('Ivy 14 '), justify='center',relief="solid")
e_seu_nome.place(x=10, y=40)



# linha separatoria

l_linha = Label(frameMeio, width=1, height=10,anchor=NW, font=('Verdana 1 '), bg=cor3, fg=cor1)
l_linha.place(x=190, y=40)
l_linha = Label(frameMeio, width=1, height=10,anchor=NW, font=('Verdana 1 '), bg=cor5, fg=cor1)
l_linha.place(x=200, y=40)

l_nome = Label(frameMeio, text="Nome do/a parceiro/a", height=1,anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_nome.place(x=217, y=15)

e_parceiro_nome = Entry(frameMeio, width=15, font=('Ivy 14 '), justify='center',relief="solid")
e_parceiro_nome.place(x=220, y=40)



# abrindo imagem
app_love  = Image.open('imagens/coracao.png')
app_love = app_love.resize((20, 20))
app_love = ImageTk.PhotoImage(app_love)

botao_calcular = Button(
    frameMeio,
    image=app_love,
    width=200,
    compound=LEFT,
    anchor=CENTER,
    text=" Calcular amor".upper(), 
    overrelief=RIDGE,  
    font=('ivy 9 '),
    bg=cor2, 
    fg=cor1 )
botao_calcular.place(x=110, y=140)

# Função para escolher opções

def escolher():
    # definindo algumas variaveis globais
    global app_img, app_love

    escolha_1 = selecionado_1.get()
    escolha_2 = selecionado_2.get()

    if escolha_1 =='Homem' and escolha_2 =='Mulher':
        imagem = 'imagens/casal_1.jpeg'
        imagem_2 = 'coracao.png'

    elif escolha_1 =='Homem' and escolha_2 =='Homem':
        imagem = 'imagens/casal_3.jpeg'
        imagem_2 = 'coracao.png'

    elif escolha_1 =='Mulher' and escolha_2 =='Homem':
        imagem = 'imagens/casal_1.jpeg'
        imagem_2 = 'coracao.png'

    elif escolha_1 =='Mulher' and escolha_2 =='Mulher':
        imagem = 'imagens/casal_2.jpeg'
        imagem_2 = 'coracao.png'

    else:
        print('selecione os genero')
        return

    # abrindo imagem
    app_img  = Image.open(imagem)
    app_img = app_img.resize((140, 140))
    app_img = ImageTk.PhotoImage(app_img)
    app_logo['image'] = app_img

    # abrindo imagem
    app_love  = Image.open(imagem_2)
    app_love = app_love.resize((30, 30))
    app_love = ImageTk.PhotoImage(app_love)

    botao_calcular['image'] = app_love


selecionado_1 = StringVar()
rad_1 = Radiobutton(frameMeio, text='Homem', bg=cor1,font=('Ivy 10'), value='Homem', variable=selecionado_1, command=escolher).place(x=10, y=80)
rad_2 = Radiobutton(frameMeio, text='Mulher', bg=cor1,font=('Ivy 10'), value='Mulher', variable=selecionado_1, command=escolher).place(x=10, y=105)
selecionado_2 = StringVar()
rad_3 = Radiobutton(frameMeio, text='Homem', bg=cor1,font=('Ivy 10'), value='Homem', variable=selecionado_2, command=escolher).place(x=220, y=80)
rad_4 = Radiobutton(frameMeio, text='Mulher', bg=cor1,font=('Ivy 10'), value='Mulher', variable=selecionado_2, command=escolher).place(x=220, y=105)

app.mainloop()
