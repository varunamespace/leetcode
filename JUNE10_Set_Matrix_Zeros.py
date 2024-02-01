a = [[1,1,1],[1,0,1],[1,1,1]]
def find(a):
    n = len(a)
    l = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            #print(i,j,a[i][j])
            if a[i][j]==0:
                l.append((i,j))
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j and i in l:
                a[i][j] = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(i,j,a[i][j])
    print(a)

    print(l)

find(a)
