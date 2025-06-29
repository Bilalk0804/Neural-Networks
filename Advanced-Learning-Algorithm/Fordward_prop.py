import numpy as np
def sequential(x):
    '''
    a1=dense(  x,w1,b1)
    a2=dense(a1,w2,b2)
    for all the  neurons inside a layer
    f(z)=a4;
    return f()
    '''

    
def dense(a_in,w,b):
    dims=w.shape[1]
    a_out=np.zeros(dims)
    for i in range(dims):
        a_out[i]=np.dot(a_in,w[i])+b[i]
    a_out=g(z)
    return a_out
