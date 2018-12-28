def ins_sort(a):

    n = len(a)

    for i in range(1, n):

        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:

            a[j+1] = a[j]
            j -= 1

        a[j+1] = key

    return a

if __name__ == '__main__':

    d = [2, 4, 5, 1, 3]
    print (ins_sort(d))