from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        industry = request.form["industry"]
        rating = request.form["rating"]

        # print(name, industry, rating)

        if name == "" or industry == "":
            return render_template("index.html", message="Fill required fields!")

        return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
