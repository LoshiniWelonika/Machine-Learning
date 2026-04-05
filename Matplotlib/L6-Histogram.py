import matplotlib.pyplot as plt

marks = [34,78,33,23,78,39,23,95,75,35]
plt.hist(marks, bins=[0,20,30,90], rwidth=0.95)
plt.show()