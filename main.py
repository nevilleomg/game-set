import numgen

numgen.fileGen()


def arrCardsGen():
    f = open('set.txt')
    arr = []
    for words in f.read().split():
        arr.append(words)
    s = ''
    arr_s = []
    for i in range(len(arr) // 4):
        s += arr[0]
        if arr[1][0] == 'с':
            s += 'b'  # blue
        elif arr[1][0] == 'к':
            s += 'r'  # red
        else:
            s += 'g'  # green
        if arr[2][1] == 'а':
            s += 'f'  # full
        elif arr[2][1] == 'о':
            s += 's'  # stripped
        else:
            s += 'e'  # empty
        if arr[3][0] == 'о':
            s += 'o'  # oval
        elif arr[3][0] == 'р':
            s += 'r'  # rhombuses
        else:
            s += 'b'  # bean
        for j in range(4):
            arr.pop(0)
        arr_s.append(s)
        s = ''
    f.close()
    return arr_s


def isSet(x, y, z):
    for i in range(4):
        if x[i] == y[i] == z[i]:
            return True
    return False


def findSets():
    arr = arrCardsGen()
    f = open('set.txt', 'a')
    f.write('\n')
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if isSet(arr[i], arr[j], arr[k]):
                    print(arr[i], arr[j], arr[k])
                    f.write('\n' + arr[i] + ' ' + arr[j] + ' ' + arr[k])
    f.close()


findSets()
