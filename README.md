# Gemini-Ai-whatsapp-chatbot

#Introduction

In this Project, we will learn how to Build A WhatsApp Bot Using Python Bot using Python. A WhatsApp bot is a software application capable of communicating with users in both written and spoken formats. Our bot will use the Twilio API to connect with WhatsApp and perform tasks like sending and receiving messages, notifications, and more.

We’ll use the Python library Flask to handle incoming and outgoing messages and Ngrok to expose our Flask application to the public internet so that Twilio can communicate with it.


#Required Modules and Packages
To build this WhatsApp bot, you will need the following:

1.A Twilio Account: Sign up at Twilio and get a phone number with WhatsApp enabled.
2.Python 3.9 or Newer: Make sure you have Python installed on your system.
3.Flask: A lightweight web framework for Python that will be used to handle incoming HTTP requests from Twilio.
4.Ngrok: A tool that will help expose your Flask application running on your local machine to the internet.(install and create an account in ngrok)

#How To Run The Code 
Follow these steps to set up and run the WhatsApp bot:

Step 1: Set up a Twilio account by visiting Twilio WhatsApp. Sign up and verify your email ID and phone number.

Step 2: Once logged in, navigate to the Develop section in the left menu, select Messaging, and then choose Try it out -> Send a WhatsApp message. This will take you to a page for setting up the WhatsApp Sandbox.

Step 3: Configure the WhatsApp Sandbox by sending a message to the provided WhatsApp number (+14155238886) with a unique security code like join <secret-code>.

Step 4: Once you send the security code, you will receive a confirmation message in WhatsApp.

Step 5: Open the terminal and run the following commands to create a directory for the bot, set up a virtual environment, and install the required packages:

Create a Directory and Navigate to It:

mkdir whatsapp-bot && cd whatsapp-bot

Create and Activate a Python Virtual Environment:(windows)

python -m venv venv

venv\Scripts\activate


Install Twilio, Flask, and Requests:
 
pip install twilio flask requests

note:make sure that path of system variables set correctly.


How to Run the Bot

Run the Python Script:

python main.py

Start Ngrok Server: In a separate terminal window, run:

ngrok config add-authtoken YOUR_AUTHTOKEN(which is in ngrok dashboard)

ngrok http 5000

This command will expose the Flask application to the internet, allowing Twilio to connect to it.

Set Up the Forwarding URL: Copy the forwarding URL provided by Ngrok (it will look like http://<random-string>.ngrok.app) and paste it into the WhatsApp Sandbox settings at Twilio Sandbox Settings.

note:make sure \gemini is entered after the url.

Then scan the QR code to use the bot.
