
import matplotlib.pyplot as plt

data = {'apple': 10, 'banana': 8, 'orange': 5, 'grapes': 12}

plt.bar(data.keys(), data.values())
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.title('Fruit Quantity Bar Chart')
plt.show()
