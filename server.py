import http.server
import socketserver

PORT = 8000

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()


        message = "Hello from a Docker container!"
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
