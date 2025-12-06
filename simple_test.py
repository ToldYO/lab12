from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/quick-test')
def quick_test():
    return jsonify({"status": "ok", "time": time.time()})

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    print("Starting simple test server on port 3001...")
    app.run(host='0.0.0.0', port=3001, debug=False, threaded=True)
