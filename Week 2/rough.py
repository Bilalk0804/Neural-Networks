import numpy as np
import matplotlib.pyplot as plt
# #a=np.zeros((10,10))
# #print(a)
# #print(type(a))
# # x=np.array([[[1],[2]],[[3],[4]]])
# # print(x.shape)
# t_image = np.array([[[ 0.67826139,  0.29380381],
#                      [ 0.90714982,  0.52835647],
#                      [ 0.4215251 ,  0.45017551]],

#                    [[ 0.92814219,  0.96677647],
#                     [ 0.85304703,  0.52351845],
#                     [ 0.19981397,  0.27417313]],

#                    [[ 0.60659855,  0.00533165],
#                     [ 0.10820313,  0.49978937],
#                     [ 0.34144279,  0.94630077]]])
# print(t_image.shape)
# t_image=np.linalg.norm(t_image,axis=1,keepdims=True) #meaning apply broadcasting and normilisation of a vector
# print(t_image)
# print(np.abs(10.5-4))
# def L1(yhat, y):
#     """
#     Arguments:
#     yhat -- vector of size m (predicted labels)
#     y -- vector of size m (true labels)
    
#     Returns:
#     loss -- the value of the L1 loss function defined above
#     """
    
#     #(≈ 1 line of code)
#     # loss = 
#     # YOUR CODE STARTS HERE
#     loss=np.abs(y-yhat)
#     # YOUR CODE ENDS HERE
    
#     return loss

# yhat = np.array([.9, 0.2, 0.1, .4, .9])
# y = np.array([1, 0, 0, 1, 1])
# print("L1 = " + str(L1(yhat, y)))
# dim=(2,1)
# index=1
# w=np.zeros(dim)
# print(w.shape)
# w = np.zeros((dim, 1))
# num=10
# count=0
# for i in range(num):
#     #print(i);
#     if i%num == 0:
#         count+=1
#         print(i)       
data = np.random.rand(50, 50)
plt.imshow(data, cmap='viridis')  # 'viridis' is a popular colormap
plt.colorbar()  # Show color scale
plt.title("Random Data Visualization")
plt.show()
