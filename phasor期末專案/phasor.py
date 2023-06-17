import numpy as np
import matplotlib.pyplot as plt
import os
T = np.linspace(0.0, 2*np.pi, num=180)
print(T)

count = 0
"""plt.arrow(0,0,np.cos(np.pi/3),np.sin(np.pi/3))
plt.arrow(np.cos(np.pi/3), np.sin(np.pi/3),np.cos(np.pi/3)+np.cos(np.pi*2/3),np.sin(np.pi/3)+np.sin(np.pi*2/3))
plt.show()"""
for theta in T:
    ax = plt.gca()
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    x, y= 0,0
    dx, dy = np.cos(theta), np.sin(theta)
    for s in range(2, 10):
        plt.arrow(x, y, dx, dy, width = 0.1)
        x, y = x+dx, y+dy
        dx, dy = np.cos(s*theta), np.sin(s*theta)
    plt.savefig("pic{:0>3d}".format(count))
    count += 1
    ax.cla()
ax = plt.gca()
ax.cla()

for i in range(80):
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    x, y= 0,0
    for j in range(8):
        plt.arrow(x,y,1,0, width = 0.1)
        x += 1
    plt.savefig("pic{:0>3d}".format(count))
    count += 1
    ax.cla()
os.system("ffmpeg -r 30 -i pic%03d.png -pix_fmt yuv420p out.mp4")