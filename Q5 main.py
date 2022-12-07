def calculasalario(Sb):
  Din=(11*Sb)/100
  k=Sb - Din
  Dir=(15*k)/100
  Sl=Sb - (Din + Dir)
  return Sl

t=calculasalario(5000)
print("O salario liquido é de R$",t)