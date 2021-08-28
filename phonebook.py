import os


class PhoneBook:
    def __init__(self):
        self.numbers = {}


    def lookup(self, name):
        return self.numbers[name]

    def add(self, name,number):
        self.numbers[name] = number

    def names(self):
        return set(self.numbers.keys())

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True

    def clear(self):
        self.cache.close()
        os.remove(self.filename)



