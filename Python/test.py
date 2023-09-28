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


def pig_it(text):
    l = 0
    list = text.split()
    print(list)
    z = []
    for x in list:
        a = x[0]
        n = ''
        for i in range(len(x) - 1):
            b = x[i + 1]
            n += b
        n += a
        n += 'ay'
        z.append(n)
    r = ''
    for i in range(len(z)):
        r += z[i]
        if i == (len(z) - 1):
            break
        r += ' '

    return r


number = pig_it('Pig latin is cool')

print(number)
