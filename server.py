
# Using a 3rd party module to create a server with Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>My first web server. This is the base route.</p>"

@app.route("/hello")
def hello():
    return "<p>Hello, coder what are you doing here?</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show user profile for the specific user that is passed in
    return f'User {username}' #should return 'User <whatever username is passed in>'

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