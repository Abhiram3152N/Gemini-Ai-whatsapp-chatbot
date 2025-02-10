from flask import Flask, request, jsonify
import google.generativeai as genai
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the Gemini API key from the environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Ensure API key is set
if not GEMINI_API_KEY:
    raise ValueError("Google Gemini API key is missing. Set it as an environment variable.")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Flask app
app = Flask(__name__)

# Function to generate responses using Gemini AI
def generate_answer(incoming_que):
    try:
        model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" model
        response = model.generate_content(incoming_que)
        return response.text  # Extract text response
    except Exception as e:
        print(f"Gemini AI error: {e}")
        return "Sorry, I am unable to process your request right now."

# Route to handle incoming WhatsApp messages
@app.route('/gemini', methods=['POST'])
def gemini():
    incoming_que = request.values.get('Body', '').strip()
    print("User Question:", incoming_que)

    if not incoming_que:
        return "Invalid request", 400

    answer = generate_answer(incoming_que)
    print("Bot Response:", answer)

    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    msg.body(answer)
    
    return str(bot_resp)

# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
