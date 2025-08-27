import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, send_file, abort, request
import subprocess
from ingress_folder.ingress import ingress_api

app = Flask(__name__)
app.register_blueprint(ingress_api)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def main_fe():
    return send_file(os.path.join(BASE_DIR, 'main_fe.html'))

@app.route('/ingress')
def handle_ingress():
    subprocess.run(['python', os.path.join(BASE_DIR, '..', 'ingress_folder', 'ingress.py')], check=False)
    return send_file(os.path.join(BASE_DIR, '..', 'ingress_folder', 'ingress_fe.html'))

##### remove this !!!!!!!
@app.route('/secret')
def handle_secret():
    subprocess.run(['python', os.path.join(BASE_DIR, '..', 'secret', 'secret.py')], check=False)
    return send_file(os.path.join(BASE_DIR, '..', 'secret', 'secret_fe.html'))

if __name__ == '__main__':
    app.run(debug=True)
