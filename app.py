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
    import os

client_id = os.getenv("QB_CLIENT_ID")
client_secret = os.getenv("QB_CLIENT_SECRET")
access_token = os.getenv("QB_ACCESS_TOKEN")

print("Client ID:", client_id)
print("Client Secret:", client_secret)
print("Access Token:", access_token)
