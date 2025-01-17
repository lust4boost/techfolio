<<<<<<< HEAD
# Import Flask and a helper function for JSON responses
from flask import Flask, jsonify

# Import CORS
from flask_cors import CORS

# Enable CORS for the Flask app
CORS(app)

# Create a Flask app instance
app = Flask(__name__)

# Define a route (URL) and its corresponding function
@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({"message": "This is a test route!"})

# Run the app in development mode
if __name__ == '__main__':
    app.run(debug=True)
