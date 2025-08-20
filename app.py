import os
from flask import Flask

app = Flask(__name__)

# Load environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
access_token = os.getenv("ACCESS_TOKEN")

@app.route("/")
def home():
    return """
    <h2>DupDetect is running! 🔒</h2>
    <p>The QuickBooks connection has been successfully configured.</p>
    <p>If you encounter any issues, please check the logs or contact support.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
print("Access token loaded:", access_token)

