import csv

group1 = "group1.txt"
group2 = "group2.txt"

fd = open(group1, "r")
reader = csv.reader(fd,)
for row in reader:
    print(row)
while True:
 line = fd.readline()
 if not line:
     break
print(line.strip())
fd.close()

fd = open(group2, "r")
reader = csv.reader(fd)
for row in reader:
    print(row)
while True:
 line = fd.readline()
 if not line:
     break
print(line.strip())
fd.close()


fd = open(group1, "a")
a = input() + "/n"
print(a)
fd.close()

import glob 
for group1 in glob.glob("C:\\group1.txt"):
    print(group1)

for group2 in glob.glob("C:\\group1.txt"):
    print(group2)







