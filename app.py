from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Online Boutique Demo</h1>
    <p>Version 1.0</p>
    <p>Deployed via GitHub Actions + ArgoCD + GKE</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
