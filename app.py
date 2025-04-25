from flask import Flask
import psutil
app = Flask(__name__)
@app.route('/')
def home():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    return f"App Status: CPU {cpu}%, Memory {memory}% - {psutil.boot_time()}"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
