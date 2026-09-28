def even_numbers(s, i=0):
    if i == len(s):
        return

    if s[i] % 2 == 0:
        print(s[i], end=" ")

    even_numbers(s, i + 1)


s = list(map(int, input("Enter numbers separated by space: ").split()))

even_numbers(s)