
# module_6_flask_app_example.py
# A simple Flask application with intentional bugs for debugging practice

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Intentional bug: Undefined variable 'template'
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
