# How to run the microservice
First, make sure the Flask package for Python is installed, either globally or in a virtual environment.

The simplest way to run the microservice is to just run the extension-attacher.py file with Python (e.g. navigate to this directory in a terminal and enter `python extension-attacher.py`). This will start the microservice's Flask server on whichever port is specified at the top of extension-attacher.py.

# How to request data
I'm using Python for these examples.

To request data, send an HTTP POST request to the microservice at the /attach endpoint. I used the Requests library to do this in Python. It can be installed with `pip install requests`. Here's an example request:
```python
data = {
	"name": "corvallis",
	"extension": "jpg"
}

requests.post("http://localhost:19283/attach", json=data)
```
The data must be a dictionary containing two keys:
- `name`, with the value being the desired file name 
- `extension`, with the value being the desired file extension

The data needs to be sent as JSON, which is what's happening in the `json=data` parameter. Also, the port number after `localhost:` should match the one from extension-attacher.py.

# How to receive data
`requests.post` will return the microservice's response, so you can assign it to a variable to save that response. Here's the same example, but with the response being saved to a variable called `response`:
```python
data = {
	"name": "corvallis",
	"extension": "jpg"
}

response = requests.post("http://localhost:19283/attach", json=data)
```
The response will be a dictionary with the requested filename. It will also contain a list of absolute paths for files that that match the requested filename and are within the microservice's folder or subfolders. For example, the microservice's file structure might look like this:
```
+ microservice (folder)
	- extension-attacher.py
	- README.md
	- requirements.txt
	+ images (folder)
		- corvallis.jpg
```
For the example request above, the response will look something like:
```python
{
	"filename": "corvallis.jpg",
	"filepaths": ["/bla/bla/bla/microservice/images/corvallis.jpg"]
}
```
The response will contain the filename even if no matching files are found.
