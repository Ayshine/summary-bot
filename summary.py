import os
import openai

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    print("Error: OpenAI API key environment variable not found.")
    exit(1)

openai.api_key = openai_api_key

def summarize(messages):
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Özetle: " + messages,  # 'Özetle' means 'Summarize' in Turkish
        max_tokens=150,  # Adjust as needed
        temperature=0.7)
    summary = response.choices[0].text.strip()
    
    return summary
