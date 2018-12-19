def find_max(a):
    
    max_value = a[0]
    
    for value in a[1:]:
        if value > max_value:
            max_value = value
    return max_value


    
if __name__ == '__main__':
    
    v = [17, 92, 18, 33, 58, 7, 33, 42]

    print (find_max(v))
