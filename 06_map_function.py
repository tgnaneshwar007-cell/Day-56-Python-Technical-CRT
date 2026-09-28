# Map
# map(function, iterable)

s = input("Enter numbers separated by space: ").split()

d = list(map(int, s))
print(d)

d = list(map(float, s))
print(d)