import os
import subprocess
import sys
import time
import urllib.request
import webbrowser

PORT = 8080

if getattr(sys, "frozen", False):
    base = os.path.dirname(sys.executable)
else:
    base = os.path.dirname(os.path.abspath(__file__))

server = os.path.join(base, "llama-server.exe")
model = os.path.join(base, "model.gguf")

if not os.path.exists(server) or not os.path.exists(model):
    input("llama-server.exe or model.gguf is missing. Press Enter to exit.")
    sys.exit(1)

proc = subprocess.Popen(
    [server, "-m", model, "-c", "2048", "-t", "4", "--port", str(PORT)],
    cwd=base,
)

print("Loading model, please wait...")
ready = False
for _ in range(120):
    if proc.poll() is not None:
        input("The server stopped unexpectedly. Press Enter to exit.")
        sys.exit(1)
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{PORT}/health", timeout=2)
        ready = True
        break
    except Exception:
        time.sleep(1)

if ready:
    webbrowser.open(f"http://localhost:{PORT}")
    print(f"Offline AI running at http://localhost:{PORT}")
else:
    print("Server is slow to start. Try opening the address manually.")

print("Close this window to stop the AI.")
try:
    proc.wait()
except KeyboardInterrupt:
    pass
finally:
    if proc.poll() is None:
        proc.terminate()
