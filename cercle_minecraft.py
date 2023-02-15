import numpy as np
import matplotlib.pyplot as plt

# Parametres
size = 100

mat = np.zeros((size,size))

center = [size/2-0.5,size/2-0.5]
radius = size/2

for i in range(size):
    for j in range(size):
        if (i-center[0])**2+(j-center[1])**2<radius**2:
            mat[i,j]=1

# Init plot
fig, ax = plt.subplots()

# Plot Matrix
plt.imshow(mat,extent=[-size/2,size/2,-size/2,size/2])

# Plot lines
for i in range(size+1):
    plt.plot([i-radius,i-radius],[-radius,radius],'black')
    plt.plot([-radius,radius],[i-radius,i-radius],'black')
    
# Plot center
plt.scatter(0,0,c='red')

# Plot circle
circle = plt.Circle([0,0],radius,fill=False,color='b')
ax.set_aspect(1)
ax.add_artist(circle)
plt.show()