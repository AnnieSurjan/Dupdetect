import os  # 🔹 Ez a sor kell, hogy működjön az os.getenv()

# Környezeti változók beolvasása
client_id = os.getenv("QB_CLIENT_ID")
client_secret = os.getenv("QB_CLIENT_SECRET")
access_token = os.getenv("QB_ACCESS_TOKEN")

# Ellenőrzés: kiírjuk, hogy sikerült-e beolvasni
print("Client ID:", client_id)
print("Client Secret:", client_secret)
print("Access Token:", access_token)

