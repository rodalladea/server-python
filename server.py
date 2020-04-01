import http.server
import socketserver
from os import curdir, sep


PORT = 8082
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/':
      self.path = 'public/index.html'

    try:

      sendReply=False

      if self.path.endswith(".html"):
        mimetype='text/html'
        sendReply = True
      if self.path.endswith(".js"):
        mimetype='application/javascript'
        sendReply = True
      if self.path.endswith(".css"):
        
        mimetype='text/css'
        sendReply = True

      if sendReply == True:
        f = open(curdir + sep + self.path) 
        self.send_response(200)
        self.send_header('Content-Type', mimetype)
        self.end_headers()
        self.wfile.write(f.read().encode())
        f.close()
    
      return

    except IOError:
      self.send_error(404,'File Not Found: %s' % self.path)

handler_object = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
  print("serving port: ", PORT)
  httpd.serve_forever()