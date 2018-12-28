def find_ins_idx(r, v):

    n = len(r)

    for i in range(0, n):

        if v < r[i]:

            return i

    return n


def ins_sort(a):

    value_list = []

    while a:

        value = a.pop(0)

        idx = find_ins_idx(value_list, value)
        value_list.insert(idx, value)

    return value_list

if __name__ == '__main__':

    d = [2, 4, 5, 1, 3]

    print(ins_sort(d))