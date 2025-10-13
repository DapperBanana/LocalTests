
import matplotlib.pyplot as plt

def generate_bar_chart(data):
    keys = list(data.keys())
    values = list(data.values())
    
    plt.bar(range(len(data)), values, tick_label=keys)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')
    
    plt.show()

# Dictionary of data
data = {'A': 10, 'B': 20, 'C': 15, 'D': 25}

generate_bar_chart(data)
