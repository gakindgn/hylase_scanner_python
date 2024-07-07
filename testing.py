from flask import Flask, render_template, request

import matplotlib.pyplot as plt

app = Flask(__name__)

# Function to collect data
def collect_data():
	data = []
	while True:
		value = input("Enter a data point (or 'q' to quit): ")
		if value == 'q':
			break
		data.append(float(value))
	return data

# Function to visualize data
def visualize_data(data):
	plt.plot(data)
	plt.xlabel('Data Point')
	plt.ylabel('Value')
	plt.title('Data Visualization')
	plt.savefig('static/plot.png')  # Save the plot as an image
	plt.close()

# Route to display the visualization in browser
@app.route('/')
def display_data():
	data = collect_data()
	visualize_data(data)
	return render_template('index.html', data=data)

# Route to display specific amount of data
@app.route('/plot', methods=['POST'])
def display_specific_data():
	start = int(request.form['start'])
	end = int(request.form['end'])
	data = collect_data()
	selected_data = data[start:end]
	visualize_data(selected_data)
	return render_template('index.html', data=selected_data)

# Main program
if __name__ == '__main__':
	app.run()