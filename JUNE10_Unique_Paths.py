def unique(m,n):
    row = [1]*n
    for i in range(m-1):
        newRow = [1]* n
        for j in range(n-2,-1,-1):
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
    return row[0]
print(unique(3,7))

def uni(m,n):
    row = [0]*(n-1)+[1]
    for i in range(m):
        for j in range(n-2,-1,-1):
            row[j] = row[j] + row[j+1]
    return row[0]
print(uni(3,7))

