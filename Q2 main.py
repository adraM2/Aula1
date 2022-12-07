hi=int(input("digite a hora inicial em formato 12h: "))
mi=int(input("digite o minuto inicial: "))
hf=int(input("digite a hora final: "))
mf=int(input("digite o minuto final: "))
h= hf-hi
h_=h*60
m=mf-mi
horastotal=(h_ + m)//60
print("O jogo durou",horastotal,"horas e",m,"minutos")
