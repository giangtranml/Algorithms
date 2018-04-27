while True:
    n = int(input().strip())
    if n == 0:
        break
    no = True
    for fghij in range(1234, (98765//n)+1):
        abcde = fghij * n
        used = fghij < 10000
        tmp = abcde
        while tmp:
            used |= 1 << (tmp % 10)
            tmp //= 10
        tmp = fghij
        while tmp:
            used |= 1 << (tmp % 10)
            tmp //= 10
        if used == (1 << 10) - 1:
            print("%0.5d / %0.5d = %d" % (abcde, fghij, n))
            no = False
    if no:
        print("There are no solutions for %d" % n)
    print()
