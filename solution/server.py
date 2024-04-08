import http.server
import socketserver
import json
import urllib

orders = {}
order_id = 1

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global orders
        if self.path == '/orders':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(orders).encode())
        elif self.path.startswith('/orders/'):
            order_id = int(self.path.split('/')[-1])
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(orders[order_id]).encode())
        elif self.path.startswith('/orders?status='):
            status = urllib.parse.unquote(self.path.split('=')[-1])
            filtered_orders = {k: v for k, v in orders.items() if v['status'] == status}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(filtered_orders).encode())

    def do_POST(self):
        global orders
        global order_id
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        order = json.loads(post_data)
        orders[order_id] = order
        orders[order_id]['id'] = order_id
        order_id += 1
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(orders[order_id - 1]).encode())

    def do_PUT(self):
        global orders
        order_id = int(self.path.split('/')[-1])
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        update = json.loads(put_data)
        orders[order_id].update(update)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(orders[order_id]).encode())

    def do_DELETE(self):
        global orders
        order_id = int(self.path.split('/')[-1])
        del orders[order_id]
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'message': 'Orden eliminada'}).encode())

with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("serving at port", 8000)
    httpd.serve_forever()
