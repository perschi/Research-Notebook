from flask import Flask, send_from_directory
import random

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/filetree")
def send_filetree():
    return {
        "name": 'directory',
        "depth": 0,
        "type": 'directory',
        "sub_directories": [
           {"name": 'directory5',
            "type": 'directory',
            "depth": 1,
            "sub_directories": []},
           {"name": 'File1',
            "depth": 1,
            "type": 'file',
            "sub_directories": []}
        ]
    }

if __name__ == "__main__":
    app.run(debug=True)

