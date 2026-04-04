import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [2,4,6,8])
left,right = plt.xlim(2,7)
bottom,top = plt.ylim(2,8)
print(left)
print(right) 
plt.show() 