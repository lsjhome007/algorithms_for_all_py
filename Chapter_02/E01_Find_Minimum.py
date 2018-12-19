def find_min(a):

    min_value = a[0]

    list_length = len(a)

    for i in range(1, list_length):
        if a[i] < min_value:
            min_value = a[i]

    return min_value


if __name__ == '__main__':
    
    v = [17, 92, 18, 33, 58, 7, 33, 42]

    print (find_min(v))
