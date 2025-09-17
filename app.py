from flask import Flask

app = Flask(__name__)

@app.route('/')
def coming_soon():
    return '<h1>Coming Soon</h1>'

if __name__ == '__main__':
    app.run(debug=True)
