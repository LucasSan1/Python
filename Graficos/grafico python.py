import matplotlib.pyplot as plt

eixox =[8, 10, 12, 14, 16]
eixoy =[1, 9, 4, 15, 12]

plt.plot(eixox, eixoy)

plt.title('vendas no dia aa/aa/aa')
plt.ylabel('numero de vendas')
plt.xlabel('horas')

plt.grid(True)
plt.show()