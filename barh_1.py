import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'
"""with open("data.txt", "r") as f:
    data = f.read().strip().split()
with open("name.txt","r") as f:
    name = f.read().split()"""

name = ['土木營建', '建築', '電子電機', '資訊通訊', '化工材料' ,'生技醫工', '環工綠能','機械']
data = [15, 29, 8, 18, 17, 44,17,3]
t = zip(name, data)
d = dict(t)
sort_list = sorted(d.values())
sort_dict = {}

for i in sort_list:
    for j in d:
        if d[j] == i:
            sort_dict[j] = i
            break
name = list(sort_dict.keys())
data = list(sort_dict.values())#注意unhashtable
#data = [float(i) for i in data]
#name.reverse()
#data.reverse()
font = FontProperties(fname='/Library/Fonts/Arial Unicode.ttf', size=12)
#color = ['b']*17
#color.append('r')
#color.reverse()
#print(color)

fig, ax = plt.subplots(figsize=(19, 10), dpi=80)
ax.barh(name, data, color = 'b')

ax.tick_params(axis='y', which='major', labelsize=16)

plt.title("各工程師中女性佔比", fontsize = 24)
ax.set_xlabel('佔比', fontsize = 15)
plt.ylabel("職業名稱", fontproperties = font, rotation = 0, fontsize = 18, color = 'b')
plt.gca().yaxis.set_label_coords(-0.12, 0.6)
for i in range(len(data)):
    plt.text(data[i], name[i], str(f'{data[i]}%'),fontsize=14, va = 'center')
plt.savefig("女工程師.jpg",dpi=300, bbox_inches='tight' ,format = 'jpg')
plt.show()
