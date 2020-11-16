import time
#Constants N and M used to define the 2d array and sum
N = M = 1024

#array and sum initialization
arr = [[1]*M] * N
sum = 0

#starting time function to give the time prior to executing the sum
start = time.time()
#executing first sum
for i in range(M):
    for j in range(N):
        sum+= arr[i][j]
#end time function after the sum is executed
end = time.time()
#the distance in time between the start of the sum execution and the end
distance = end - start
print('It took ', '%f' % (distance), ' seconds and the sum is ', sum)

#setting sum to 0 again for the second sum execution
sum = 0
#start time prior to the second execution of the sum
start = time.time()
for i in range(N):
    for j in range(M):
        sum+=arr[j][i]
#end time after the execution of the second sum
end = time.time()
#distance in time between the second sum's start and end times
distance = end - start
print('It took ', '%f' % (distance), ' seconds and the sum is ', sum)

