
import matplotlib.pyplot as plt

def generate_bar_chart(data):
    labels = list(data.keys())
    values = list(data.values())

    plt.bar(labels, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')

    plt.show()

data = {
    'A': 10,
    'B': 20,
    'C': 15,
    'D': 25
}

generate_bar_chart(data)
