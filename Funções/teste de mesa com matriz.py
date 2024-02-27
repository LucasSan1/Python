exemplo = [['A', 'D', 'C'],['D', 'E', 'F']]

print('Numero de linhas da matriz:', len(exemplo))
print('Numero de colunas da matriz:', len(exemplo[0]))
print()
num_lin = 0

print('---------- teste de mesa ----------')
print('Linha\tColuna\tElemento acessado\tConteudo')

for lin in range(len(exemplo)):
  for col in range(len(exemplo[lin])):
    print(num_lin, '\t', col, '\t', 'a' +eval(r'"\u208' + str(num_lin) + '"'+r'"\u208' + str(col) + '"' ), '\t\t\t', exemplo[lin][col] )
    num_lin +=1