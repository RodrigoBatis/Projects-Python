# Importando tkinter 
from tkinter import *
from tkinter import ttk

#Importando tkcalendar 
from tkcalendar import Calendar, DateEntry

#Importando dateutil
from dateutil.relativedelta import relativedelta

#Importando datetime
from datetime import date


#Criando uma janela 
janela =Tk()
#colocando titulo na janela 
janela.title("Calculadora de Idade")
#adicionando uma largura e a altura
janela.geometry("310x400")

# Cores Utilizadas 
black       = "#3b3b3b"
black_heavy = "#333333"
white       = "#feffff"
orange      = "#fcc058"

#Criando frames para dividir a janela em duas partes 

#Parte de cima da calculadora 
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=black_heavy)
frame_cima.grid(row=0, column=0)

#Parte de baixo da calculadora
frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=black)
frame_baixo.grid(row=1, column=0)


#Criando labels para o frame cima

label_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief="flat", anchor="center", font=('Ivy 15 bold'), bg=black_heavy, fg=white)
label_calculadora.place(x=0, y=30)

label_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief="flat", anchor="center", font=('Arial 35 bold'), bg=black_heavy, fg=orange)
label_idade.place(x=0, y=70)


# ---------- Função calcular idade ----------

def calcular_idade():
   inicial  = calendario_inicial.get() 
   termino  = calendario_nascimento.get()

   #Separando os valores
   dia_1, mes_1, ano_1 = [ int(f) for f in inicial.split('/')]
   #Convertendo os valores em formato date/datetime
   data_inicial = date(ano_1, mes_1, dia_1)

   #Separando os valores
   dia_2, mes_2, ano_2 = [ int(f) for f in termino.split('/')]
   #Convertendo os valores em formato date/datetime
   data_nascimento = date(ano_2, mes_2, dia_2)

   anos = relativedelta(data_inicial, data_nascimento).years
   meses = relativedelta(data_inicial, data_nascimento).months
   dias = relativedelta(data_inicial, data_nascimento).days

   label_app_anos["text"] = anos
   label_app_meses["text"] = meses
   label_app_dias["text"] = dias

#Criando labels para o frame baixo

#Frame Data_inicial
label_data_inicial = Label(frame_baixo, text="Data inicial", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 11'), bg=black, fg=white)
label_data_inicial.place(x=40, y=30)

#Criando o calendario para a data inicial para o calculo
calendario_inicial = DateEntry(frame_baixo, width=13, bg="darkblue", fg=white, borderwidth=2, date_pattern="dd/mm/y", y=2022)
calendario_inicial.place(x=180, y=30)

#Frame Data_nascimento
label_data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 11'), bg=black, fg=white)
label_data_nascimento.place(x=40, y=70)

#Criando o calendario para a data de nascimento para o calculo
calendario_nascimento = DateEntry(frame_baixo, width=13, bg="darkblue", fg=white, borderwidth=2, date_pattern="dd/mm/y", y=2022)
calendario_nascimento.place(x=180, y=70)

#Local que mostra quantos anos possui
label_app_anos = Label(frame_baixo, text="0", height=1, padx=0, pady=0, relief="flat", anchor="center", font=('Ivy 25 bold'), bg=black, fg=white)
label_app_anos.place(x=60, y=135)

label_app_anos_nome = Label(frame_baixo, text="Anos", height=1, padx=0, pady=0, relief="flat", anchor="center", font=('Ivy 11 bold'), bg=black, fg=white)
label_app_anos_nome.place(x=60, y=175)

#Local que mostra quantos anos/messes possui
label_app_meses = Label(frame_baixo, text="0", height=1, padx=0, pady=0, relief="flat", anchor="center", font=('Ivy 25 bold'), bg=black, fg=white)
label_app_meses.place(x=140, y=135)

label_app_meses_nome = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief="flat", anchor="center", font=('Ivy 11 bold'), bg=black, fg=white)
label_app_meses_nome.place(x=140, y=175)


#Local que mostra quantos anos/messes/dias possui
label_app_dias = Label(frame_baixo, text="0", height=1, padx=0, pady=0, relief="flat", anchor="center", font=('Ivy 25 bold'), bg=black, fg=white)
label_app_dias.place(x=220, y=135)

label_app_dias_nome = Label(frame_baixo, text="Dias", height=1, padx=0, pady=0, relief="flat", anchor="center", font=('Ivy 11 bold'), bg=black, fg=white)
label_app_dias_nome.place(x=220, y=175)


#Criando botão calcular
btn_calcular = Button(frame_baixo, command=calcular_idade, text="Calcular", width=20, height=1, relief="raised", overrelief="ridge", font=('Ivy 10 bold'), bg=black, fg=white)
btn_calcular.place(x=70, y=225)


janela.mainloop()