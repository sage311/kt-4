import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# Функция для создания снимков экрана
def save_figure_as_image(fig, filename):
    fig.savefig(filename, dpi=300)
    image = Image.open(filename)
    image.show()

# Создание 3D графиков
fig = plt.figure(figsize=(12, 4))
fig.patch.set_facecolor('#1F1F1F')  # Установим тёмный фон

# Первое подграфическое окно
ax1 = fig.add_subplot(141, projection='3d')
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = X**2 - Y**2
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('Плоскость 1', color='white')
ax1.set_facecolor('#1F1F1F')

# Второе подграфическое окно
ax2 = fig.add_subplot(142, projection='3d')
Z2 = np.exp(-np.sqrt(X**2 + Y**2))
ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_title('Плоскость 2', color='white')
ax2.set_facecolor('#1F1F1F')

# Третье подграфическое окно (Тор)
ax3 = fig.add_subplot(143, projection='3d')
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
r = 2  # Уменьшили радиус
X3 = r * np.sin(phi) * np.cos(theta)
Y3 = r * np.sin(phi) * np.sin(theta)
Z3 = r * np.cos(phi)
ax3.plot_surface(X3, Y3, Z3, color='orange')
ax3.set_title('3D Тор (Сверху)', color='white')
ax3.set_facecolor('#1F1F1F')

# Четвёртое подграфическое окно с анимацией
ax4 = fig.add_subplot(144, projection='3d')
X4 = np.linspace(-10, 10, 100)
Y4 = np.linspace(-10, 10, 100)
X4, Y4 = np.meshgrid(X4, Y4)

# Функция для обновления анимации
def update(frame):
    ax4.clear()
    Z4 = np.sin(X4 + 0.3 * frame)
    ax4.plot_surface(X4, Y4, Z4, cmap='inferno')
    ax4.set_title('3D Одинокая Волна', color='white')
    ax4.set_zlim(-1, 1)
    ax4.set_facecolor('#1F1F1F')

# Отображаем первый кадр анимации
update(0)

# Сохранение изображений
save_figure_as_image(fig, 'figure.png')

plt.show()
