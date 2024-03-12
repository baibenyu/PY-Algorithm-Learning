import datetime as dt


class Leapyear:
    def __init__(self):
        self.now = dt.date.today().year

    def isLeapyear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapyear(self.now):
            self.now -= 1
        temp = self.now
        self.now -= 1
        return temp

ly = Leapyear()
for i in ly:
    if i > 1800:
        print(i)
    else:
        break
