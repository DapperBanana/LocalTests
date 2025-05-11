
import matplotlib.pyplot as plt

def generate_bar_chart(data):
    keys = list(data.keys())
    values = list(data.values())
    
    plt.bar(keys, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Simple Bar Chart')
    plt.show()

# Sample data
data = {'A': 10, 'B': 20, 'C': 15, 'D': 25, 'E': 30}

generate_bar_chart(data)
