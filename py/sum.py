import time
N = M = 10

arr = [[1]*M] * N
sum = 0
start = time.time()
for i in range(M):
    for j in range(N):
        sum+= arr[i][j]
end = time.time()
distance = end - start
print('It took ', '%f' % (distance), ' seconds and the sum is ', sum)

sum = 0
start = time.time()
for i in range(N):
    for j in range(N):
        sum+=arr[i][j]
end = time.time()
distance = end - start
print('It took ', '%f' % (distance), ' seconds and the sum is ', sum)

