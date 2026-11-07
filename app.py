from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Apex Timberline Operations - D6 Admin Hub Active'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)