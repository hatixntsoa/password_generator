from flask import Flask, render_template_string, request, redirect, url_for
from pypass.app.gui.web.content import html_content

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission
        username = request.form.get('username')
        password = request.form.get('password')
        # Process the data (e.g., save it, perform some logic)
        return render_template_string(
            '<h1>Username: {{ username }} ; Password: {{ password }} </h1>', 
            username=username, password=password
        )
    
    # Render the form if GET request
    return render_template_string(html_content)

def main():
    app.run()

if __name__ == "__main__":
    main()
