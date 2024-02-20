import matplotlib.pyplot as plt

x = [50, 100, 150, 200, 300]
y = [9.27, 14.90, 19.58, 23.36, 26.53]  # Removed the last element from y

plt.plot(x, y, marker='o')
plt.xlabel('Number of Topics')
plt.ylabel('Percentage of total variance')
plt.title('LSA Topic Selection')
plt.grid(True)
plt.savefig('lsa.png')
plt.show()
