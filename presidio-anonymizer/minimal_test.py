from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def test():
    return jsonify({"message": "test successful"})

@app.route('/genz-test')
def genz_test():
    return jsonify({
        "example": "Call Emily at 577-988-1234",
        "example_output": "Call GOAT at vibe check"
    })

if __name__ == '__main__':
    print("Starting minimal test on port 3003")
    app.run(host='0.0.0.0', port=3003, debug=True)
