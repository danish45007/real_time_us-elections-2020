from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

frame_len = 10000

fig = plt.figure(figsize=(9,6))


def animate(i):
    data = pd.read_csv('sentiment.csv')
    y1 = data['Trump']
    y2 = data['Warren']

    if len(y1) <= frame_len:
        plt.cla()
        plt.plot(y1, label='Donald Trump')
        plt.plot(y2, label='Elizabeth Warren')
    else:
        plt.cla()
        plt.plot(y1[-frame_len:], label='Donald Trump')
        plt.plot(y2[-frame_len:], label='Elizabeth Warren')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()