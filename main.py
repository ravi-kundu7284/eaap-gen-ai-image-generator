
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the EAAP Gen AI Image Generator!"



def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
