number=[-10,2,3,7,5.4]
import time
start=time.time()
a=[89.7 , -12 , 74 , -5.1 , 140 , -12 , 9.2]
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]
print(a)
print("run time: " + str(time.time() - start))