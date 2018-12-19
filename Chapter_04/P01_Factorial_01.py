def fact(n):

    f  = 1

    for i in range(1, n+1):
        f *= i

    return f

if __name__ == '__main__':
    print (fact(1))
    print (fact(5))
    print (fact(10))


        
