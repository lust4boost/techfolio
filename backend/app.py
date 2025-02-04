##########################
# Import Flask functuion #
##########################

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



######################################
# Openai Route for Resume Generation #
######################################

# Import the OpenAI library
import openai 

# Set your OpenAI API key
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Parse the input data from the frontend
@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    data = request.json
    name = data.get('name', 'Unknown Candidate')
    skills = data.get('skills', 'No skills provided')
    experience = data.get('experience', 'No experience provided')

# Generate a prompt for OpenAI
    prompt = f"""
    Create a professional resume for the following individual:
    Name: {name}
    Skills: {skills}
    Experience: {experience}
    """

# Use OpenAI API to generate text
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        resume = response.choices[0].text.strip()
        return jsonify({"resume": resume})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

