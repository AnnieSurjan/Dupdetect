from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'DupDetect működik!'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    return f'Kaptunk kódot: {code}'

if __name__ == '__main__':
    app.run(port=8000)