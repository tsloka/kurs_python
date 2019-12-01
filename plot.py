import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df['E'] = df['A'] + df['C']
print(df[['A','B','E']])

a = df['E'].sum()
print(a)
#df.to_csv('tablica.csv')

df1 = pd.read_csv('tablica.csv')

print(df1)

plt.contour([df['A'], df['B'],] df['C','E'], c = 'y', label='Pierwszy wykres', marker='^')
plt.ylim((0,100))
plt.xlim(0,100)
plt.xlabel('labelX [\03ucm]')
plt.ylabel('labelY')
plt.legend()
plt.show()
