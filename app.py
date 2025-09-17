from flask import Flask

app = Flask(__name__)

@app.route('/')
def coming_soon():
    return '<h1>Coming Soon  THE ARKA 2025</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
