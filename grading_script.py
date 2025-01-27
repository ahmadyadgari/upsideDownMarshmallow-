import os
from groq import Groq
from termcolor import colored
from dotenv import load_dotenv
import builtins

def wrap_text(text, max_length=150):
    lines = text.splitlines(keepends=True)
    wrapped_lines = []

    for line in lines:
        if line.strip() == "":
            wrapped_lines.append("")
            continue

        words = line.split()
        current_line = []

        for word in words:
            if len(' '.join(current_line + [word])) > max_length:
                wrapped_lines.append(' '.join(current_line))
                current_line = [word]
            else:
                current_line.append(word)

        if current_line:
            wrapped_lines.append(' '.join(current_line))

        if line.endswith("\n"):
            wrapped_lines[-1] += "\n"

    return '\n'.join(wrapped_lines)

# Custom print function
def print(*args, max_length=150, **kwargs):
    text = ' '.join(str(arg) for arg in args)
    wrapped_text = wrap_text(text, max_length=max_length)
    builtins.print(wrapped_text, **kwargs)

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("API key not found. Please set it in your .env file as GROQ_API_KEY.")
    exit(1)

# Initialize Groq Client
client = Groq(api_key=api_key)

# Generate response using Groq
def generate_response(messages, model="llama-3.1-8b-instant", max_tokens=1500, temperature=0.7):
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature
        )
        response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        exit(1)

# Add system message to the chat
def add_system_message(chat, message):
    chat.append({"role": "system", "content": message})
    return chat

# Add user message to the chat
def add_user_message(chat, message):
    chat.append({"role": "user", "content": message})
    return chat

# Add AI message to the chat
def add_ai_message(chat, message):
    chat.append({"role": "assistant", "content": message})
    return chat

# Read data from data.txt
def read_data_from_file(file_path):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        raise FileNotFoundError(f"The file '{file_path}' is missing or empty.")

    with open(file_path, 'r') as file:
        data = file.read()
    return data

# Main program logic
def main():
    # Read data from a text file
    data_file = "data.txt"
    try:
        data_content = read_data_from_file(data_file)
    except FileNotFoundError as e:
        print(e)
        return

    # Initialize the conversation with a system message
    chat = []
    chat = add_system_message(chat, "You are a professional automatic grading tool.")

    # Define the one-shot prompt
    one_shot_prompt = f"""
    You are a professional Grading Tool.
    Based on these quiz results and rubric:

    Rubric:
    - Each question is worth 10 points.
    - Deduct 2 points for minor errors.
    - Deduct 5 points for major errors.
    - Full points for correct answers.

    Data:
    {data_content}

    Grade the quizzes according to the rubric in this format:

    Student Name | Question 1 | Question 2 | Question 3 | Total Score | Feedback
    ---------------------------------------------------------------------------
    Example      | 10         | 8          | 5          | 23/30      | Minor errors on Q2; major errors on Q3.

    Format the graded results into an easy-to-read and clean data sheet.
    """

    # Add the one-shot prompt to the chat
    chat = add_user_message(chat, one_shot_prompt)

    # Generate the response using Groq
    response = generate_response(chat, model="llama-3.1-8b-instant", max_tokens=1500, temperature=0.7)
    chat = add_ai_message(chat, response)

    # Print the output
    print("\nGraded Results:\n")
    formatted_response = response.replace("**", "").strip()
    print(colored(formatted_response, "green"))

if __name__ == "__main__":
    main()
