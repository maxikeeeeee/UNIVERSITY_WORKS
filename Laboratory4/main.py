#Частота появи слів з різною довжиною
import sys
rawSentences = []
with open(sys.path[0] + "/tolsoi.txt", "r", encoding="utf-8") as book:
  lines = book.readlines()
  for line in lines:
    sentencesInLine = line.split(".")
    if line != "\n" and line != "~ ~ ~\n":
      for i in sentencesInLine:
        if i != "":
          rawSentences.append(i)

counter = {}
sentCount = 0
for line in rawSentences:
  wordsCount = len(line)
  if wordsCount in counter:
    counter[wordsCount] += 1
  else:
    counter[wordsCount] = 1
  sentCount += 1

print("Пари: "+ str(counter))
print("Кількість слів: "+ str(sentCount))
print("Частота появи слів: "+ str(len(counter) / sentCount))