text = "Children start school at the age of five, but there is some free nursery-school education before that age. The state nursery schools are not for all. They are for some families, for example for families with only one parent. In most areas there are private nursery schools. Parents who want their children to go to nursery school pay for their children under 5 years old to go to these private nursery schools.".upper()
import pylab as plt
import sys
lettersCount = {i:text.count(i) for i in text}

del lettersCount[" "]
del lettersCount["."]
del lettersCount[","]


xdata = list(lettersCount.keys())
xdata.sort()
ydata = [lettersCount[i] for i in xdata]


plt.bar(xdata, ydata)
plt.title("English Text 9 клас")
plt.show()
plt.savefig(sys.path[0]+"/risunok2.png")