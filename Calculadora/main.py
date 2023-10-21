from tkinter import *
from tkinter import ttk

#cores (color picker Google)
cor_preta = '#2b2e2c'
cor_branca = '#ebedeb'
cor_azul = '#278adb'
cor_cinza = '#617280'
cor_laranja = '#e37d29'

janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg=cor_preta)

#frames
frame_tela = Frame(janela, width=235, height=50, bg=cor_azul,)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variavel global
todos_valores = ''

#função
def entrar_valores(event):
    
    global todos_valores

    todos_valores += str(event)
   
    #mostrando valores na tela
    valor_texto.set(todos_valores)

#função calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor_branca, fg=cor_preta)
app_label.place(x=0, y=0)

#botões
#fila 1
botao1 = Button(frame_corpo, command=limpar_tela , text='C', width=11, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao1.place(x=0, y=0)

botao2 = Button(frame_corpo, text='%', width=5, height=2, command= lambda: entrar_valores('%'), bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao2.place(x=118, y=0)

botao3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text='/', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao3.place(x=177, y=0)

#fila 2
botao4 = Button(frame_corpo, command= lambda: entrar_valores('9'), text='9', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao4.place(x=0, y=52)

botao5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text='8', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao5.place(x=59, y=52)

botao6 = Button(frame_corpo, command= lambda: entrar_valores('7'), text='7', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao6.place(x=118, y=52)

botao7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text='*', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao7.place(x=177, y=52)

#fila 3
botao8 = Button(frame_corpo, command= lambda: entrar_valores('6'), text='6', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=0, y=104)

botao9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text='5', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=59, y=104)

botao10 = Button(frame_corpo, command= lambda: entrar_valores('4'), text='4', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao10.place(x=118, y=104)

botao11 = Button(frame_corpo, command= lambda: entrar_valores('+'), text='+', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao11.place(x=177, y=104)

#fila 4
botao12 = Button(frame_corpo, command= lambda: entrar_valores('3'), text='3', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao12.place(x=0, y=156)

botao13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text='2', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao13.place(x=59, y=156)

botao14 = Button(frame_corpo, command= lambda: entrar_valores('1'), text='1', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao14.place(x=118, y=156)

botao15 = Button(frame_corpo, command= lambda: entrar_valores('-'), text='-', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao15.place(x=177, y=156)

#fila 5
botao16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text='0', width=11, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao16.place(x=0, y=208)

botao17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text='.', width=5, height=2, bg=cor_cinza, fg=cor_preta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao17.place(x=118, y=208)

botao18 = Button(frame_corpo, command=calcular, text='=', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao18.place(x=177, y=208)


janela.mainloop()