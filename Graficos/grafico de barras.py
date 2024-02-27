import matplotlib.pyplot as plt

linguagens = ['c/c','python','java','vba','matlab','outras']
y_pos =range(len(linguagens))

percentual = [36, 29, 22, 4, 2, 7]

plt.bar(y_pos, percentual, align='center', alpha=0.5)
plt.xticks(y_pos, linguagens)
plt.ylabel('percentual')

plt.title('percentual de programadores x linguagens de programaçao')
plt.show()