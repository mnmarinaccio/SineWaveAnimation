'''
Sine Wave Animation
Author: Michael Marinaccio, [Github Profile](https://github.com/mnmarinaccio)
Date: February, 2025 

This Python script generates an animated plot of a sine wave using matplotlib. 
The wave appears to move horizontally as the animation updates the x-values and recalculates the sine values in real time.
This file serves as template code for creating math animations with matplotlib.

''' 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

if __name__ == '__main__':
    X = np.linspace(0, 10*np.pi, 1000)
    Y = np.sin(X)
    
    fig, ax = plt.subplots()
    line, = ax.plot(X,Y)
    
    def update(frame):
        global X
        X += 0.1
        Y = np.sin(X)
        line.set_ydata(Y)
        line.set_xdata(X)
        return line,


    ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
    # uncomment below two lines to save the animation as a GIF 
    # ani.save('./images/sine_wave.gif', writer='pillow', fps=20)
    
    plt.title('Animated Sine Wave')
    plt.show()