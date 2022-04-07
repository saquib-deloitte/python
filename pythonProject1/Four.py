from Three import SearchCommonElements


class EqualSumPairs(SearchCommonElements):
    def __init__(self):
        super().__init__()
        self.make()
        print("Output of Search Common Elements : ", self.commonElements)
        temp = {}
        for x in self.pairs:
            if temp.get(int(x[0]) + int(x[1])) != None:
                temp[int(x[0]) + int(x[1])] += 1
            else:
                temp[int(x[0]) + int(x[1])] = 0
        result = []
        for x in self.pairs:
            if temp[int(x[0]) + int(x[1])] == 0:
                result.append(x)
        print(result)
        print(len(result))


if __name__ == '__main__':
    obj = EqualSumPairs()