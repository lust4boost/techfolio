# Import Flask and a helper for JSON responses
from flask import Flask, jsonify
from flask_cors import CORS

# Create a Flask app instance
app = Flask(__name__)

# Allow all origins to access all routes
CORS(app)

# Define a route (URL) and its corresponding function
@app.route('/api/test', methods=['GET'])
def test_route():
	return jsonify({"message": "This is a test route"})

# Default route
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Techfolio!"})

# Run the app in development mode
if __name__ == '__main__':
	app.run(debug=True)
