import http.server
import socketserver

PORT = 8002

Handler = http.server.SimpleHTTPRequestHandler

    print("serving at port", PORT)
    httpd.serve_forever()
