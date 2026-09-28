s = list(map(int, input("Enter numbers separated by space: ").split()))

even = list(filter(lambda x: x % 2 == 0, s))

print("Even numbers:", even)