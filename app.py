from flask_notifications import notify
from flask import Flask
app = Flask(__name__)

@app.route('/')
def send_notification():
    notify("You have a new message!", recipient="igomue07@gmail.com")
    return "Notification sent!"
