import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Đọc biến môi trường để demo cho Task 0
    env = os.environ.get('APP_ENV', 'development')
    return jsonify({
        "message": "Hello DevOps Engineer!",
        "environment": env,
        "status": "healthy"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)