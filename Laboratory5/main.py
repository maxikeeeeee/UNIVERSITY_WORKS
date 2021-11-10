import csv
import sys

class Library:
  def __init__(self, lid, lin):
    self.lid = lid
    self.lin = lin
    self.books = [0]

  def addbook(self, bkj):
    bkj.bkid = self.books[0]
    self.books.append(bkj)
    self.books[0] += 1

  def removebook(self, bkid):
    for i in range(1, len(self.books)):
      if self.books[i].bkid == bkid:
        del self.books[i]
        return True
    return False

  def getnames(self):
    return [f"{self.books[i].bkid} : {self.books[i].name} ({self.books[i].year})"
            for i in range(1, len(self.books))]

  def getbyname(self, name):
    for i in range(1, len(self.books)):
      if self.books[i].name == name:
        return self.books[i]
    return False

  def getbyaut(self, author):
    result = []
    for i in range(1, len(self.books)):
      if self.books[i].author == author:
        result.append(self.books[i])
    return result


class Book:
  def __init__(self, name, year, author):
    self.name = name
    self.year = year
    self.author = author

def formatedPrint(output):
  print("Назва книги : " + output.name)
  print("Рік першого видання : " + output.year)
  print("Автор книги : " + output.author)

lb1 = Library(0, "Бібліотека")

with open(sys.path[0] + "/library.csv", "r", encoding="utf-8") as table1:
  reader = list(csv.reader(table1))
  del reader[0]
  for row in reader:
    lb1.addbook(Book(row[0], row[1], row[2]))

while True:
  print("1. Додати книгу")
  print("2. Показати список книг")
  print("3. Пошук за? ")
  userInput = input("Що робимо? ")
  if userInput == "1":
    name = input("Введіть назву книги : ")
    year = input("Введіть рік видання: ")
    author = input("Введіть автора книги: ")
    print(f"ID Книги: {lb1.addbook(Book(name, year, author))}")
  elif userInput == "2":
    print(lb1.getnames())
  elif userInput == "3":
    while True:
      print("1) Пошук за назвою")
      print("2) Пошук за автором")
      userInput = input("Що робимо? ")
      if userInput == "1":
        bookOutput = lb1.getbyname(input("Введіть назву книги : "))
        if bookOutput:
          formatedPrint(bookOutput)
        else:
          print("Error")
      elif userInput == "2":
        bookOutput = lb1.getbyaut(input("Введіть автора книги: "))
        if bookOutput != []:
          for book in bookOutput:
            formatedPrint(book)
        else:
          print("Error")
        break