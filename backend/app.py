#########################
# Import Flask & OpenAI #
#########################

from flask import Flask, jsonify, request  # Added `request` import
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv



############################
# Flask App Initialization #
############################

app = Flask(__name__)
CORS(app)

# Load OpenAI API Key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



######################################
# OpenAI Route for Resume Generation #
######################################

@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    data = request.json  # Fixed request parsing
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
    


##################################
# Default Route for Health Check #
##################################

@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

# ✅ Ensure this is placed at the end
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
