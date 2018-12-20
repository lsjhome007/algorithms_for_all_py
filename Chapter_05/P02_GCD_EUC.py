def gcd_euc(a, b):

    if b == 0:

        return a

    return gcd_euc(b, a%b)

if __name__ =="__main__":

    print (gcd_euc(1, 5))
    print (gcd_euc(3, 6))
    print (gcd_euc(60, 24))
    print (gcd_euc(81, 27))
