def make_pair(a):

    n = len(a)

    for i in range(0, n-1):

        for k in range(i+1, n):

            print (a[i], '-' ,a[k])

if __name__ == '__main__':

    name = ['Tom', 'Jerry', 'Mike']

    make_pair(name)
