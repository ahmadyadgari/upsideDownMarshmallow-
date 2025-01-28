# upsideDownMarshmallow

This is a Flask web application that allows users to input data, analyze it using a grading script, and get feedback in a CSV format. The application uses the Groq API for processing and grading.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone this repository to your local machine:

   ```terminal
   git clone https://github.com/yourusername/upsideDownMarshmallow.git
   cd upsideDownMarshmallow

2. Install the required dependencies by running:

   ```terminal
   pip install -r requirements.txt

3. Ensure you have set up your environment variables correctly. Create a .env file in the root directory and add your Groq API key like this:

   ```terminal
   GROQ_API_KEY=your_api_key_here

## Running the Application

1. Start the Flask server by running:

   ```terminal
   python app.py
