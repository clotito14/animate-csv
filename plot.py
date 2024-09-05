from matplotlib import pyplot as plt
import matplotlib.animation as animation
import pandas as pd

data_buffer = pd.read_csv("./annual-generated.csv")

year = data_buffer['Year']
net = data_buffer['Net Electricity Generation (TkWh)']

fig = plt.figure()
axis = plt.subplot()

def animate(i):
    axis.clear()
    axis.plot(year[:i], net[:i], label = 'annual generated')
    axis.set_xlim([1949, 2023])
    axis.set_ylim([250, 4100])

ani = animation.FuncAnimation(fig, animate, interval=10)
ani.save(filename="./tmp/plot.gif", writer='pillow')
