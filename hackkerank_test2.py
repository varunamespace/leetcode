cost = [2,5,3,11,1]
label = ["legal","illegal","legal","illegal","legal"]
target = 2
count = 0
cf = 0
big = []
for i in range(len(label)):
    if count==target:
        count = 0
        big.append(cf)
        cf = 0
    if count<target:
        if label[i] =="legal":
            count = count + 1
        cf = cf + cost[i]

print(max(big))

