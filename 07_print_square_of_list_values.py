s = list(map(int, input("Enter numbers separated by space: ").split()))

print("Original list:", s)

square = list(map(lambda x: x * x, s))

print("Square values:", square)