def recur_max(a, n):

    if n == 1:
        
        return a[0]

    max_n_1 = recur_max(a, n-1)

    if max_n_1 > a[n-1]:

        return max_n_1

    return a[n-1]

if __name__ == '__main__':

    v = [17, 92, 18, 33, 58, 7, 33, 42]

    print (recur_max(v, len(v)))
