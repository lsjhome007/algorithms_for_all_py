def gcd(a, b):

    small  = min(a, b)
    big = max(a, b)
    
    while True:

        if big % small == 0:
            return small

        else:
            small -= 1

if __name__ =="__main__":

    print (gcd(1, 5))
    print (gcd(3, 6))
    print (gcd(60, 24))
    print (gcd(81, 27))
