import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import Tk, Canvas


class Huy:
    @staticmethod
    def plot(color='black',
             aspect=1,
             xlabel='i',
             ylabel='hui',
             title='Huy'):  # Draws a plot in the shape of dick
        
        def func1(x):  # Egg function
            y = math.sqrt(4 - (x + 2) * (x + 2)) - 6
            return y
        
        def func2(x):  # Egg function
            y = math.sqrt(4 - (x - 2) * (x - 2)) - 6
            return y
        
        fig, ax = plt.subplots()
        
        x = [i for i in np.arange(-2, 2, 0.01)]  # Dick plot start
        y = [-i * i for i in x]
        ax.scatter(x, y, color=color)  # Dick plot end
        
        x = [i for i in np.arange(-1.5, 1.5, 0.01)]  # Dickhead plot start
        y = [-2.25 for i in x]
        ax.scatter(x, y, color=color)  # dickhead plot end
        
        for i in np.arange(-4, 0, 0.001):  # Egg plot start
            x.append(i)
            y.append(func1(i))
            x.append(i)
            y.append(func1(i) - 2 * abs(-6 - func1(i)))
        ax.scatter(x, y, color=color)  # Egg plot end
        
        for i in np.arange(0, 4., 0.001):  # Egg plot start
            x.append(i)
            y.append(func2(i))
            x.append(i)
            y.append(func2(i) - 2 * abs(-6 - func2(i)))
ax.scatter(x, y, color=color)  # Egg plot end

ax.set_aspect(aspect)  # Square shape of plot
ax.set_xlabel(xlabel)  # Label for x
ax.set_ylabel(ylabel)  # Label for y
ax.set_xlim(-5, 5)  # X points
ax.set_ylim(-9, 1)  # Y points
ax.set_title(title)  # Plot title

plt.show()

@staticmethod
    def draw(outline_egg='black',  # Draws dick in tkinter
             fill_egg=None,
             width_egg=3,
             outline_dick='black',
             fill_dick=None,
             width_dick=3):
        root = Tk()
        canvas = Canvas(width=500,
                        height=500)
                        canvas.create_arc(150, 490, 350, 10,  # Dick draw
                                          start=0,
                                          extent=180,
                                          width=width_dick,
                                          fill=fill_dick,
                                          outline=outline_dick)
                        canvas.create_rectangle(150, 250, 350, 250,  # Dick bugs fix
                                                width=width_dick,
                                                fill='white',
                                                outline='white')
                        canvas.create_oval(50, 450, 250, 250,  # Egg draw
                                           width=width_egg,
                                           fill=fill_egg,
                                           outline=outline_egg)
                        canvas.create_oval(250, 450, 450, 250,  # Egg draw
                                           width=width_egg,
                                           fill=fill_egg,
                                           outline=outline_egg)
                        canvas.create_rectangle(250, 10, 250, 70,  # Dickhead draw
                                                width=width_dick,
                                                fill=fill_dick,
                                                outline=outline_dick)
                        canvas.create_rectangle(185, 70, 315, 70,  # Dickhead draw
                                                width=width_dick,
                                                fill=fill_dick,
                                                outline=outline_dick)
                        canvas.pack()
                        root.mainloop()

@staticmethod
    def text(text='Huy',  # Just prints "Huy"
             amount=1,
             sep=' '):
        for i in range(amount):
            print(text, sep=sep)


