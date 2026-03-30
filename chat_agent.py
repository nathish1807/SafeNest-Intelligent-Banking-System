from openai import OpenAI

client = OpenAI(api_key="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")

def ask_bank_ai(question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful banking AI assistant that explains fraud detection, loans, and banking services."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content