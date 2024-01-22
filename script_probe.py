
import matplotlib.pyplot as plt

def generate_line_chart(data):
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Chart')
    plt.show()

# Example data
data = {'January': 50, 'February': 75, 'March': 45, 'April': 60}

# Generate line chart
generate_line_chart(data)
