from flask import Flask, render_template, request, redirect, url_for


import numpy as np # Import the NumPy library
import random # Import the random library
import os # Import the os library 
from flask import send_from_directory  # Import the send_from_directory function from the Flask library


# run matplotlib gui in main thread
import matplotlib
matplotlib.use('Agg') # Set the backend of Matplotlib to 'Agg' to save plots as images
import matplotlib.pyplot as plt # Import the Matplotlib library




# Create a Flask app
app = Flask(__name__)



# function to load images from the static folder
def load_file(filename):
	return send_from_directory(filename)
	


def collect_data():
	data = []
	# generate random data
	for i in range(100):
		data.append(random.randint(0, 100))
	return data


# Function to visualize data
def visualize_data(data): 
	plt.plot(data)
	plt.xlabel('Data Point')
	plt.ylabel('Value')
	plt.title('Data Visualization')
	plt.savefig('static/plot.png')  # Save the plot as an image
	plt.close()

# route to load images
@app.route('/<filename>')
def send_image(filename):
	return send_from_directory("static", filename)


# Route to display the visualization in browser
@app.route('/') 
def index():
	data = collect_data()
	visualize_data(data)
	return render_template('index.html', data=data)

# Main program
if __name__ == '__main__':
	app.run()