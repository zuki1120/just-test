# example
import openai

openai.api_key = "your-api-key"

def call_llm(prompt, model="gpt-4", temperature=0.7):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=1024,
    )
    return response['choices'][0]['message']['content'].strip()