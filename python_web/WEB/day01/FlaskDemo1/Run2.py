from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    str = render_template('index.html')
    print(str)
    return str

if __name__ == '__main__':
    app.run(debug=True,port=5555)