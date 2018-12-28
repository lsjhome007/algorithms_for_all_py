def sel_sort(a):

    n = len(a)

    for i in range(0, n-1):

        min_idx = i

        for j in range(i+1, n):

            if a[min_idx] > a[j]:

                min_idx = j

        a[min_idx], a[i] = a[i], a[min_idx]

    return a

if __name__ == '__main__':


    a = [2, 3, 4, 1, 5]

    print (sel_sort(a))