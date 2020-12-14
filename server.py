from flask import Flask, send_from_directory
import json

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


@app.route("/file/<path:subpath>")
def load_file(subpath):
    print(json.dumps({"name": 'File2', str(subpath): 'file', "content": [
          {"id": 'Undefined', "text": '4', "type": 'Markdown', "file": 'index.txt', "dirty": False}]}))
    return json.dumps({"name": str(subpath), 'type': 'file', "content": [{"id": 'Undefined', "text": '4', "type": 'Markdown', "file": 'index.txt', "dirty": False}]})

if __name__ == "__main__":
    app.run(debug=True)

