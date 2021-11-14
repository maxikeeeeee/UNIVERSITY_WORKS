from numpy import *
import matplotlib.pyplot as plt

x = linspace(-5, 5, 100)
y = 1/x*sin(5*x)

plt.plot(x, y, 'g--', label='1/x*sin(5*x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Laboratory №7')
plt.legend() # вставка легенди (тексту в label)
plt.show()