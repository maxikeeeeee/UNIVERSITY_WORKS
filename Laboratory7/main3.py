import pylab as plt
import sys

with open(sys.path[0]+'/k0l0b0k.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    sentencesCount = {
        ".": data.count(". "),
        "!": data.count("! "),
        "?": data.count("? "),
        "...": data.count("... "),
    }

xdata = list(sentencesCount.keys())
ydata = [sentencesCount[i] for i in xdata]
plt.bar(xdata, ydata)
plt.title("Загальна кількість речень \'Колобок\' ")
plt.savefig(sys.path[0]+"/risunok3.png")