i = 5
while i != 0:
    print(i)
    i = i - 1

i = 10
while i != 0:
    print(i)
    j = i
    while j != 0:
        print(j)
        j = j - 1

        if j == 2:
            break
        elif j == 5:
            continue

    i = i - 1
