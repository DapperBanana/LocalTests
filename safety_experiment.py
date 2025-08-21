
import matplotlib.pyplot as plt

data = {
    'January': 100,
    'February': 150,
    'March': 120,
    'April': 200,
    'May': 180
}

months = list(data.keys())
values = list(data.values())

plt.plot(months, values, marker='o')
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Simple Line Chart')
plt.grid(True)
plt.show()
