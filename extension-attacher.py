from flask import Flask, abort, request
import os


app = Flask(__name__)
excluded_dirs = [".venv", ".git", "__pycache__"]


@app.route("/attach", methods=['POST'])
def attach_extension():
    data = request.get_json()

    try:
        file_name = data["file-name"]
    except KeyError:
        abort(400, {"message": "Request is missing file-name"})

    try:
        file_extension = data["file-extension"]
    except KeyError:
        abort(400, {"message": "Request is missing file-extension"})

    full_filename = file_name + "." + file_extension.strip(".")

    # get list of matching files
    file_paths = []
    for root, dirs, files in os.walk(".", topdown=True):
        dirs[:] = [dir for dir in dirs if dir not in excluded_dirs]
        for file in files:
            if file == full_filename:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    # file_extension = file_extension.strip(" .")

    return {
        "file-name": full_filename,
        "file-paths": file_paths
    }


if __name__ == "__main__":
    app.run(port=54321)
