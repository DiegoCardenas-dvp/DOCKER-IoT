import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.exp(-x/3) * np.cos(x)

plt.figure(figsize=(8,6))
plt.plot(x, y, label='Señal Amortiguada', color='red')
plt.title('Gráfica Generada en Contenedor Python')
plt.grid(True)
plt.savefig('output/grafica_python.png')
print("Gráfica guardada en output/grafica_python.png")
