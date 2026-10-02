from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "deepseek-coder:6.7b"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    payload = {
        "model": MODEL_NAME,
        "prompt": user_message,
        "stream": False
    }

    response = requests.post(OLLAMA_API_URL, json=payload)

    data = response.json()

    return jsonify({
        "response": data.get(
            "response",
            "Sorry, I didn't understand that. Please try again."
        )
    })


if __name__ == "__main__":
    app.run(debug=True)