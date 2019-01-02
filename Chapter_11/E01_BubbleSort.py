def bubble_sort(l):

    
    while True:
        changed = False
        for i in range(0, len(d)-1):
            
            if l[i] > l[i+1]:
                print (l)
                l[i], l[i+1] = l[i+1], l[i]
                
                changed = True
        if changed == False:
            return l

if __name__ == '__main__':
    d = [2, 4, 5, 1, 3]
    print (bubble_sort(d))
