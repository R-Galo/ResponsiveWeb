from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def test_route():
    return jsonify({"message": "Backend is working!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)