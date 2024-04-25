from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "NetSPI - Subdomain Takeover POC"
