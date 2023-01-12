for i in range(0, 50, 1):
    # path = 'cat-9/v2/out-{0}.json'.format(i)
    path = 'cat-9/hybrid-v1-v2/out-v2{0}.json'.format(i)
    f = open(path, 'r')
    sl = f.read()

    print(type(sl))
    newsl = '[{0}]'.format(sl)

    print(newsl)

    f.close()
    f = open(path, 'w')
    f.write(newsl)

