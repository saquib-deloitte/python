class clc(Exception):
    def __init__(self):
        pass
while True:
    frm = input("Enter the formula to calculate: ")
    if frm == "quit":
        break
    else:
        lst = frm.split(" ")
        while True:
            try:
                if len(lst) != 3:
                    raise clc
                else:
                    if lst[1] == '+' or lst[1] == '-':
                        try:
                            a = int(lst[0])
                            b = int(lst[2])
                            if lst[1] == '+':
                                print(a + b)
                                break
                            else:
                                print(a - b)
                                break
                        except ValueError:
                            print("Formula is invalid")
                            break
                    else:
                        raise clc
            except clc:
                print("Formula is Invalid")
                break