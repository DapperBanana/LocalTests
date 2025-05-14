
import matplotlib.pyplot as plt

data = {
    'A': 10,
    'B': 20,
    'C': 15,
    'D': 25
}

labels = data.keys()
values = data.values()

plt.bar(labels, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')

plt.show()
