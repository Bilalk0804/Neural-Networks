import numpy as np
import time
a=np.array([1,2,3,4,5,6,7])
print(a)
tic=time.time()
a=np.random.rand(1000000)
b=np.random.rand(1000000)
c=np.dot(a,b)
toc=time.time()
print(c)
print('Vectorization :' + str(1000*(toc-tic))+'ms')
''''''
c=0;
tic=time.time()
for i in range(1000000):
    c+=a[i]*b[i]
toc=time.time()
print(c)
print('Vectorization :' + str(1000*(toc-tic))+'ms')