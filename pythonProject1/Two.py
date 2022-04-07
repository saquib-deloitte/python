from One import StringClass


class PairsPossible(StringClass):
    def __init__(self):
        super().__init__()
        self.pairString = input("Enter String for Pairs : ")
        self.pairs = []

    def make(self):
        for x in range(len(self.pairString)):
            for y in range(x + 1, len(self.pairString)):
                pair = [self.pairString[x], self.pairString[y]]
                self.pairs.append(pair)

    def print(self):
        for element in self.pairs:
            print(element, end=" ")


if __name__ == '__main__':
    obj = PairsPossible()
    obj.make()
    obj.print()