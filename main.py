#Cria e importa as bibliotecas necessárias
from ast import Delete
from tkinter import * #immporta todos         Por que precisa impotar o de baixo se ja importou tudo?
from tkinter import ttk

#cores
#peguei as cores do "color picker"
preto = "#0d0d0d"
branco = "#ffffff"
azul = "#5074ad"
cinza = "#5b5b5e"
laranja = "#ed811c"

#cria janela e faz configurações básicas
janela = Tk() #cria a interface (Não entendi porque usa esse Tk())
janela.title("Calculadora")#nomezinho que fica em cima
janela.geometry("235x250") #largura x comprimento

#dividir a janela em duas partes
#parte superior
frame_tela = Frame(janela, width=235, height=50, bg=cinza)
frame_tela.grid(row=0, column=0)

#parte inferior
frame_corpo = Frame(janela, width=235, height=268,bg= preto)
frame_corpo.grid(row=1, column=0)#Aqui precisa do row=1 porque o corpo é maior do que a tela

#variavel todos os valores
todos_valores = ""

#criando função
def entrar_valores(valor):

    global todos_valores

    todos_valores = todos_valores + str(valor)

    #passando valor para tela
    valor_texto.set(todos_valores)

#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    #mostrar resultado na tela
    valor_texto.set(str(resultado))

#função limpa tela

def limpa_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable = valor_texto, width=16, height=2, padx=7, anchor="e",font=('Ivy 18 '), bg=cinza, fg=branco)
app_label.place(x = 0, y=0)

#criando botões
b_1 = Button(frame_corpo,command = limpa_tela ,text="C", width=16, height=2,overrelief=RIDGE)#Esse último destaca o botao
b_1.place(x=0,y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores("%"), text="%", width=8, height=2, overrelief=RIDGE)
b_2.place(x=121,y=0)
b_3 = Button(frame_corpo, command= lambda: entrar_valores("/"), text="/", width=8, height=2,  bg=laranja, overrelief=RIDGE)
b_3.place(x=178,y=0)

b_4= Button(frame_corpo, command= lambda: entrar_valores("1"), text="1", width=8, height=2, overrelief=RIDGE)
b_4.place(x=0,y=40)
b_5= Button(frame_corpo, command= lambda: entrar_valores("2"), text="2", width=8, height=2, overrelief=RIDGE)
b_5.place(x=60,y=40)
b_6= Button(frame_corpo, command= lambda: entrar_valores("3"), text="3", width=8, height=2, overrelief=RIDGE)
b_6.place(x=120,y=40)
b_7= Button(frame_corpo, command= lambda: entrar_valores("+"), text="+", width=8, height=2, bg=laranja, overrelief=RIDGE)
b_7.place(x=178,y=40)

b_8= Button(frame_corpo, command= lambda: entrar_valores("4"), text="4", width=8, height=2, overrelief=RIDGE)
b_8.place(x=0,y=80)
b_9= Button(frame_corpo, command= lambda: entrar_valores("5"), text="5", width=8, height=2, overrelief=RIDGE)
b_9.place(x=60,y=80)
b_10= Button(frame_corpo, command= lambda: entrar_valores("6"), text="6", width=8, height=2, overrelief=RIDGE)
b_10.place(x=120,y=80)
b_11= Button(frame_corpo, command= lambda: entrar_valores("-"), text="-", width=8, height=2, bg=laranja, overrelief=RIDGE)
b_11.place(x=178,y=80)

b_12= Button(frame_corpo, command= lambda: entrar_valores("7"), text="7", width=8, height=2, overrelief=RIDGE)
b_12.place(x=0,y=120)
b_13= Button(frame_corpo, command= lambda: entrar_valores("8"), text="8", width=8, height=2, overrelief=RIDGE)
b_13.place(x=60,y=120)
b_14= Button(frame_corpo, command= lambda: entrar_valores("9"), text="9", width=8, height=2, overrelief=RIDGE)
b_14.place(x=120,y=120)
b_15= Button(frame_corpo, command= lambda: entrar_valores("*"), text="*", width=8, height=2, bg=laranja, overrelief=RIDGE)
b_15.place(x=178,y=120)

b_16 = Button(frame_corpo, command= lambda: entrar_valores("0"), text="0", width=16, height=2,overrelief=RIDGE)#Esse último destaca o botao
b_16.place(x=0,y=160)
b_17 = Button(frame_corpo, command= lambda: entrar_valores("."), text=".", width=8, height=2, overrelief=RIDGE)
b_17.place(x=121,y=160)
b_18 = Button(frame_corpo, command = calcular, text="=", width=8, height=2,  bg=laranja, overrelief=RIDGE)
b_18.place(x=178,y=160)


#Permite executar o programa
janela.mainloop()