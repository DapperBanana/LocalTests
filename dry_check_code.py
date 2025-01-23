
import matplotlib.pyplot as plt

data = {
    'Day 1': 10,
    'Day 2': 20,
    'Day 3': 30,
    'Day 4': 25,
    'Day 5': 15
}

days = list(data.keys())
values = list(data.values())

plt.plot(days, values)
plt.xlabel('Days')
plt.ylabel('Values')
plt.title('Simple Line Chart')

plt.show()
