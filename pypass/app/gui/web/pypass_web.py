from flask import Flask, render_template_string, request, jsonify
from .content import passgen_content, pass_content
import secrets
import string
import webbrowser
from threading import Timer

app = Flask(__name__)

def generate_password(length=12, exclude=None):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    if exclude:
        exclude_set = set(exclude)
        alphabet = ''.join(char for char in alphabet if char not in exclude_set)
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

@app.route('/', methods=['GET'])
def home():
    return render_template_string(pass_content)

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form.get('length', 12))
    exclude = request.form.get('exclude', '')
    password = generate_password(length, exclude)
    return jsonify({'password': password})

def open_browser():
    webbrowser.open_new('http://localhost:5000/')

def main():
    # Delay to allow server time to start
    Timer(1, open_browser).start()
    app.run()

if __name__ == "__main__":
    main()