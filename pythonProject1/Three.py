from Two import PairsPossible


class SearchCommonElements(PairsPossible):
    def __init__(self):
        super().__init__()
        self.commonElements = []
        temp = {}
        temp = temp.fromkeys(self.char(self.name), 0)

        for element in self.char(self.pairString):
            if temp.get(element) is not None:
                temp[element] += 1
        for element in temp:
            if temp[element] > 0:
                self.commonElements.append(element)


if __name__ == '__main__':
    obj = SearchCommonElements()