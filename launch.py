from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import threading
import webbrowser

server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(Path(__file__).resolve().parent)))
url = f"http://127.0.0.1:{server.server_port}/index.html"
print("ClearSky Tower:", url)
print("Keep this window open. Press Ctrl+C to stop.")
threading.Timer(0.6, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
