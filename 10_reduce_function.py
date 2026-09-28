from functools import reduce

s = list(map(int, input("Enter numbers separated by space: ").split()))

result = reduce(lambda x, y: x + y, s)

print("Sum =", result)