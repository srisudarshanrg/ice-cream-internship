from flask import render_template, request
from . import app
from .age_flavour_recommender import predict_flavour

@app.route("/", methods=["GET", "POST"])
def flavour_recommender():
    if request.method == "POST":
        gender = request.form.get("gender")
        age_group = request.form.get("age-group")

        prediction = predict_flavour(gender, age_group)
        return render_template("flavour_recommender.html", prediction=prediction)
    
    return render_template("flavour_recommender.html")