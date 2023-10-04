
# Using a 3rd party module to create a server with Flask
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>My first web server. This is the base route.</p>"

@app.route("/hello")
def hello():
    return "<p>Hello, coder what are you doing here?</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login() #do_the_login() is a function that you would have to create
    else:
        return show_the_login_form() #show_the_login_form() is a function that you would have to create
    
@app.route('/user/<username>')
def show_user_profile(username):
    # show user profile for the specific user that is passed in
    return f'User {username}' #should return 'User <whatever username is passed in>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {subpath}'

with app.test_request_context(): #test_request_context() creates a test request context that you can use to test the functionality of request handling code. In this case, we are using it to test the url_for() function
    print(url_for('index')) #prints out the url for the index function
    print(url_for('hello')) #prints out the url for the hello function
    print(url_for('login')) #prints out the url for the login function

def show_the_login_form():
    return 'This is the login form'

def do_the_login():
    return 'You logged in!'

#** GET / POST requests **#
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

#** Rendering Templates **#
@app.route('/hello/<name>')
def hello_name(name=None): #set name to None so that if no name is passed in, it will still work
    return render_template('hello.html', name=name)

## Python docs way of creating a server

# from http.server import BaseHTTPRequestHandler, HTTPServer
# import time

# hostName = "localhost"
# serverPort = 8080

# class MyServer(BaseHTTPRequestHandler):
#   def do_GET(self):
#     self.send_response(200)
#     self.send_header("Content-type", "text/html")
#     self.end_headers()
#     self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
#     self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
#     self.wfile.write(bytes("<body>", "utf-8"))
#     self.wfile.write(bytes("<p>My first web server.</p>", "utf-8"))
#     self.wfile.write(bytes("</body></html>", "utf-8"))

# if __name__ == "__main__":
#   webServer = HTTPServer((hostName, serverPort), MyServer)
#   print("Server started http://%s:%s" % (hostName, serverPort))

#   try:
#     webServer.serve_forever()
#   except KeyboardInterrupt:
#     pass

#   webServer.server_close()
#   print("Server stopped.")