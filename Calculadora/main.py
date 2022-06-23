# Importando tkinter 
from tkinter import *
from tkinter import ttk
from unittest import result

# Cores Utilizadas 

black    = "#3b3b3b"
white    = "#feffff"
blue     = "#38576b"
gray     = "#ECEFF1"
orange   = "#FFAB40"

#Criando uma janela 
janela =Tk()
#colocando titulo na janela 
janela.title("Calculadora")
#adicionando uma largura e a altura
janela.geometry("235x318")
#adicionando uma cor para a janela
janela.config(bg=black)

#Criando frames para dividir a janela em duas partes 

#Parte superior da calculadora 
frame_tela = Frame(janela, width=235, height=50, bg=blue)
frame_tela.grid(row=0, column=0)

#Parte do corpo da calculadora
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#Vareavel todos_valores
todos_valores = ""

valor_txt = StringVar()

#Criando função 
def entrar_valores(event):
   
   global todos_valores
   
   todos_valores  = todos_valores + str(event)

   #passqando o valor para a tela
   valor_txt.set(todos_valores)


#Função para calcular

def calcular():
   global todos_valores
   resultado = eval(todos_valores)
   
   valor_txt.set(str(resultado))



#função para limpar tela

def limpar_tela():
   global todos_valores
   todos_valores = ""
   valor_txt.set("")

#Criando label 

app_label = Label(frame_tela, textvariable= valor_txt, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=blue, fg=white)
app_label.place(x=0, y=0)


#Criando os botões 

btn1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn1.place(x=0, y=0)

btn2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn2.place(x=118, y=0)

btn3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text="/", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn3.place(x=177, y=0)

btn4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn4.place(x=0, y=52)

btn5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn5.place(x=59, y=52)
 
btn6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn6.place(x=118, y=52)

btn7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="*", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn7.place(x=177, y=52)

btn8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn8.place(x=0, y=104)

btn9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn9.place(x=59, y=104)
 
btn10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn10.place(x=118, y=104)

btn11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn11.place(x=177, y=104)

btn12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn12.place(x=0, y=156)

btn13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn13.place(x=59, y=156)
 
btn14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn14.place(x=118, y=156)

btn15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn15.place(x=177, y=156)

btn16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text="0", width=11, height=3, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn16.place(x=0, y=208)

btn17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text=".", width=5, height=3, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn17.place(x=118, y=208)

btn18 = Button(frame_corpo, command= calcular, text="=", width=5, height=3, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn18.place(x=177, y=208)


janela.mainloop()