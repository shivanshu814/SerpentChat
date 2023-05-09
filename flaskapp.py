import os
import openai
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form['message']

        # Send request to OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
        )

        # Get generated text from response
        generated_text = completion["choices"][0]["text"]

        return render_template('index.html', response=generated_text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)))
