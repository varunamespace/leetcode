A = [3,3,3,2,2]
#A = [4,4,5,5,6,6]
def multi(n,A):
    ans = []
    dict = {}
    for i in A:
        if i==2:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
        tar = i
        for j in range(2,tar):
            if(tar%j==0):
                break
            if((tar%j)!=0):
                if tar not in dict:
                    dict[tar] = 1
                    break
                else:
                    dict[tar] = dict[tar] + 1
                    break
    for i in dict:
        if dict[i]>1:
            ans.append(i)

    return sorted(ans)

print(multi(5,A))
print()