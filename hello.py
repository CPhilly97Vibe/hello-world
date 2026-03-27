import http.server
import urllib.parse
import webbrowser
import threading


def build_greeting(name: str) -> str:
    cleaned_name = name.strip() or "world"
    return f"Hello, {cleaned_name}!"


HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Hello App</title>
    <style>
        body {
            font-family: -apple-system, Helvetica, Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #1a1a2e;
            color: #eee;
        }
        .card {
            background: #16213e;
            padding: 40px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        input {
            font-size: 18px;
            padding: 10px 16px;
            border: 2px solid #0f3460;
            border-radius: 8px;
            width: 260px;
            background: #1a1a2e;
            color: #eee;
            outline: none;
        }
        input:focus { border-color: #e94560; }
        button {
            font-size: 16px;
            padding: 10px 24px;
            background: #e94560;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 16px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        button:hover { background: #c73e54; }
        #greeting {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            min-height: 36px;
            color: #e94560;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>👋 Greeter</h2>
        <input type="text" id="name" placeholder="Type your name..." autofocus>
        <button onclick="greet()">Greet Me</button>
        <div id="greeting"></div>
    </div>
    <script>
        function greet() {
            const name = document.getElementById('name').value;
            fetch('/greet?name=' + encodeURIComponent(name))
                .then(r => r.text())
                .then(t => document.getElementById('greeting').textContent = t);
        }
        document.getElementById('name').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') greet();
        });
    </script>
</body>
</html>"""


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/greet"):
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            name = params.get("name", [""])[0]
            greeting = build_greeting(name)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(greeting.encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML.encode())

    def log_message(self, format, *args):
        pass  # suppress console noise


def main() -> None:
    port = 8765
    server = http.server.HTTPServer(("127.0.0.1", port), Handler)
    print(f"Running at http://127.0.0.1:{port} — press Ctrl+C to stop")
    threading.Timer(0.5, lambda: webbrowser.open(f"http://127.0.0.1:{port}")).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()


if __name__ == "__main__":
    main()
