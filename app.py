from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    Defines the index route for the Flask application.

    Returns:
        The rendered index.html template.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)
