from tkinter import *
from tkinter import ttk

#cores
cor_preta = '#101211'
cor_azul = '#2264d6'
cor_branca = '#f2f4f7'

#criando e configurando janela
janela = Tk()
janela.title('Limpador de códigos de barras')
janela.geometry('350x146')

#criando os frames
frame1 = Frame(janela, bg=cor_azul, width=350, height=56)
frame2 = Frame(janela, width=350, height=35, bg=cor_azul)
frame3 = Frame(janela, bg=cor_azul, width=350, height=56)

#colocando os frames na janela
frame1.grid(row=0,column=0)
frame2.grid(row=1,column=0)
frame3.grid(row=2,column=0)

#label frame1
label1 = Label(frame1, text='Insira o código de barras',font=('Roboto 17'), height=2, justify=CENTER, width=27, bg=cor_azul, fg=cor_branca)

#input frame2
entry1 = Entry(frame2, width=27, font=('Roboto 10'), relief=FLAT)

#botão frame3
button1 = Button(frame2, text='Limpar', width=7 , height=1, relief=FLAT, overrelief=RIDGE,font='Roboto 9')

#colocando elementos nos frames
label1.place(x=0, y=0)
entry1.place(x=55, y=0)
button1.place(x=250, y=0)

janela.mainloop()