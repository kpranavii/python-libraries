import numpy as np

#np.array()
print("Using np.array()")
x=np.array([1,2,3,4,5])
print(x,"\n")

#np.arange()
print("Using np.arange()")
x=np.arange(1,10)
print(x,"\n")

#np.zeroes()
print("Using np.zeros()")
x= np.zeros(5)
print(x,"\n")

#np.linspace()
print("Using np.linspace()")
x=np.linspace(0,100,5)
print(x,"\n")

#reshape()
print("Using reshape()")
x=np.array([[1,2,3],[4,5,6]])
print(x,"\n")
x=x.reshape(3,2)
print(x,"\n")

#np.concatenate()
print("Using np.concatenate()")
x=np.array([1,2,3])
y=np.array([4,5,6])
z=np.concatenate([x,y])
print(z,"\n")

#np.array_split()
print("Using np.array_split()")
x=np.array([1,2,3,4,5,6])
y=np.array_split(x,4)
print(y,"\n")

#np.where()
print("Using np.where()")
x=np.array([1,4,3,4,5,6,7,8,9,12])
print(np.where(x==4),"\n")
