from matplotlib import pyplot as plt
import matplotlib.animation as animation
import pandas as pd

data_buffer = pd.read_csv("./annual-generated.csv")

year = data_buffer['Year']
net = data_buffer['Net Electricity Generation (TkWh)']

fig = plt.figure()
axis = plt.subplot()


def update(frame):
    axis.clear()

    # update data each frame
    x = year[:frame]
    y = net[:frame]

    axis.set_title('Electricity Net Generation, Electric Power Sector: Created By Paris Lotito')
    axis.set_xlabel('Year')
    axis.set_ylabel('Net Electricity Generation in Billions of kWh')

    axis.plot(x, y, label = 'annual generated')
    axis.set_xlim(xmin=1949.0, xmax=2023.0)
    axis.set_ylim(ymin=250.0, ymax=4100.0)

ani = animation.FuncAnimation(fig, update, interval=60, save_count=100)
ani.save(filename="./tmp/plot.gif", writer='pillow', fps=60)
# plt.show()
