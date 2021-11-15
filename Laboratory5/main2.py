class Student:
    def __init__(self, name, settings_dict):
        self.name = name                #Імя студента
        self.maxmark = settings_dict['maxmark']      #Максимальна оцінка
        self.maxmarkforlab = settings_dict['maxmarkforlab']     #Максимальна оцінка за лабораторну роботу
        self.labcnt = settings_dict['labcnt']       #К-сть лабораторних робіт для студента
        self.avt = settings_dict['avt']      #Оцінка автоматом
        self.sprobuLAB = 0       #К-сть спроб для лабораторної роботи
        self.sprobuIN = 0      #К-сть звичайних спроб
        self.labs = []         # Лабораторна


        for i in range(self.labcnt): self.labs.append(dict(tryCount = 0, mark = None))


    def passLabWork(self, mark, labID):
        if mark > self.maxmarkforlab:
            try:
                self.labs[labID]['tryCount'] += 1
                self.labs[labID]['mark'] = mark
                return True
            except IndexError:
                return False



        else:
            return False
    def passIndWork(self, mark):
        if mark > self.maxmark:
            self.sprobuIN += 1
            self.indWorkMark = mark
            return True
        else:
            return False