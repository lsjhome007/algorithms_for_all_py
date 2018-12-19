def recur_sum(n):
    
    if n == 1:

        return 1

    return n + recur_sum(n - 1)




if __name__ == '__main__':

    print (recur_sum(1))
    print (recur_sum(5))
    print (recur_sum(10))
