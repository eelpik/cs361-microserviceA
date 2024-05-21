from flask import Flask, abort, request
import os


app = Flask(__name__)
excluded_dirs = [".venv", ".git", "__pycache__"]


@app.route("/attach", methods=['POST'])
def attach_extension():
    data = request.get_json()

    # try getting data from request
    try:
        name = data["name"]
    except KeyError:
        abort(400, {"message": "Request is missing name"})

    try:
        extension = data["extension"]
    except KeyError:
        abort(400, {"message": "Request is missing extension"})

    # attach name and extension
    filename = name + "." + extension.strip(" .")

    # get list of matching files
    filepaths = []
    for root, dirs, files in os.walk(".", topdown=True):
        dirs[:] = [dir for dir in dirs if dir not in excluded_dirs]
        for file in files:
            if file == filename:
                filepath = os.path.join(root, file)
                filepath = os.path.abspath(filepath)
                filepaths.append(filepath)

    return {
        "filename": filename,
        "filepaths": filepaths
    }


if __name__ == "__main__":
    app.run(port=54321)
