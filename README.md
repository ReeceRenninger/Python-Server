# Python-Server

Testing creating a Python server from docs and using a 3rd party (Flask)

## Setup

1. Clone repo down to local machine
2. Create a virtual environment of your choice, I used venv and the command is `python3 -m venv flaskenv`, the flaskenv will be the name of your virtual environment
3. (if you using pip for installs) run pip install -r requirements.txt
4. This will install all dependencies that Flask needs, this is stated in their documentation located [here](https://flask.palletsprojects.com/en/2.3.x/installation/#)
5. If you want to use the Flask portion of code, comment out the code above the import and then run flask --app server run, server is targeting the server.py file, so if you name your file hello.py, you would run flask --app hello run
6. If you want to use the base Python code, comment out all code below the import and run the file.
7. You made your first Python server!
