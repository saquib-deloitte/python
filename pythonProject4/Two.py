lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

A = sum(map(lambda lst: list(lst).count('A'), lst1))
a = sum(map(lambda lst: list(lst).count('a'), lst1))

print(a, A)