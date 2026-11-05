import os, subprocess, sys, time, webbrowser

base = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, frozen, False) else __file__))
server = os.path.join(base, llama-server.exe)
model = os.path.join(base, model.gguf)

if not (os.path.exists(server) and os.path.exists(model))
    input(llama-server.exe or model.gguf is missing. Press Enter to exit.)
    sys.exit(1)

proc = subprocess.Popen([server, -m, model, -c, 2048, -t, 4, --port, 8080], cwd=base)
time.sleep(6)
webbrowser.open(httplocalhost8080)
print(Offline AI running at httplocalhost8080 - close this window to stop.)
try
    proc.wait()
except KeyboardInterrupt
    proc.terminate()