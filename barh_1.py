import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'
with open("data.txt", "r") as f:
    data = f.read().strip().split()
with open("name.txt","r") as f:
    name = f.read().split()


data = [float(i) for i in data]
name.reverse()
data.reverse()
font = FontProperties(fname='/Library/Fonts/Arial Unicode.ttf', size=12)
color = ['b']*17
color.append('r')
color.reverse()
print(color)

fig, ax = plt.subplots(figsize=(18, 10), dpi=80)
ax.barh(name, data, color = color)

ax.tick_params(axis='y', which='major', labelsize=16)

plt.title("女性醫生在不同國家的佔比", fontsize = 24)
ax.set_xlabel('女性醫師佔整體醫師的百分比', fontsize = 15)
plt.ylabel("國家名字", fontproperties = font, rotation = 0, fontsize = 18)
plt.gca().yaxis.set_label_coords(-0.1, 0.5)
for i in range(len(data)):
    plt.text(data[i], name[i], str(f'{data[i]}%'),fontsize=14, va = 'center')
plt.savefig("女性醫師佔比.jpg",dpi=300, bbox_inches='tight' ,format = 'jpg')
plt.show()
