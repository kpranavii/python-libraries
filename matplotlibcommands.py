import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

#plot1
plt.subplot(2,2,1)
plt.plot(x,y)

#plot 2
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.subplot(2,2,2)
plt.scatter(x,y)


#plot3
x=np.array(["A","B","C","D"])
y=np.array([3,8,1,10])
plt.subplot(2,2,3)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.bar(x,y)

#plot4
x=np.array([50,25,5,15])
plt.subplot(2,2,4)
plt.pie(x)

plt.savefig("Graph.jpeg")
plt.show()


