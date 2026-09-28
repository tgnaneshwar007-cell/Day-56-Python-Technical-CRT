def vowels(s, i=0):
    if i == len(s):
        return

    if s[i].lower() in "aeiou":
        print(s[i], end=" ")

    vowels(s, i + 1)


s = input("Enter a string: ")
vowels(s)