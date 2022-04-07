class StringClass:
    def __init__(self):
        self.name = input("Enter the String : ")

    def len(self):
        return len(self.name)

    def char(self, string):
        return list(string)


if __name__ == '__main__':
    obj = StringClass()
    print(obj.len())
    print(obj.char("Saquib"))