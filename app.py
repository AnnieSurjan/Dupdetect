from flask import Flask
import os

app = Flask(__name__)

# Beolvassuk a környezeti változókat
client_id = os.getenv("QB_CLIENT_ID")
client_secret = os.getenv("QB_CLIENT_SECRET")
access_token = os.getenv("QB_ACCESS_TOKEN")

@app.route("/")
def home():
    return f"""
    <h2>QuickBooks API teszt</h2>
    <p>Client ID: {client_id}</p>
    <p>Client Secret: {client_secret}</p>
    <p>Access Token: {access_token}</p>
    """

# Ezt a részt Render nem használja, de lokális teszthez jó
if __name__ == "__main__":
    app.run(debug=True)


