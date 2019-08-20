from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://db:pw@db/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    rating = db.Column(db.Integer)

    def __init__(self, mail, name, industry, rating):
        self.mail = mail
        self.name = name
        self.industry = industry
        self.rating = rating


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        mail = request.form["mail"]
        name = request.form["name"]
        industry = request.form["industry"]
        rating = request.form["rating"]

        if mail == "" or name == "" or industry == "":
            return render_template("index.html", message="Fill required fields!")
        if db.session.query(Feedback).filter(Feedback.mail == mail).count() == 0:
            data = Feedback(mail, name, industry, rating)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")

        return render_template(
            "index.html", message="You already submitted your rating!"
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
