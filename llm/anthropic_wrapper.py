import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

def call_llm(prompt, model="claude-3-opus-20240229"):
    response = client.messages.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )
    return response.content[0].text.strip()