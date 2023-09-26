def persistence(n):
    s = str(n)
    i = 0
    x = str(n)
    while True:
        s = str(x)
        for char in s:
            x = 1
            x *= int(char)
            if x <= 9:
                break
            i += 1

    return i

number = persistence(999)
print(number)