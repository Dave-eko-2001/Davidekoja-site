# Portfolio Site Python backend (Flask)
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Portfolio site backend running.'

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    # Here you would process contact form data, e.g., send email or store in DB
    return jsonify({'status': 'success', 'message': 'Message received.'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
