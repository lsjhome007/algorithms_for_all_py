def find_max_idx(a):

    list_len = len(a)
    
    max_idx = 0

    for i in range(1, list_len):
        
        if a[max_idx] < a[i]:
            max_idx = i

    return max_idx

if __name__ == '__main__':

    v = [17, 92, 18, 33, 58, 7, 33, 42]

    print (find_max_idx(v))
