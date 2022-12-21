for i in range(1, 100, 1):
    path = 'v1_meh/out-{0}.json'.format(i)
    f = open(path, 'r')
    sl = f.read()

    print(type(sl))
    newsl = '[{0}]'.format(sl)

    print(newsl)

    f.close()
    f = open(path, 'w')
    f.write(newsl)

