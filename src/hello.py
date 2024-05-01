from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    response = {'message': 'Hello, M.NIRAV!'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
