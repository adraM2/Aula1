quantidade=0
somaidades=0
idade=int(input("qual a sua idade? "))
while idade>0:
  quantidade=quantidade + 1
  somaidades= somaidades + idade
  idade=int(input("qual a sua idade? "))
media=somaidades/quantidade
print("A media das idades é",media)
