
def generate_bar_chart(data):
    max_value = max(data.values())
    
    for key, value in data.items():
        bar_length = int(value / max_value * 20)
        bar = '#' * bar_length
        print(f'{key}: {bar}')

data = {'A': 10, 'B': 20, 'C': 15, 'D': 5}

generate_bar_chart(data)
