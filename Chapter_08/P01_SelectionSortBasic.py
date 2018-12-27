def find_min_id(a):

    n = len(a)
    min_idx = 0

    for i in range(1, n):

        if a[min_idx] > a[i]:
            min_idx = i

    return min_idx


def sel_sort(a):

    result = []

    while a:

        min_idx = find_min_id(a)
        min_value = a.pop(min_idx)
        result.append(min_value)
    return result



if __name__ == '__main__':

    d = [2, 4, 5, 1, 3]

    print (sel_sort(d))
