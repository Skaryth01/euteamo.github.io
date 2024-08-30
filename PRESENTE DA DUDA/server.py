from flask import Flask, send_from_directory, request, jsonify
import os
import json

app = Flask(__name__)

# Diretório para arquivos estáticos
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def index():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/save_message', methods=['POST'])
def save_message():
    message = request.json.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Adiciona a mensagem ao arquivo
    if not os.path.exists('static/messages.json'):
        with open('static/messages.json', 'w') as f:
            json.dump([], f)
    
    with open('static/messages.json', 'r+') as f:
        messages = json.load(f)
        messages.append(message)
        f.seek(0)
        json.dump(messages, f)

    return jsonify({'success': True})

@app.route('/load_messages', methods=['GET'])
def load_messages():
    if not os.path.exists('static/messages.json'):
        return jsonify([])

    with open('static/messages.json', 'r') as f:
        messages = json.load(f)
    
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
