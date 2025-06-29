import numpy as np
a=np.array([[12 ,23 ,54, 56],[23 ,46,68,54],[12,34,56,87]])
cap=a.sum(axis=0)
per=100*a/cap.reshape(1,4)
print(per)

b=np.array([[1,2,3],[4,5,6]])
copy=b+100  #copy of integer 100 id=s created in the form of an 2x3 matrix and submission is performed
print(copy) #This is colled broadcasting
b=np.array([[1,2,3],[4,5,6]])
c=np.array([[1],[2]])
copy=b+c    #this time broadcasting will be done horizontally
print(copy)