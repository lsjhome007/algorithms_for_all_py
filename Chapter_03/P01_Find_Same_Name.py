def find_same_name(a):

    result = set()

    n = len(a)


    # 먼저 시작되는 기준을 선택하고
    for i in range(0, n-1):
        # 비교되는 기준을 선택한다.
        for k in range(i+1, n):

            if a[i] == a[k]:

                result.add(a[i])

    return result


if __name__ == '__main__':

    name = ['Tom', 'Jerry', 'Mike', 'Tom']

    name_2 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']

    print (find_same_name(name))
    print (find_same_name(name_2))
